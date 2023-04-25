import matplotlib.pyplot as plt
import keras_ocr

pipeline = keras_ocr.pipeline.Pipeline()

x = keras_ocr.detection.Detector()
print(x.detect("test_img.png"))