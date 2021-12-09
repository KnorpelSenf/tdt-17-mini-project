# TDT 17 Mini Project

Source code for object detection using YOLOv5s.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Preprocessing

1. Copy the data into this repo to ./data.zip. (It is listed in .gitignore.)
2. Run `./pre/extract.sh`

This will create a folder `data`, and prepare everything that is necessary.

## Training, Inference and Evaluation

This project uses https://github.com/ultralytics/yolov5.

1. Clone that repo
2. Copy the file `dataset.yaml` from this repo into that repo
3. Perform training as stated in the instructions

