import random  # 随机


def gen_option_str(id):
    """生成单个提交"""
    ctx = str.format('finish_%s=%s' % (id, gen_random_option()))
    return ctx


def gen_req_ctx(start_id, course_id, start_time, em):
    """生成做题请求data值"""
    ctx = gen_option_str(start_id)
    for i in range(1, 10):
        ctx = ctx + '&' + gen_option_str(start_id + i)
    ctx = ctx + '&courseId=' + str(course_id) + '&startTime=' + str(start_time) + '&em=' + em
    return ctx


def gen_random_option():
    """生成随机答案"""
    option = ['A', 'B', 'C', 'D']
    return option[random.randint(0, 3)]
