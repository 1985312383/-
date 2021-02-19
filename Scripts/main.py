import random
import readJSON
import jieba
import docx

data = readJSON.readJson("data.json")
nonsense = data['nonsense']
abstract = data['abstract']
introduction = data['introduction']
conclusion = data['conclusion']
acknowledge = data['acknowledge']
reference = data['reference']


# 随机调用各data中的句子
def randomSentence(content):
    while True:
        random.shuffle(content)
        for j in content:
            yield j


next_nonsense = randomSentence(nonsense)
random_abstract = randomSentence(abstract)
random_introduction = randomSentence(introduction)
random_conclusion = randomSentence(conclusion)
random_acknowledge = randomSentence(acknowledge)
random_reference = randomSentence(reference)


def get_another_passage():
    another_passage = "\r\n"
    another_passage += "\t"
    return another_passage


def call_the_subject_again():
    return " "


def get_subject_content():
    return " "


def get_content():
    # doc = docx.Document()  # 以默认模板建立文档对象
    # doc = docx.Document('论文.docx')  # 读取a.docx文档，建立文档对象

    tmp = str()  # 存放生成的文字
    tmp += "标题：" + theme + "\n"

    # 添加摘要
    tmp += "摘要\n"
    tmp += next(random_abstract) + "\n"  # 摘要

    # 添加关键字
    tmp += "关键字\n   "
    keyword = jieba.lcut(theme)
    tmp += " ".join(keyword)
    tmp += "\n"

    # 添加引言
    tmp += "引言\n\t"
    tmp += next(random_introduction) + "\n"

    # 添加正文
    tmp += "正文\n\t"
    while len(tmp) < words:
        segmentationProbability = random.randint(0, 100)  # 下一句话的形式生成的概率
        if segmentationProbability < 5:  # 另起一段的概率为5%
            tmp += get_another_passage()
        elif segmentationProbability < 20:  # 再次称述主题的概率
            tmp += call_the_subject_again()
        elif segmentationProbability < 100:  # 胡编乱造的主要内容
            tmp += next(next_nonsense)
    tmp += "\n"

    # 添加结论or结束语
    tmp += "结论/结语\n"
    tmp += "\t" + next(random_conclusion) + "\n"

    # 添加鸣谢
    tmp += "鸣谢\n"
    for i in range(4):
        tmp += "\t" + next(random_acknowledge) + "\n"

    # 替换全文的主题i
    tmp = tmp.replace("i", theme)

    # 添加引用
    tmp += "引用\n"
    for i in range(8):
        tmp += "\t" + "[" + str(i + 1) + "] " + next(random_reference) + ".\n"

    # 打印全文，搞开发的小伙伴把下面的这话行代码取消注释就可以看控制台输出了
    # print(tmp)

    return tmp


if __name__ == "__main__":
    theme = input("请输入文章主题：")  # 全文反复横跳的主题
    # type = input("请输入论文类型") #确定调用哪个种类的语论文包
    words = int(input("大概多少字："))  # 论文字数

    # 输出所生成论文,生成docx文件
    tmp = get_content()

    # 输出TXT文件
    while txt != "y" or "n":
        txt = input("是否生成txt文件在当前目录下？(y/n)")
        if txt == "y":
            file = open('论文.txt', 'w')
            file.write(tmp)
        elif txt == "n":
            break
        else:
            print("请输入y或n!")
