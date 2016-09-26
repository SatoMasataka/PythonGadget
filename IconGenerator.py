# coding: utf-8
import datetime
import math
from PIL import Image, ImageDraw, ImageFont
class Picture():
    
    def MakePicture(self,scaleX,scaleY,fontSize,tx,imgPath):
        marginX=2 #横余白
        marginY=0 #縦余白
        
        # 画像オブジェクトを作成。サイズと背景色を指定する。背景色はRGBAの各々をtupleにして与える。
        text_canvas = Image.new('RGBA', (scaleX,scaleY), (250, 250, 250,0))
        draw = ImageDraw.Draw(text_canvas)
        
        # フォントの種類とサイズを指定
        font = ImageFont.truetype('c:\\WINDOWS\\Fonts\\HGRSGU.TTC', fontSize)
        fon_x, fon_y = font.getsize(tx)
        
        #画像
        iconImage = Image.open(imgPath)
        img_x, img_y = iconImage.size
        scaleY_minusMargin=scaleY-marginY*2
        iconImage =iconImage.resize((img_x * scaleY_minusMargin / img_y , scaleY_minusMargin)) #縦横比を変えず高さを合わせてリサイズ
        img_x, img_y = iconImage.size
        
        # テキストを書き込み。引数は順に、書き込み座標（tuple）、テキスト、テキストのフォント、テキストのカラー
        draw.text((img_x+ marginX,(scaleY-fon_y)/2),tx, font=font, fill='#000')
        text_canvas.paste( iconImage, (  marginX, marginY ) )
        
        # 保存
        stamp = str(datetime.datetime.today().strftime("%Y%m%d%H%M%S"))
        text_canvas.save('TestImages\\'+stamp + '.png', 'PNG', quality=100, optimize=True)
  
p = Picture()
p.MakePicture(160,36,20,u'テステス','a.png')