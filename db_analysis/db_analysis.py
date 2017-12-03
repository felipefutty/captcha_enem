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





df = pd.read_csv("../dataset-joined.csv", header = -1)

allstr = ''
sizedic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
dictionary = plt.figure()
for v in df.values:
    if len(v[1]) not in sizedic:
        print("Error with len ", len(v[1]))
    
    sizedic[len(v[1])] =  sizedic[len(v[1])] + 1
    allstr = allstr + v[1]

plt.xlabel('Captcha size')
plt.ylabel('Amount of samples')
plt.bar(range(len(sizedic)), sizedic.values(), align='center')
plt.xticks(range(len(sizedic)), sizedic.keys())
plt.show()


# Count chars
chardic = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g': 0,
           'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0,
           's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0,
           '0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0,
           }

aux = 0
for c in chardic.keys():
    chardic[c] = allstr.count(c)
    aux = aux + allstr.count(c)
    
plt.xlabel('Character')
plt.ylabel('Amount')
plt.bar(range(len(chardic)), chardic.values(), align='center')
plt.xticks(range(len(chardic)), chardic.keys())
plt.show()