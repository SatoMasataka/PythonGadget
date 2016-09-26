# -*- coding: utf-8 -*-
import webbrowser
import PIL.ImageGrab
import datetime
import time
#http://d.hatena.ne.jp/white_wheels/20100311/p2
#残像

im=PIL.Image.open(u"C:/Users/Masataka/Pictures/na.jpg")
#time.sleep(10)
#im=PIL.ImageGrab.grab()
images=[]
#ちょっとずつ回転させた画像生成
for i in range(10):
    images.append(im.rotate(360/10 * (i)))
#画像合成
out=im
out2=im
for image in images:
    out=PIL.Image.blend(out,image, 0.1)
out.show()
#now=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#im.rotate(30).convert("L").save('screen'+now+'.png')
#im2=im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
#PIL.Image.blend(im,im2, 0.5).show()
