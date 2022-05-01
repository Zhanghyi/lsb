from PIL import Image
import numpy as np
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=str, help='input file path')
    parser.add_argument('--output', '-o', type=str, help='output file path')
    args = parser.parse_args()

    input_img = Image.open(args.input, 'r')
    input_arr = np.asarray(input_img)

    # 将输入图片的RGB最低位提取出来 作为隐藏图片RGB取值
    input_arr = np.bitwise_and(input_arr, np.full(input_arr.shape, int('00000001', 2), dtype='uint8'))
    input_arr = input_arr * 255

    output_img = Image.fromarray(input_arr)
    output_img.save(args.output)
