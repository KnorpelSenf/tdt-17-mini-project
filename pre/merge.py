#!/usr/bin/env python3
# -*- coding: utf8 -*-

import os
from shutil import copyfile


path = 'data/LiDAR-videos'
vids = [os.path.join(path, file)
        for file in sorted(os.listdir(path))
        if not file.endswith('est')]


index = 0
for vid in vids:
    i = os.path.join(vid, 'images')
    l = os.path.join(vid, 'labels')
    for [image, label] in zip(sorted(os.listdir(i)),  sorted(os.listdir(l))):
        from_i = os.path.join(i, image)
        from_l = os.path.join(l, label)
        target_i = os.path.join('data/train/images', str(index) + '-' + image)
        target_l = os.path.join('data/train/labels', str(index) + '-' + label)
        print(from_i, target_i)
        print(from_l, target_l)
        copyfile(from_i, target_i)
        copyfile(from_l, target_l)
        index += 1


index = 0
path = 'data/LiDAR-videos'
vids = [os.path.join(path, file)
        for file in sorted(os.listdir(path))
        if file.endswith('est')]
for vid in vids:
    i = os.path.join(vid, 'images')
    for image in sorted(os.listdir(i)):
        from_i = os.path.join(i, image)
        target_i = os.path.join('data/test/images', str(index) + '-' + image)
        print(from_i, target_i)
        copyfile(from_i, target_i)
        index += 1
