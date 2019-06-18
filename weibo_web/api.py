import requests
from .login import login
from .user import get_username


class Weibo:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.session()
        self.uuid = 0

    def _retry(func):
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except:
                self.login()
                return func(self, *args, **kwargs)
        return wrapper

    def login(self):
        self.uuid, self.session = login(self.username, self.password)

    @_retry
    def get_username(self):
        return get_username(self.session, self.uuid)

    def post_text(self):
        pass

    def post_with_img(self):
        pass

    def repost(self):
        pass

    def comment(self):
        pass


