import time
import WanXue.WXAPI as WXAPI

FILE_PATH = '.\\AnswerPages\\'  # 爬取文件存储路径

COURSE_ID = 1012

if __name__ == '__main__':
    em_ids = []
    em_ids.extend(list(range(6977, 6979)))  # 第一单元课程
    em_ids.extend(list(range(6981, 7001)))  # 第二单元课程
    em_ids.extend(list(range(7002, 7016)))  # 第三单元课程
    em_ids.extend(list(range(7017, 7019)))  # 第四单元课程
    em_ids.extend(list(range(7020, 7024)))  # 第五单元课程

    print(em_ids)  # 显示所有课程id

    cookie = WXAPI.fileGetCookie()  # 读取文件cookie

    for em_id in em_ids:
        print('2_' + str(em_id) + ' ' + str(COURSE_ID) + ' ' + cookie)  # 显示请求参数，调试
        time.sleep(0.5)
        ReqCtx = WXAPI.getAnswer('2_' + str(em_id), COURSE_ID, cookie)  # 请求答案页面
        f = open(FILE_PATH + str(em_id) + '.html', 'w+', encoding='utf-8')
        f.write(ReqCtx)  # 写入文件
        f.close()

    print("Finished")
