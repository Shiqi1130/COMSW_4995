# Video Generation Based on a Single Image after Super-Resolution
This repo is for COMS4995 course project.
Our project aims to generate a smooth video based on a super resolution (SR) image. The first part of our project implements two models --  Zero-Shot Super Resolution3(MZSR) and SinGAN, to generate SR image. For futher function, 

## To downsample image you want to train:
```
python image_process.py width height downsample_factor input output
```
width and height is the resolution power of original image.
downsample_factor is the dowsample factor.
input includes the directory and the name of the image you want to process.
output includes the directory and the name of the image you have processed.


## MZSR
Credit goes to https://github.com/JWSoh/MZSR.

Type in :
```
python main.py --gpu 0 --inputpath Input/set/ --gtpath GT/set/ --savepath results/scale4 --kernelpath Input/g20/kernel.mat --model 1 --num 5  --scale 4
```
to run code with 5 iterations and scale is 4. 
We have 2 models with scaling factors 2 and 4 respectively.
Input has 2 files, one is for scale 2 and the other is for sacle 4.The original pictures are in GT.
MZSR can enhance the resolution within few iterations, which is faster than SinGAN.


## SinGAN
Credit goes to https://github.com/tamarott/SinGAN

To implement SR module, run
```
python SR.py --input_name <figure name.jpg> --sr_factor <upsampling scale, default=4>
```


## PSNR/SSIM
PSNR is chosen to be the average of three channels (i.e. RGB), greater value means better performance, identical images would lead to infinity value. SSIM is in range of (0,1], again, greater value is better.
