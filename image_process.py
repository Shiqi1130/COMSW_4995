from PIL import Image
import sys


def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)

def main():
    width = int(sys.argv[1])//int(sys.argv[3])
    height = int(sys.argv[2])//int(sys.argv[3])
    input_img = sys.argv[4]
    output_img = sys.argv[5]
    produceImage(input_img, width, height, output_img)

if __name__ == '__main__':
    main()