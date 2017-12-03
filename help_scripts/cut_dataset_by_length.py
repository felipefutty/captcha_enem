#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:56:13 2017

@author: feliperodrigues
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 00:31:51 2017

@author: feliperodrigues
"""

import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
#import plotly.plotly as py
import os
from PIL import Image





df = pd.read_csv("../dataset-joined-no-normalized.csv", header = -1)

sizedic = {3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
cut = 5
dir = "captcha-{}-joined".format(cut)
csvname = "dataset-{}-joined.csv".format(cut)
dir_old = "../captcha-joined"

newcsv = open(csvname, "w")
os.mkdir(dir)
k = 0
for v in df.values:
    if len(v[1]) not in sizedic:
        print("Error with len ", len(v[1]))
        continue

    if len(v[1]) != cut:
        continue

    img = Image.open("{}/{}.png".format(dir_old, v[0]))

    # Cut horizontally
    step = img.size[0]/cut
    for i in range(cut):
        area = (i*step, 0, (i+1)*step-1, img.size[1])
        print(area)
        cropped_img = img.crop(area)
        cropped_img.save("{}/{}.png".format(dir, k))
        newcsv.write("{},{}\n".format(k,v[1][i]))
        k += 1

newcsv.close()
