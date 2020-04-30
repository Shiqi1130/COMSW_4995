from SinGAN.config import get_arguments
from SinGAN.SinGAN.manipulate import *
from SinGAN.SinGAN.training import *
from SinGAN.SinGAN.imresize import imresize
import SinGAN.SinGAN.functions as functions
import os


def SR(args):
    args.mode = 'SR'
    sr_factor = args.sr_factor
    inname = args.input_name
    method = args.method
    num = args.num
    os.system('python SR.py --method %s --input_name %s --sr_factor %d' %(method,inname,sr_factor))
    if method == 'SinGAN':
        sr_name = 'SinGAN_%s.png' % (inname[:-4])
    else:
        sr_name = 'MZSR_iter=%02d_%s.png' % (num,inname[:-4])
    args.input_name = sr_name
    return args


def animation(args):
    args.mode = 'animation'
    args.input_dir = 'Output/SR_image'
    args.out = 'Output/SR_video'
    opt = functions.post_config(args)
    Gs = []
    Zs = []
    reals = []
    NoiseAmp = []
    dir2save = functions.generate_dir2save(opt)
    if True:
        opt.min_size = 20
        opt.mode = 'animation_train'
        real = functions.read_image(opt)
        functions.adjust_scales2image(real, opt)
        dir2trained_model = functions.generate_dir2save(opt)
        if (os.path.exists(dir2trained_model)):
            Gs, Zs, reals, NoiseAmp = functions.load_trained_pyramid(opt)
            opt.mode = 'animation'
        else:
            train(opt, Gs, Zs, reals, NoiseAmp)
            opt.mode = 'animation'
        try:
            os.makedirs(dir2save)
        except OSError:
            pass
        start_scale = opt.animation_start_scale
        beta = opt.beta_animation
        generate_gif(Gs, Zs, reals, NoiseAmp, opt, beta, start_scale)


if __name__ == '__main__':
    parser = get_arguments()
    parser.add_argument('--animation_start_scale', type=int, help='generation start scale', choices=[0,1,2], required=True)
    parser.add_argument('--alpha_animation', type=float, help='animation random walk first moment', default=0.1)
    parser.add_argument('--beta_animation', type=float, help='animation random walk second moment', choices=[0.8,0.85,0.9,0.95], required=True)
    parser.add_argument('--input_dir', help='input image dir', default='Input/LR')
    parser.add_argument('--input_name', help='input image name', required=True)
    parser.add_argument('--mode', help='task to be done', default='animation')
    parser.add_argument('--method', help='SinGAN or MZSR', choices=['SinGAN','MZSR'], required=True)
    parser.add_argument('--sr_factor', type=int, help='super resolution factor', choices=[1,2,4], default=4, required=True)
    parser.add_argument('--out',help='output folder',default='Output/SR_image')
    parser.add_argument('--gtpath', type=str, help='gtpath', default='Input/GT')
    parser.add_argument('--kernelpath', type=str, help='kernelpath', default='MZSR/Input/g20/kernel.mat')
    parser.add_argument('--num', type=int, help='num_of_adaptation', choices=[1,5,10], default=1)
    parser.add_argument('--gpu', type=str, help='gpu', default='0')
    args = parser.parse_args()
    if args.sr_factor == 1:
        animation(args)
    else:
        args = SR(args)
        animation(args)