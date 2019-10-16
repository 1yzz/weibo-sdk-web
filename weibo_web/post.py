import time
import re


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


def post_text_with_img(session, text, pic_id):
    unix = int(time.time() * 1e3)
    url = "https://weibo.com/aj/mblog/add?ajwvr=6&__rnd=%d" % unix

    payload = {
        'location': 'v6_content_home',
        'text': text,
        'appkey': '',
        'style_type': 1,
        'pic_id': pic_id,
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


def upload_pic(session, base64_data):
    url = 'https://picupload.weibo.com/interface/pic_upload.php'
    params = {
        'cb': 'https://weibo.com/aj/static/upimgback.html?_wv=5&callback=STK_ijax_%d' % int(time.time() * 1e3),
        'mime': 'image/jpeg',
        'data': 'base64',
        'url': "",
        'markpos': 1,
        'logo': '',
        'nick': '',
        'marks': 0,
        'app': 'miniblog',
        's': 'rdxt',
        'pri': '',
        'file_source': 1,
    }
    payload = {
        'b64_data': base64_data,
    }
    r = session.post(url, params=params, data=payload, allow_redirects=False)
    # Location: https://weibo.com/aj/static/upimgback.html?_wv=5&callback=STK_ijax_156108350363335&ret=1&pid=804a43cegy1g48k8hemi7j20ig0ag0sv
    location = r.headers.get('location')
    if location is None:
        raise Exception('无法获得pid')
    return re.findall(r'pid=(.*?)$', r.headers.get('location'))[0]
