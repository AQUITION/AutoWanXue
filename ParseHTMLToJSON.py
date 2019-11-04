import json

from bs4 import BeautifulSoup
import glob
import re

files_path = '.\\AnswerPagesHTML\\*'

# def


if __name__ == '__main__':
    file_name_list = glob.glob(files_path)  # 读取该目录下所有文件
    print(file_name_list)  # 输出文件夹下所有文件
    em_list = []  # 创建存放所有页面答案的list

    """按页遍历"""
    for file_name in file_name_list:
        em_id = re.sub(r'\D', '', file_name)  # 正则过滤掉非数字得出em_id
        soup = BeautifulSoup(open(file_name, encoding='utf-8'), "html.parser")  # 创建解析器对象
        tags = soup.select('span[class="c4"]')  # 提取当页内所有答案tag
        answer_list = []

        """按tag遍历所有题"""
        for tag in tags:
            subject_id_str = tag.parent.parent.parent['id']  # 取父节点，以获取题号str
            subject_answer_str = tag.string  # 获取单条答案tag内容str

            subject_id = int(re.sub(r'\D', '', subject_id_str))  # 正则提取str中数字部分
            subject_answer = re.sub(r'[^A-D]', '', subject_answer_str)  # 正则去除答案str中非英文字符部分

            subject_answer_list = list(subject_answer)  # 将连续的答案拆成list

            print(str(subject_id) + '  ' + subject_answer)  # 显示题号以及答案
            answer = {
                'subject_id': subject_id,  # 题号
                'answer_list': subject_answer_list  # 答案list
            }
            print(answer)  # 显示字典
            answer_list.append(answer)  # 单条答案存入list

        answers = {
            'em_id': em_id,
            "answers": answer_list
        }
        print(answers)  # 显示当页答案字典
        em_list.append(answers)  # 当前页存入list

    answers_JSON_text = json.dumps(em_list)  # 格式化成json
    f = open('.\\answer.json', 'w+')  # 打开文件
    f.write(answers_JSON_text)  # 写入文件
    f.close()  # 关闭文件
    print('Finished!')
