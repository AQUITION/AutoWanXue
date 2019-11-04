from urllib import request, parse

COMMIT_EM_URL = 'https://jluzh.wanxue.cn/sls/jwExam/addRecord'  # 提交答案URL

GET_ANSWER_URL = 'https://jluzh.wanxue.cn/sls/jwExam/examAnalysis'  # 获取答案URL

USER_AGENT_FIREFOX = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'  # User_Agent

COOKIE_PATH = '.\\cookie'  # cookie 存放目录


def doCourse(data, start_time, courseId, em, cookie):
    """完成课程作业"""
    header = {  # HTTP Header
        'User-Agent': USER_AGENT_FIREFOX,
        'Cookie': cookie
    }

    param = {  # 请求参数
        'data': data,
        'startTime': start_time,
        'courseId': courseId,
        'em': em
    }

    data = bytes(parse.urlencode(param), encoding='utf-8')  # 编码参数
    req = request.Request(url=COMMIT_EM_URL, headers=header, data=data, method='POST')  # 创建请求
    response_stream = request.urlopen(req)  # 发起请求
    response_ctx = response_stream.read().decode('utf-8')  # 读取返回流
    return response_ctx


def getAnswer(em, courseId, cookie):
    """请求答案"""
    header = {  # HTTP Header
        'User-Agent': USER_AGENT_FIREFOX,
        'Cookie': cookie
    }

    param = {  # 请求参数
        'em': em,
        'courseId': courseId
    }
    url_values = parse.urlencode(param)
    print(url_values)
    req = request.Request(url=GET_ANSWER_URL + '?' + url_values, headers=header, method='GET')  # 创建请求
    response_stream = request.urlopen(req)  # 发起请求
    response_ctx = response_stream.read().decode('utf-8')  # 读取返回流
    return response_ctx


def fileGetCookie():
    f = open(COOKIE_PATH, 'r')
    cookie_ctx = f.read()
    f.close()
    print(cookie_ctx)
    return cookie_ctx
