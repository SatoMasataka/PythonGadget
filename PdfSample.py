# -*- coding: utf-8 -*- 
import os
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.units import cm
if __name__ == "__main__":
    if os.path.exists("./python.pdf"):
        os.remove("./python.pdf")
        
    pdfFile = canvas.Canvas("./python.pdf")
    pdfFile.saveState()
    pdfFile.setAuthor("python-izm.com")
    pdfFile.setTitle(u"PDFê∂ê¨")
    pdfFile.setSubject(u"ÉTÉìÉvÉã")
    #    A4
    pdfFile.setPageSize((21.0*cm,29.7*cm))
    #    B5
#   pdfFile.setPageSize((18.2*cm,25.7*cm))
    pdfFile.setFillColorRGB(0,0,100)
    pdfFile.rect(2*cm,2*cm,6*cm,6*cm,stroke=1,fill=1)
    pdfFile.setFillColorRGB(0,0,0)
    pdfFile.setLineWidth(1)
    pdfFile.line(0*cm,25*cm,21*cm,25*cm)
    pdfmetrics.registerFont(UnicodeCIDFont("HeiseiKakuGo-W5"))
    pdfFile.setFont("HeiseiKakuGo-W5",3*cm)
    pdfFile.drawString(0*cm,25.6*cm,u"ÅõÅõå©êœèë")
    
    pdfFile.restoreState()
    pdfFile.save()
