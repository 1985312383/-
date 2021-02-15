import os
import re
import random
import readJSON

data = readJSON.readJson("data.json")
bosh = data['boshi']


def randomSentence(boshi):
    while True:
        random.shuffle(list(boshi))
        for j in list(boshi):
            return str(j)


next_boshi = randomSentence(bosh)


def get_another_passage():
    another_passage = ". "
    another_passage += "\r\n"
    another_passage += "    "
    return another_passage


def call_the_subject_again():
    return " "


def get_subject_content():
    return " "


if __name__ == "__main__":
    theme = input("请输入文章主题：")  # 全文反复横跳的主题
    # type = input("请输入论文类型") #确定调用哪个种类的语论文包
    words = int(input("大概多少字："))  # 论文字数
    for i in theme:
        tmp = str()  # 存放生成的文字
        while len(tmp) < words:
            segmentationProbability = random.randint(0, 100)  # 下一句话的形式生成的概率
            if segmentationProbability < 5:  # 另起一段的概率为5%
                tmp += get_another_passage()
            elif segmentationProbability < 20:  # 再次称述主题的概率
                tmp += call_the_subject_again()
            elif segmentationProbability < 100:  # 胡编乱造的主要内容
                tmp += next(randomSentence(next_boshi))
        tmp = tmp.replace("i", theme)
        print(tmp)
