from PIL import Image
import numpy as np
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--watermark', '-w', type=str, help='watermark file path')
    parser.add_argument('--input', '-i', type=str, help='input file path')
    parser.add_argument('--output', '-o', type=str, help='output file path')
    args = parser.parse_args()

    watermark_img = Image.open(args.watermark, 'r')
    watermark_width, watermark_height = watermark_img.size
    watermark_arr = np.asarray(watermark_img)

    input_img = Image.open(args.input, 'r')
    input_width, input_height = input_img.size
    input_arr = np.asarray(input_img)

    # 将隐藏图片扩充到输入图片的大小
    watermark_arr = np.tile(watermark_arr,
                            (int(input_height / watermark_height), int(input_width / watermark_width), 1))
    watermark_arr = np.pad(watermark_arr, (
        (0, input_arr.shape[0] - watermark_arr.shape[0]), (0, input_arr.shape[1] - watermark_arr.shape[1]), (0, 0)),
                           'constant')

    # 取隐藏图片的RGB最高位
    watermark_arr = np.bitwise_and(watermark_arr, np.full(input_arr.shape, int('10000000', 2), dtype='uint8'))
    watermark_arr = np.right_shift(watermark_arr, 7)

    # 将输入图片的RGB最低位设置为隐藏图片的RGB最高位
    input_arr = np.bitwise_and(input_arr, np.full(input_arr.shape, int('11111110', 2), dtype='uint8'))
    input_arr = np.bitwise_or(input_arr, watermark_arr)

    output_img = Image.fromarray(input_arr)
    output_img.save(args.output)
