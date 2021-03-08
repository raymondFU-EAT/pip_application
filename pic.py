from PIL import Image
import os #導入OS系統
for file in os.listdir('orig'): # 利用系統把資料夾orig中的檔案一個一個讀出
	if file.endswith('.jpg'): # 如果檔名的尾部為.jpg檔
	
		image_file = Image.open(os.path.join('orig',file)) 
		# open the file(.jpg) in orig with os system 
	
		image_file = image_file.convert('L') 
		# convert image to black and white
	
		image_file.save(os.path.join('result', file[:-4]+'_gray.png')) 
		# save the file(file[:-4]從前面數來倒數第四個字母才開始(把原來檔名.jpg剔除)_gray.png)