import argparse
import numpy as np
import cv2

import common
# import yuv_pb2
from SRNTT.SRNTT.model import *

from gabriel_protocol import gabriel_pb2
from gabriel_server import local_engine
from gabriel_server import cognitive_engine

COMPRESSION_PARAMS = [cv2.IMWRITE_JPEG_QUALITY, 67]

class DisplayEngine(cognitive_engine.Engine):
    def __init__(self, args):
        # Instantiate SRNTT model
        self.srntt = SRNTT(
            srntt_model_path=args.srntt_model_path,
            vgg19_model_path=args.vgg19_model_path,
            save_dir=args.save_dir,
            num_res_blocks=args.num_res_blocks,
        )
        print("SRNTT model initialized.")
        self.prev = None
        self.prev_orig = None

    def handle(self, input_frame):
    # check input_dir
        # input_frame.payloads[0] = [[ A, B, C],
        #                            [ D, E, F]]
        # where A = [R, G, B]

        # Preprocessing steps used by both engines
        np_data = np.frombuffer(input_frame.payloads[0], dtype=np.uint8)
        orig_img = cv2.imdecode(np_data, cv2.IMREAD_COLOR)

        # print(self.prev_orig == orig_img)
        # self.prev_orig = orig_img

        # Conversion from BGR -> RGB
        # orig_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2RGB)

        # TODO: Run test without reference on input image
        # srntt_frame = self.srntt.test_without_ref(
        #     input_dir=orig_img,
        #     ref_dir=None,
        #     use_pretrained_model=True,
        #     use_init_model_only=False,
        #     use_weight_map=False,
        #     result_dir="SRNTT/demo_testing_srntt",
        #     ref_scale=1.0,
        #     is_original_image=True
        #     # input_dir=args.input_dir,
        #     # ref_dir=args.ref_dir,
        #     # use_pretrained_model=args.use_pretrained_model,
        #     # use_init_model_only=args.use_init_model_only,
        #     # use_weight_map=args.use_weight_map,
        #     # result_dir=args.result_dir,
        #     # ref_scale=args.ref_scale,
        #     # is_original_image=args.is_original_image
        # )

        srntt_frame = self.srntt.test(
            input_dir=orig_img,
            ref_dir=orig_img,
            save_ref=False,
            result_dir="SRNTT/demo_testing_srntt",
        )

        # print(self.prev == srntt_frame)
        # self.prev = srntt_frame

        # Encode result as JPG and convert into payload bytes format
        # _, jpeg_img = cv2.imencode(".jpg", orig_img, COMPRESSION_PARAMS)
        _, jpeg_img = cv2.imencode(".jpg", srntt_frame, COMPRESSION_PARAMS)
        payload_img = jpeg_img.tostring()

        # print(f"payload_img: {len(payload_img)}, equality: {payload_img == input_frame.payloads[0]}")

        # PREV structure
        status = gabriel_pb2.ResultWrapper.Status.SUCCESS
        result_wrapper = cognitive_engine.create_result_wrapper(status)

        result = gabriel_pb2.ResultWrapper.Result()
        result.payload_type = gabriel_pb2.PayloadType.IMAGE
        result.payload = payload_img
        # result.payload = orig_img.tobytes()
        # result.payload = input_frame.payloads[0]
        result_wrapper.results.append(result)

        return result_wrapper


def main():
    print("I am here")
    common.configure_logging()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'source_name', nargs='?', default=common.DEFAULT_SOURCE_NAME)
    
    # Initialization Parameters
    parser.add_argument('--srntt_model_path', type=str, default='SRNTT/SRNTT/models/SRNTT')
    parser.add_argument('--vgg19_model_path', type=str, default='SRNTT/SRNTT/models/VGG19/imagenet-vgg-verydeep-19.mat')
    parser.add_argument('--save_dir', type=str, default=None, help='dir of saving intermediate training results')
    parser.add_argument('--num_res_blocks', type=int, default=16, help='number of residual blocks')

    # Test Parameters
    # parser.add_argument('--result_dir', type=str, default='result', help='dir of saving testing results')
    # parser.add_argument('--ref_scale', type=float, default=1.0)
    # parser.add_argument('--is_original_image', type=str2bool, default=True)
    
    args = parser.parse_args()

    def engine_factory():
        return DisplayEngine(args)

    local_engine.run(engine_factory, args.source_name, input_queue_maxsize=60,
                     port=common.WEBSOCKET_PORT, num_tokens=2)


if __name__ == '__main__':
    main()
