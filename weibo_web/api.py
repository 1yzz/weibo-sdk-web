import requests
from .login import login
from .user import get_username
from .post import post_text


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

    def post_with_img(self):
        pass

    def repost(self):
        pass

    def comment(self):
        pass
