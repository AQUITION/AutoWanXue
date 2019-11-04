import random
import time
import WanXue.WXAPI as WXAPI
import WanXue.WXUtil as WXUtil

first_choice_id = 20637
COURSE_ID = 1012
time_stamp = 1572757350812

if __name__ == '__main__':
    em_ids = []
    em_ids.extend(list(range(6977, 6979)))  # 第一单元课程
    em_ids.extend(list(range(6981, 7001)))  # 第二单元课程
    em_ids.extend(list(range(7002, 7016)))  # 第三单元课程
    em_ids.extend(list(range(7017, 7019)))  # 第四单元课程
    em_ids.extend(list(range(7020, 7024)))  # 第五单元课程

    print(em_ids)

    cookie = WXAPI.fileGetCookie()

    for em_id in em_ids:
        ReqCtx = WXUtil.gen_random_option(first_choice_id, COURSE_ID, time_stamp + random.randint(1, 10) * 1000,
                                          '2_' + str(em_id))  # 生成请求完成课程的请求参数
        print(ReqCtx)  # 显示请求参数
        print(WXAPI.doCourse(ReqCtx, time_stamp, COURSE_ID, '2_' + str(em_id), cookie))  # 请求完成课程并显示Resp
        first_choice_id = first_choice_id + 10  # 题号自增10
        time.sleep(1)
