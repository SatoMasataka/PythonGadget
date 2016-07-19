# -*- coding: utf-8 -*-
import lxml.html
import urllib2
import Tkinter as Tk
import tkMessageBox
import threading
import time
import datetime
class NewsWindow(Tk.Frame):
    """ニュースを集めて表示"""        
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title('本日のトピック')
        
    #googleニュースを集めてくる
    def GetYahooNews(self):
        #http://www.cafe-gentle.jp/challenge/tips/python_tips_001.html
        htmlPage = urllib2.urlopen('https://news.google.co.jp/').read() # html 取得
        root = lxml.html.fromstring(htmlPage)
        return root.xpath('//span[@class="titletext"]')
    #静的ウィンドウ表示
    def DispNews(self,dispMode=1):
        #http://www.shido.info/py/tkinter2.html
        topics=self.GetYahooNews()
        
        #引数dispMode別に表示変更
        for (i,topic) in enumerate(topics):
            la = Tk.Label(self, text = topic.text,relief=Tk.RIDGE, bd=2, font=('Times', '9'),bg='LightSkyBlue')
            if dispMode==0:
                now_side = Tk.LEFT if i%2==0 else Tk.TOP
                la.pack(anchor=Tk.W, side=Tk.TOP)
            else:
                la.grid(row=i/2, column=i%2,sticky=Tk.W + Tk.E)
        else:
            self.pack()
            self.mainloop()
            
    #動的ウィンドウ表示
    def DispNewsDynamic(self):
        topics=self.GetYahooNews()
        #ラベルテキストリスト
        echo=[]
        for i in range(4):
            echo.append(Tk.StringVar())
        
        #ラベルリスト
        self.dy_label=[]
        for i in range(4):
            self.dy_label.append(
                Tk.Label(self, textvariable=echo[i],relief=Tk.RIDGE,
                         bd=2,width=80, font=('Times', '9'),bg='LightSkyBlue')
            )
        
        #タイトルラベル 
        now=datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        tit_label=Tk.Label(self, text = "本日のトピック",bd=2, font=('Times', '12'))
        time_label=Tk.Label(self, text = now+"現在",bd=2, font=('Times', '8'))
       
        #ラベル配置
        self.dy_label[0].grid(row=0, column=0,sticky=Tk.W + Tk.E)
        self.dy_label[1].grid(row=0, column=1,sticky=Tk.W + Tk.E)
        time_label.grid(row=1, column=0,columnspan=2,sticky=Tk.W + Tk.E)
        tit_label.grid(row=2, column=0,columnspan=2,sticky=Tk.W + Tk.E)
        self.dy_label[2].grid(row=3, column=0,sticky=Tk.W + Tk.E)
        self.dy_label[3].grid(row=3, column=1,sticky=Tk.W + Tk.E)
        #スレッド起動
        thr=TopicThread(topics,echo)
        thr.start()
        self.pack()
        self.mainloop()
        
#動的ウィンドウ表示用スレッド処理          
class TopicThread(threading.Thread):
    """docstring for TestThread"""
    #http://qiita.com/konnyakmannan/items/2f0e3f00137db10f56a7
    
    def __init__(self, topics, echo):
        super(TopicThread, self).__init__()
        self.t = topics
        self.e = echo
    def run(self):
        while True:
            for (i,topic) in enumerate(self.t):
                time.sleep(2)
                #ターゲットになるStringVarを指定
                targetE=self.e[i%len(self.e)]
                targetE.set(topic.text)
if __name__ == "__main__":
    n=NewsWindow()
    n.DispNewsDynamic()
    #n.DispNews(1)
