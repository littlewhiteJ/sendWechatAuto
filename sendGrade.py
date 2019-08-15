import csv
import itertools
import wechat
import datetime
import os


today = str(datetime.date.today())
datetoday = int(today.split('-')[2])


# 这里写你的.csv表格的名称(不含.csv)
######################################
fileName = 'week3'
######################################

'''
datetoday1 = int(fileName.split('.')[1])

if datetoday != datetoday1:
    print(datetoday)
    print(datetoday1)
    print('date error!')
    os._exit(0)
'''


textFileName = fileName + '.txt'
csvFileName = fileName + '.csv'

textFile = open(textFileName,'w')
wechat.login()

with open(csvFileName, 'r') as csvFile:
    reader, reader0 = itertools.tee(csv.reader(csvFile))

    tagLength = int((len(next(reader0)) - 2) / 2)
    # print(tagLength)

    tag = []

    flag = 1

    for item in reader:
        output = ''
        if flag:
            for i in range(tagLength):
                
                # print(item[i * 2 + 2])
                tag.append(item[i * 2 + 2])    
            flag = 0
            # print(tag)       
            continue

        #l = len(tag)
        print(item)

        output += item[1] + '家长您好\n\n'
        output += '21天的奋斗结束了，孩子坚持下来，就是成功！\n但高中的奋斗，才刚刚开始，21天的苦修，不过是一个序曲。\n所谓，有志者事竟成；苦心人天不负。高中的学习没有捷径，成功的人生没有坦途。\n作为孩子们的辅导员老师，我还想再唠叨几句：\n一、心态最重要，壁立千仞，无欲则刚。\n二、身体很重要，修学先健身。 \n三、吃好睡好玩好。\n四、好好学习\n最后的最后，麻烦您转达给孩子我衷心的祝愿：\n加油吧，少年少女们！\n201 姜宇航'
        output += '\n\n'
        if int(item[6]) != 0:
            remarkname = item[1] + '家长'
            output += '附第三次周测成绩:\n'
            for i in range(tagLength):
                if float(item[2*i+2]) == 0:
                    continue
                output += str(tag[i])
                output += ':'
                output += str(item[2*i+2])
                output += '分，等级'
                output += item[2*i+3]
                output += '\n'
            output += '\n'


        wechat.sendInfo(remarkname, output)
        # break
        textFile.write(output + '\n')
        

    
        

textFile.close()
