# coding: utf-8
import datetime
import math
from PIL import Image, ImageDraw, ImageFont
class Picture():
    
    def MakePicture(self,scaleX,scaleY,fontSize,tx,imgPath):
        marginX=2 #���]��
        marginY=0 #�c�]��
        
        # �摜�I�u�W�F�N�g���쐬�B�T�C�Y�Ɣw�i�F���w�肷��B�w�i�F��RGBA�̊e�X��tuple�ɂ��ė^����B
        text_canvas = Image.new('RGBA', (scaleX,scaleY), (250, 250, 250,0))
        draw = ImageDraw.Draw(text_canvas)
        
        # �t�H���g�̎�ނƃT�C�Y���w��
        font = ImageFont.truetype('c:\\WINDOWS\\Fonts\\HGRSGU.TTC', fontSize)
        fon_x, fon_y = font.getsize(tx)
        
        #�摜
        iconImage = Image.open(imgPath)
        img_x, img_y = iconImage.size
        scaleY_minusMargin=scaleY-marginY*2
        iconImage =iconImage.resize((img_x * scaleY_minusMargin / img_y , scaleY_minusMargin)) #�c�����ς������������킹�ă��T�C�Y
        img_x, img_y = iconImage.size
        
        # �e�L�X�g���������݁B�����͏��ɁA�������ݍ��W�ituple�j�A�e�L�X�g�A�e�L�X�g�̃t�H���g�A�e�L�X�g�̃J���[
        draw.text((img_x+ marginX,(scaleY-fon_y)/2),tx, font=font, fill='#000')
        text_canvas.paste( iconImage, (  marginX, marginY ) )
        
        # �ۑ�
        stamp = str(datetime.datetime.today().strftime("%Y%m%d%H%M%S"))
        text_canvas.save('TestImages\\'+stamp + '.png', 'PNG', quality=100, optimize=True)
  
p = Picture()
p.MakePicture(160,36,20,u'�e�X�e�X','a.png')