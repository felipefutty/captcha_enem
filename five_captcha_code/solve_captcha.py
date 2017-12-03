
import sys
from load_data import *
import captcha_params
import load_model
import io
from PIL import Image

MAX_CAPTCHA = captcha_params.get_captcha_size()
CHAR_SET_LEN = captcha_params.get_char_set_len()

class CaptchaEval:

	def __init__(self):
		# load the trained model
		self.model = load_model.get_model('')

		self.model.compile(loss='categorical_crossentropy',
		              optimizer='adadelta',
		              metrics=['accuracy'])

   
	def predict_from_img(self, img):
		X_test = get_x_input_from_image(img)

		predict = self.model.predict(X_test)

		text = ''
		for i in range(X_test.shape[0]):
		    predict2 = []
		    for j in range(MAX_CAPTCHA):
		        char_index = get_max(predict[i,CHAR_SET_LEN*j:(j+1)*CHAR_SET_LEN])
		        char = captcha_params.get_char_set()[char_index]
		        predict2.append(char)
		    text = text.join(predict2)

		return text


if len(sys.argv) == 2:
	fileName = sys.argv[1]
	text = ""
	# Split in 5 peaces
	k=0
	cut=5
	step = img.size[0]/cut
	for i in range(cut):
		filename="tmp/{}.png".format(k)
		area = (i*step, 0, (i+1)*step-1, img.size[1])
		cropped_img = img.crop(area)
		cropped_img.save(filename)
                
                # Predict each peace
		with open(fileName, mode='rb') as file: # b is important -> binary
			fileContent = file.read()

		stream = io.BytesIO(fileContent)

		localImage = Image.open(stream)

		captchaEval = CaptchaEval()

		letter = captchaEval.predict_from_img(localImage)
		text = text + letter
		k += 1

	print(text)
