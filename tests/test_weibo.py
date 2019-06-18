import pytest
import tests
from weibo_web import Weibo

wb = Weibo(tests.username, tests.password)
wb.login()


def test_get_username():
    assert wb.get_username() == '瞎眼看海贼'


def test_new_post():
    assert True
