import time


def post_text(session, text):
    unix = int(time.time() * 1e3)
    url = "https://weibo.com/aj/mblog/add?ajwvr=6&__rnd=%s" % unix

    payload = {
        'location': 'v6_content_home',
        'text': text,
        'appkey': '',
        'style_type': 1,
        'pic_id': '',
        'tid': '',
        'pdetail': '',
        'mid': '',
        'isReEdit': False,
        'gif_ids': '',
        'rank': 0,
        'rankid': '',
        'module': 'stissue',
        'pub_source': 'main_',
        'pub_type': 'dialog',
        'isPri': 0,
        '_t': 0
    }

    r = session.post(url, data=payload)
    r.raise_for_status()
    return r.json()
