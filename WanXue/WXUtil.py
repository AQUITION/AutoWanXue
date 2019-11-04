import random  # 随机


def gen_option_str(id):
    """生成单个提交，仅兼容单选弃用"""
    ctx = str.format('finish_%s=%s' % (id, gen_random_option()))
    return ctx


def gen_multi_option_str(answer):
    """兼容多选的提交生成"""
    subject_id = answer['subject_id']
    ctx = ''
    for one_option in answer['answer_list']:
        if ctx != '':
            ctx = ctx + '&'
        ctx = ctx + str.format('finish_%s=%s' % (subject_id, one_option))
    # print(ctx)
    return ctx


def gen_random_req_ctx(start_id, course_id, start_time, em):
    """生成随机做题请求data值"""
    ctx = gen_option_str(start_id)
    for i in range(1, 10):
        ctx = ctx + '&' + gen_option_str(start_id + i)
    ctx = ctx + '&courseId=' + str(course_id) + '&startTime=' + str(start_time) + '&em=' + em
    return ctx


def gen_req_ctx(answers, course_id, start_time, em):
    """生成做题请求data值"""
    ctx = ''
    for answer in answers['answers']:
        if ctx != '':
            ctx = ctx + '&'
        ctx = ctx + gen_multi_option_str(answer)
    ctx = ctx + '&courseId=' + str(course_id) + '&startTime=' + str(start_time) + '&em=' + str(em)
    return ctx


def gen_random_option():
    """生成随机答案"""
    option = ['A', 'B', 'C', 'D']
    return option[random.randint(0, 3)]
