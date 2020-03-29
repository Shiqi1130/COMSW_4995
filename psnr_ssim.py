from PIL import Image
import numpy as np
import math


def psnr(im1, im2):
    '''
    Peak Signal to Noise Ratio, PSNR
    im1, im2: path to original and SR
    '''
    im1,im2 = Image.open(im1),Image.open(im2)
    im2 = im2.convert('RGB')
    im1,im2 = np.array(im1,dtype=np.float64),np.array(im2,dtype=np.float64)
    assert im1.shape == im2.shape
    diff = (im1 - im2).flatten()
    mse = np.mean(diff**2)
    if mse == 0:
        return np.infty
    else:
        return 10*math.log10(255**2/mse)


def ssim(im1, im2, K1=0.01, K2=0.03):
    '''
    Structural Similarity, SSIM
    Average of 3 channels of RGB format, in range of (0,1]
    im1, im2: path to original and SR
    '''
    im1,im2 = Image.open(im1),Image.open(im2)
    im2 = im2.convert('RGB')
    im1,im2 = np.array(im1,dtype=np.float64),np.array(im2,dtype=np.float64)
    assert im1.shape == im2.shape
    h,w,c = im1.shape

    def channel_mean(ch):
        return np.mean(ch.flatten())

    def channel_error(ch):
        m = channel_mean(ch)
        e = np.sum(((ch-m).flatten())**2)/(h*w-1)
        return m, e
    
    def channel_conv(ch1, ch2):
        (m1,e1),(m2,e2) = channel_error(ch1),channel_error(ch2)
        conv = np.sum(((ch1-m1)*(ch2-m2)).flatten())/(h*w-1)
        return m1,m2,e1,e2,conv

    def channel_ssim(ch1, ch2, K1=K1, K2=K2):
        C1 = (K1*255)**2
        C2 = (K2*255)**2
        C3 = C2/2
        m1,m2,e1,e2,conv = channel_conv(ch1, ch2)
        l = (2*m1*m2+C1)/(m1**2+m2**2+C1)
        c = (2*np.sqrt(e1*e2)+C2)/(e1+e2+C2)
        s = (conv+C3)/(np.sqrt(e1*e2)+C3)
        return l*c*s
    
    ssim = 0
    for i in range(3):
        ssim += channel_ssim(im1[:,:,i],im2[:,:,i],K1=K1,K2=K2)
    ssim = ssim/3

    return ssim

