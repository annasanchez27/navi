#!/bin/sh
python3 real_time_object_detection.py \
	--prototxt MobileNetSSD_deploy.prototxt.txt \
	--model MobileNetSSD_deploy.caffemodel
