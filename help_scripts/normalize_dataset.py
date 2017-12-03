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





df = pd.read_csv("../dataset-test.csv", header = -1)

allstr = ''
sizedic = {3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
dictionary = plt.figure()

newcsv = open("dataset-test.csv", "w")
for v in df.values:
    if len(v[1]) not in sizedic:
        print("Error with len ", len(v[1]))
        continue

    c = 8-len(v[1])
    newstr = ""
    for i in range(c):
        newstr = newstr + "-"

    newcsv.write("{},{}{}\n".format(v[0],v[1],newstr))

newcsv.close()
