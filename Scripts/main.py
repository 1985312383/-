import os
import re
import random
import readJSON

data = readJSON.readJson("data.json")
nonsense = data['nonsense']
abstract = data['abstract']


# 随机调用各data中的句子
def randomSentence(content):
    while True:
        random.shuffle(list(content))
        for j in list(content):
            yield j


next_nonsense = randomSentence(nonsense)
random_abstract = randomSentence(abstract)


def get_another_passage():
    another_passage = ". "
    another_passage += "\r\n"
    another_passage += "    "
    return another_passage


def call_the_subject_again():
    return " "


def get_subject_content():
    return " "


def get_content():
    tmp = str()  # 存放生成的文字
    tmp += "摘要\n"
    tmp += next(random_abstract) + "\n"# 摘要

    tmp += "正文\n"
    while len(tmp) < words:
        segmentationProbability = random.randint(0, 100)  # 下一句话的形式生成的概率
        if segmentationProbability < 5:  # 另起一段的概率为5%
            tmp += get_another_passage()
        elif segmentationProbability < 20:  # 再次称述主题的概率
            tmp += call_the_subject_again()
        elif segmentationProbability < 100:  # 胡编乱造的主要内容
            tmp += next(next_nonsense)
    tmp = tmp.replace("i", theme)
    print(tmp)


if __name__ == "__main__":
    theme = input("请输入文章主题：")  # 全文反复横跳的主题
    # type = input("请输入论文类型") #确定调用哪个种类的语论文包
    words = int(input("大概多少字："))  # 论文字数
    get_content()
