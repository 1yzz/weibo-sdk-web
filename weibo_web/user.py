import re


def get_username(session, uuid):
    web_weibo_url = "http://weibo.com/%s/profile?topnav=1&wvr=6&is_all=1" % uuid
    weibo_page = session.get(web_weibo_url)

    return re.findall(r"nick\']='([^']+)\';", weibo_page.text)[0]

