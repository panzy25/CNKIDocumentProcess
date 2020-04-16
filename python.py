# coding:utf-8
# Written by panzy25

import os
import sys
import re

keywd = sys.argv[1]
data = []
temp = ""
# classify the documents based on whether there is a summary within
e1 = open("/Users/tommypan/Desktop/txt-" + keywd + "WithSummary.txt", 'a')
e2 = open("/Users/tommypan/Desktop/txt-" + keywd + "WithoutSummary.txt", 'a')
f = open("/Users/tommypan/Desktop/CNKI-" + keywd + ".txt")

for line in f:
    if len(line) == 1:
        if temp != "":
            data.append(temp)
            temp = ""
    else:
        temp += line

# test
# for block in data:
#	print(block)
# print(data[0],data[1])

# it can be evolved to be a function

for block in data:
    key = block

    if "摘要" in key:
        if "题名" in key:
            p1 = r"(.*)(题名)(...)(.*)"
            pattern1 = re.compile(p1)
            m1 = re.search(pattern1, key)
            e1.write(m1.group(4))
            e1.write('\t')
        else:
            e1.write("null")
            e1.write('\t')

        if "作者" in key:
            p2 = r"(.*)(作者)(...)(.*)"
            pattern2 = re.compile(p2)
            m2 = re.search(pattern2, key)
            e1.write(m2.group(4))
            e1.write('\t')
        else:
            e1.write("null")
            e1.write('\t')

        if "单位" in key:
            p3 = r"(.*)(单位)(...)(.*)"
            pattern3 = re.compile(p3)
            m3 = re.search(pattern3, key)
            e1.write(m3.group(4))
            e1.write('\t')
        else:
            e1.write("null")
            e1.write('\t')

        p4 = r"(.*)(摘要)(...)(.*)"
        pattern4 = re.compile(p4)
        m4 = re.search(pattern4, key)
        e1.write(m4.group(4))
        e1.write('\t')

        #		else:
        #			e1.write("null")
        #			e1.write('\t')

        if "发表时间" in key:
            p5 = r"(.*)(发表时间)(...)(.*)"
            pattern5 = re.compile(p5)
            m5 = re.search(pattern5, key)
            e1.write(m5.group(4))
        else:
            e1.write("null")

        e1.write('\n')

    else:
        if "题名" in key:
            p1 = r"(.*)(题名)(...)(.*)"
            pattern1 = re.compile(p1)
            m1 = re.search(pattern1, key)
            e2.write(m1.group(4))
            e2.write('\t')
        else:
            e2.write("null")
            e2.write('\t')

        if "作者" in key:
            p2 = r"(.*)(作者)(...)(.*)"
            pattern2 = re.compile(p2)
            m2 = re.search(pattern2, key)
            e2.write(m2.group(4))
            e2.write('\t')
        else:
            e2.write("null")
            e2.write('\t')

        if "单位" in key:
            p3 = r"(.*)(单位)(...)(.*)"
            pattern3 = re.compile(p3)
            m3 = re.search(pattern3, key)
            e2.write(m3.group(4))
            e2.write('\t')
        else:
            e2.write("null")
            e2.write('\t')

        if "发表时间" in key:
            p5 = r"(.*)(发表时间)(...)(.*)"
            pattern5 = re.compile(p5)
            m5 = re.search(pattern5, key)
            e2.write(m5.group(4))
        else:
            e2.write("null")

        e2.write('\n')

e1.close()
e2.close()
