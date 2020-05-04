# Video Generation Based on a Single Image after Super-Resolution
This repo is created for deep learning course project.  
Our project aims to generate a smooth super resolution video based on a low resolution image. The first part of our project is to implement two models, Zero-Shot Super Resolution3(MZSR) and SinGAN, to generate SR images. The second part is to use SinGAN to generate videos from SR images given by the previous step. 

## Brief Explanation of Contents
```
├── Input:
    ├──> GT: orginal images (480*320)
    ├──> LR: down-sampled images (factor of 2 or 4)
├── Output: 
    ├──> SR_image: SR images (480*320) created by MZSR or SinGAN
    ├──> SR_video: videos created by SinGAN from SR images
├── MZSR: modified from previous MZSR works 
├── SinGAN: modified from previous SinGAN works
├── SR.py: super resolution
├── SR_video.py: SR & video generation
├── downsample.py: downsample imamges by factor of 2 or 4
├── evaluate.py: PSNR&SSIM computation
```

## Downsample
To downsample a 480*320 image by factor of 2 or 4, run:
```
python downsample.py --original_file <filename> --lr_factor <downsample factor, [2,4]> 
```

## Super Resolution
To do SR task on a downsampled image, run:
```
python SR.py --method <['SinGAN','MZSR']> --sr_factor <scaling factor, [2,4]> --input_name <filename> --num <number of iterations of MZSR, [1,5,10]> --max_size 480
```

## Super Resolution Video
To generate a video from an SR image, run:
```
python SR_video.py --method <['SinGAN','MZSR']> --sr_factor <scaling factor, [2,4]> --input_name <filename> --num <number of iterations of MZSR, [1,5,10]> --animation_start_scale <generation start scale, [0,1,2]> --beta_animation <animation random walk second moment, [0.80,0.85,0.90,0.95]> --max_size 480
```

## PSNR/SSIM
PSNR is chosen to be the average of three channels (i.e. RGB), greater value means better performance, identical images would lead to infinity value. SSIM is in range of (0,1], again, greater value is better.

PSNR/SSIM of two videos are calculated by averaging PSNR/SSIM scores of all frame pairs.

To calculate scores, run:
```
python evalutate.py --mode <file type ['image','video']> --file1 <path of file1> --file2 <path of file2>
```

## References
SinGAN: Credit goes to https://github.com/tamarott/SinGAN  
MZSR: Credit goes to https://github.com/JWSoh/MZSR
