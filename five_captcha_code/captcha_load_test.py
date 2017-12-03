'''
Author:kemo

Trains a captcha datasets, each captcha includes four number.
Gets to 63.9% test accuracy after 64 epochs
(there is still a lot of margin for parameter tuning).
120 seconds per epoch on a Nvidia GeForce 940M GPU.
'''

from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility

from keras.models import Sequential
from keras.utils import np_utils
from keras import backend as K
from load_data import *
import h5py
from keras.callbacks import ModelCheckpoint
from sklearn.metrics import confusion_matrix
import itertools
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_fscore_support

import captcha_params
import load_model

# input image dimensions
img_rows, img_cols = captcha_params.get_height(), captcha_params.get_width()

batch_size = 512

MAX_CAPTCHA = captcha_params.get_captcha_size()
CHAR_SET_LEN = captcha_params.get_char_set_len()



### Test data
(X_train, Y_train), (X_test, Y_test) = load_data_test(tol_num = 495,train_num = 0)

# i use the theano backend
if K.image_dim_ordering() == 'th':
    X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

X_test = X_test.astype('float32')
X_test /= 255


model = load_model.get_model(input_shape)

model.compile(loss='categorical_crossentropy',
              optimizer='adadelta',
              metrics=['accuracy'])


score = model.evaluate(X_test, Y_test, verbose=0)
predict = model.predict(X_test,batch_size = batch_size,verbose = 0)


# calculate the accuracy with the test data
acc = 0

expected_str = []
predicted_str = []
labels=captcha_params.get_char_set()

for i in range(X_test.shape[0]):
    # Verify old captch
    if i%5 == 0 and i>=5:
        if expected_str[i-5:i] == predicted_str[i-5:i]:
            acc+=1
    if i%5 == 0 and i>=5 and i<=50:
        print(i, ' true: ', expected_str[i-5:i])
        print(i, ' predict: ', predicted_str[i-5:i])

    # Find out the captcha size
    len_captcha = MAX_CAPTCHA
    for j in reversed(range(MAX_CAPTCHA)):
        char_vec_true = Y_test[i, CHAR_SET_LEN * j:(j + 1) * CHAR_SET_LEN]
        char_true_idx = get_max(char_vec_true)
        if char_vec_true[char_true_idx] != 0:
            break
        len_captcha -= 1

    if len_captcha != 1:
        print("WARNING: Captcha has incorrect captcha length (!=1).")


    # Iterate over the chars
    for j in range(MAX_CAPTCHA):
        char_vec_true  = Y_test[i, CHAR_SET_LEN * j:(j + 1) * CHAR_SET_LEN]
        char_vec_pred  = predict[i,CHAR_SET_LEN*j:(j+1)*CHAR_SET_LEN]
        char_true_idx = get_max(char_vec_true)
        char_pred_idx = get_max(char_vec_pred)


        expected_str.append(labels[char_true_idx])
        predicted_str.append(labels[char_pred_idx])

if expected_str[i-4:i+1] == predicted_str[i-4:i+1]:
    acc += 1

print('predict correctly: ',acc)
print('total prediction: ',X_test.shape[0]/5)
print('Score: ',score)



# Recall and precision
plt.figure(figsize=(10,10))
metrics = precision_recall_fscore_support(expected_str, predicted_str, labels=labels)

dict_precision = {}
dict_recall = {}
for i in range(len(labels)):
    dict_precision[labels[i]] = metrics[0][i]
    dict_recall[labels[i]]  =  metrics[1][i]

plt.xlabel('Caracteres')
plt.ylabel('Precisao (%)')
plt.bar(range(len(dict_precision)), [dict_precision[key] for key in sorted(dict_precision.keys(), reverse=False)], align='center')
plt.xticks(range(len(dict_precision)), sorted(dict_precision.keys()))
plt.show()

plt.xlabel('Caracteres')
plt.ylabel('Revocacao (%)')
plt.bar(range(len(dict_recall)), [dict_recall[key] for key in sorted(dict_recall.keys(), reverse=False)], align='center')
plt.xticks(range(len(dict_recall)), sorted(dict_recall.keys()))
plt.show()

