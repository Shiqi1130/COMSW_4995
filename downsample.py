from PIL import Image
import argparse
import os


def process(filename, factor, indir, outdir):
    outname = filename[:-4] + '_x' + str(factor) + '.png'
    inpath = os.path.join(indir, filename)
    outpath = os.path.join(outdir, outname)
    image = Image.open(inpath)
    w,h = image.size
    resized_image = image.resize((w//factor, h//factor))
    resized_image.save(outpath)

    
def main(args):
    indir, outdir = args.original_dir, args.lr_dir
    name = args.original_file
    factor = args.lr_factor
    process(name, factor, indir, outdir)

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--original_dir', help='ground truth dir', default='Input/GT')
    parser.add_argument('--lr_dir', help='low resolution dir', default='Input/LR')
    parser.add_argument('--original_file', help='path of original file', required=True)
    parser.add_argument('--lr_factor', type=int, help='downsample factor', choices=[2,4], required=True)
    args = parser.parse_args()
    main(args)