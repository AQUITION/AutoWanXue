import json

if __name__ == '__main__':
    question_id = int(input('请输入第一题题号'))

    emList = list()  # 整个页面的所有题对象

    for i in range(1, 11):
        answerText = input('请输入第' + str(i) + '题答案') # 题目输入String
        answersList = list(answerText) #String切分成字符数组
        answerJSON = {
            "question_id": question_id + (i - 1),
            "answers": answersList
        }
        print(json.dumps(answerJSON))
        emList.append(answerJSON)
    print(json.dumps(emList))
