# Video Generation Based on a Single Image after Super-Resolution
This repo is for COMS4995 course project.
Our project aims to generate a smooth video based on a super resolution (SR) image. The first part of our project implements two models --  Zero-Shot Super Resolution3(MZSR) and SinGAN, to generate SR image. For futher function, 

##To downsample image you want to train:
```
python image_process.py width height downsample_factor input output
```
width and height is the resolution power of original image.
downsample_factor is the dowsample factor.
input includes the directory and the name of the image you want to process.
output includes the directory and the name of the image you have processed.


## MZSR
Credit goes to https://github.com/JWSoh/MZSR

## SinGAN
Credit goes to https://github.com/tamarott/SinGAN

To implement SR module, run
```
python SR.py --input_name <pic_name.jpg> --sr_factor <sr_factor, default=4>
```
