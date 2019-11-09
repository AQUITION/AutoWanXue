import unittest

from WanXue.WXUtil import gen_multi_option_str
from WanXue.WXUtil import gen_req_ctx

class UtilTestCase(unittest.TestCase):
    """测试Util"""

    def test_gen_option_str(self):
        """测试请求data选择题部分"""

        # 多选题测试用例
        answer1 = {"subject_id": 20641, "answer_list": ["A", "B", "C", "D"]}
        req1_str = gen_multi_option_str(answer1)
        self.assertEqual(req1_str, 'finish_20641=A&finish_20641=B&finish_20641=C&finish_20641=D')

        # 单选题测试用例
        answer2 = {"subject_id": 20639, "answer_list": ["C"]}
        req2_str = gen_multi_option_str(answer2)
        self.assertEqual(req2_str, 'finish_20639=C')

unittest.main()
