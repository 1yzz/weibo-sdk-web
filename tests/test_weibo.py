import pytest
import tests
from time import time
from weibo_web import Weibo

wb = Weibo(tests.username, tests.password)

#
# def test_get_username():
#     assert wb.get_username() == '瞎眼看海贼'
#
#
# def test_post_text():
#     res = wb.post_text('发布的微博lai[悲伤]%s' % int(time() * 1e3))
#
#     assert res['msg'] == ''
#
#
# def test_upload_pic():
#     url = 'https://wx4.sinaimg.cn/orj360/804a43cegy1g7zyxbqimuj21970u0n1a.jpg'
#     pid = wb.upload_pic(url)
#     assert pid != ''


def test_post_text_with_img():
    res = wb.post_text_with_img('发布的图片 %d' % int(time() * 1e3), [
        'https://wx4.sinaimg.cn/orj360/804a43cegy1g7zyxbqimuj21970u0n1a.jpg',
        'https://wx4.sinaimg.cn/orj360/804a43cegy1g7zyxbqimuj21970u0n1a.jpg',
        'https://wx4.sinaimg.cn/orj360/804a43cegy1g7zyxbqimuj21970u0n1a.jpg',
    ])

    assert res['msg'] == ''

