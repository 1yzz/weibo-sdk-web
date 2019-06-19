import pytest
import tests
from weibo_web import Weibo

wb = Weibo(tests.username, tests.password)
wb.login()


def test_get_username():
    assert wb.get_username() == '瞎眼看海贼'


def test_post_text():
    res = wb.post_text('发布的微博lai[悲伤]')

    assert res['msg'] == ''
