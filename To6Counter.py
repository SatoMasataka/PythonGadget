# coding: sjis
import datetime
import math
d = datetime.datetime.today()
tstr = str(d.year)+' ' + str(d.month) +' ' +  str(d.day) + ' 18:00:00'
endtime = datetime.datetime.strptime(tstr, '%Y %m %d %H:%M:%S')
nokori = (endtime - d).total_seconds()
if nokori <= 0 :
    print '�{���͏I�����܂���'
else : 
    nH = int(nokori/(60*60))
    nM = int(math.ceil((nokori % (60*60))/60))
    print '����'+ str(nH) + '����' + str(nM) + '��'