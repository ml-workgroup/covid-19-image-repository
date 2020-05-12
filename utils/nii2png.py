#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from glob import glob
import numpy as np
import nibabel as nib
from skimage.exposure import rescale_intensity
import cv2
from tqdm import tqdm
import argparse


def image_resize(image, width):
    (h, w) = image.shape[:2]
    height = h * (float(width) / w)
    height = int(height)
    return cv2.resize(image, (width, height))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='convert nii to png',
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', metavar='<dir>', default='../nii/', type=str,
                        help='input directory')
    parser.add_argument('-o', metavar='<dir>', default='../png/', type=str,
                        help='output directory')
    args = parser.parse_args()

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

    for fn in tqdm(glob(path.join(args.i, '*.nii.gz'))):
        root, cn = path.split(fn)
        cnx = cn.split('.nii.gz')[0]
        out_fn = path.join(args.o, f'{cnx}.png')

        if path.exists(out_fn):
            continue

        img = nib.load(fn)
        im = img.get_data().T
        im = np.squeeze(im)
        assert len(im.shape) == 2, f'im.shape == {im.shape}'

        im = rescale_intensity(im, in_range='image', out_range=(0, 255))

        im_r = image_resize(im, width=640)
        im_c = clahe.apply(im_r.astype(np.uint8))

        cv2.imwrite(out_fn, im_c)