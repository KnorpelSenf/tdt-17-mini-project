#!/bin/bash
set -e

# Run from repo root

for vid in $(echo data/*Ano); do
    ./pre/imgseries.py $vid/*ient.avi -o $vid/images
done
