import pytest
import tests
from weibo_web.user import get_username
from weibo_web.login import login


def test_get_username():
    uuid, session = login(tests.username, tests.password)
    username = get_username(session, uuid)
    assert username == '瞎眼看海贼'
