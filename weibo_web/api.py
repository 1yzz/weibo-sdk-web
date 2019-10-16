import requests
import base64
from .login import login
from .user import get_username
from .post import post_text, post_text_with_img, upload_pic


def _retry(max_retry=100):
    def fn(func):
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except:
                self.login()
                return func(self, *args, **kwargs)

        return wrapper

    return fn


class Weibo:
    def __init__(self, username, password):
        if not username or not password:
            raise Exception('用户名密码不能为空')

        self.username = username
        self.password = password
        self.session = requests.session()
        self.uuid = 0

    def login(self):
        self.uuid, self.session = login(self.username, self.password)
        self.session.headers.update({
            'Referer': 'https://weibo.com/u/%s/home?topnav=1&wvr=6' % self.uuid,
            'Origin': 'https://weibo.com'
        })

    @_retry()
    def get_username(self):
        return get_username(self.session, self.uuid)

    @_retry()
    def post_text(self, text):
        return post_text(self.session, text)

    @_retry()
    def post_text_with_img(self, text, imgs):
        if imgs is not None and len(imgs) > 0:
            pic_ids = []
            for img in imgs:
                pic_ids.append(self.upload_pic(img))

            return post_text_with_img(self.session, text, '|'.join(pic_ids))
        else:
            return post_text(self.session, text)

    @_retry()
    def post_text_with_b64img(self, text, imgs):
        if imgs is not None and len(imgs) > 0:
            pic_ids = []
            for b64img in imgs:
                pic_ids.append(upload_pic(self.session, b64img))

            return post_text_with_img(self.session, text, '|'.join(pic_ids))
        else:
            return post_text(self.session, text)

    @_retry()
    def upload_pic(self, url):
        b64 = base64.b64encode(requests.get(url).content)
        return upload_pic(self.session, b64)

    def repost(self):
        pass

    def comment(self):
        pass
