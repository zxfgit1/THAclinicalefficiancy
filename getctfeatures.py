# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 17:08:49 2021

@author: PC
"""

import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import os
import nrrd
import imageio
import radiomics
from radiomics import featureextractor
# In[]
def make_mask(image_p):
    image_path = image_p
    new_path = os.path.join(image_path,"image/")
    folder = os.listdir(new_path)
    
    for items in folder:
        path1 = os.path.join(new_path,items)
        img= path1
        print(img)
        if img.split('.')[-1] in ['tif','tiff']:
            ir = cv2.imread(path1,cv2.IMREAD_GRAYSCALE)
            ir2 = cv2.resize(ir,(512,512))
            ir1 = np.array(ir2)
            ir2 = ir1
        else:
            ir = Image.open(img)
            ir2 = ir.resize((512,512),Image.ANTIALIAS)
            #save_img.append(np.array(ir2))
            ir1 = np.array(ir2)
            ir2 = ir1
        ir2[ir2<60]=0
        ir3 = ir2
        ir3[ir2>0]=1
        output_path = os.path.join(image_path,"img/")
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        nrrd.write("%simg.nrrd"%output_path,ir1)
        img_path = os.path.join(image_path,"img/img.nrrd")
        output_path_mask = os.path.join(image_path,"mask/")
        if not os.path.exists(output_path_mask):
            os.mkdir(output_path_mask)
        nrrd.write("%smask.nrrd"%output_path_mask,ir3)
        mask_path = os.path.join(output_path_mask,'mask.nrrd')
    return(img_path,mask_path)
# In[]
def ct_feature(image_p):
    extractor = featureextractor.RadiomicsFeatureExtractor()
    extractor.enableAllFeatures()
    img_path,mask_path = make_mask(image_p)
    featureVector = extractor.execute(img_path,mask_path)
    ct1 = featureVector['original_shape2D_Elongation']
    ct2 = featureVector['original_shape2D_MaximumDiameter']
    ct3 = featureVector['original_shape2D_Sphericity']
    return(ct1,ct2,ct3)
