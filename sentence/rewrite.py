#!/usr/bin/python
# -*- coding: UTF-8 -*-
import jieba,codecs
fos = codecs.open("negtive.txt", "r", encoding="UTF-8")
count = 1
while 1:
    line = fos.readline()
    if line:
        print line
        indexl = line.find('>')
        line2 = line[(1+indexl):]
        print line2
        indexr = line2.find('<')
        line3 = line2[0:indexr]
        print line3
        seg_list = jieba.cut(line3, cut_all=False)
        values = " ".join(seg_list)        
        fod = codecs.open("./train/0/"+str(count)+".txt", "w+", encoding="UTF-8")
        fod.write(values)
        fod.close()
        count = count + 1
    else:
        break
fos.close()
