import os
import shutil
import csv
import numpy as np
import pandas as pd
import cv2


if __name__ == "__main__":
    org = os.getcwd()
    TrainingDataDir = org + '/TrainingData'
    TestDataDir = org + '/TestData'
    os.chdir('FlickrLogos-v2/classes/jpg')
    for brand in os.listdir():
        if not '.' in brand:
            os.chdir(brand)
            for img in os.listdir():
                if '.jpg' in img:
                    shutil.copy(img, TrainingDataDir + '/image/' + img)
                    bbox = img + '.bboxes.txt'
                    bbox = pd.read_csv('../../masks/' + brand + '/' + bbox, sep=' ')
                    with open(TrainingDataDir + '/txt/' + img[:-4] + '.txt', 'a', encoding='utf-8') as f:
                        wr = csv.writer(f)
                        for i in range(len(bbox)):
                            x, y, width, height = bbox.iloc[i]
                            pos = (x + width // 2, y + height // 2)
                            length = (width, height)
                            deg = 0
                            bbox = cv2.boxPoints((pos, length, deg))
                            poly = np.array(bbox).astype(np.int32).reshape((-1))
                            wr.writerow(poly)
            os.chdir('..')
    os.chdir(org)
