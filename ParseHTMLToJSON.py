import json

from bs4 import BeautifulSoup
import glob
import re

files_path = 'C:\\Users\\Adam\\Documents\\AutoWanXue\\AnswerPagesHTML\\*'

# def


if __name__ == '__main__':
    file_name_list = glob.glob(files_path)  # 读取该目录下所有文件
    print(file_name_list)  # 输出文件夹下所有文件
    em_list = []  # 创建存放所有页面答案的list
    for file_name in file_name_list:
        em_id = re.sub(r'\D', '', file_name)  # 正则过滤掉非数字得出em_id
        print(em_id)
        soup = BeautifulSoup(open(file_name_list[0], encoding='utf-8'), "html.parser")
        tags = soup.select('span[class="c4"]')  # 提取当页内所有答案tag
        answer_list = []
        for tag in tags:
            subject_id_str = tag.parent.parent.parent['id']  # 取父节点的题号str
            subject_answer_str = tag.string  # 获取单条答案tag内容str
            subject_id = int(re.sub(r'\D', '', subject_id_str))  # 正则提取str中数字部分
            subject_answer = re.sub(r'[^A-D]', '', subject_answer_str)  # 正则去除答案str中非英文字符部分
            subject_answer_list = list(subject_answer)
            print(str(subject_id) + '  ' + subject_answer)
            answer = {
                'subject_id': subject_id,
                'answer_list': subject_answer_list  # Todo,解析答案str成数组放这里
            }
            print(answer)
            answer_list.append(answer)
        answers = {
            'em_id': em_id,
            "answers": answer_list
        }
        print(answers)
        em_list.append(answers)
    answers_JSON_text = json.dumps(em_list)
    f = open('.\\answer.json', 'w+')
    f.write(answers_JSON_text)
    f.close()
