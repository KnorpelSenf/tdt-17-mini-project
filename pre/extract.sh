#!/bin/bash

# Run from next to data.zip

unzip data.zip
cd data/LiDAR-videos/

for vid in $(echo *Ano); do
    cd $vid
    unzip *yolo.zip
    mv obj_train_data labels
    cd -
done
