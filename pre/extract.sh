#!/bin/bash
set -e
# Run from next to data.zip

unzip data.zip

for vid in $(echo data/LiDAR-videos/*Ano); do
    cd $vid
    unzip *yolo.zip
    mv obj_train_data labels
    cd -
done

rm data/LiDAR-videos/Video00001_Ano/Video00004_*.avi

for vid in $(echo data/LiDAR-videos/*); do
    ./pre/imgseries.py $vid/*ient.avi -o $vid/images
done

mkdir -p data/{train,test}/{labels,images}
./pre/merge.py
