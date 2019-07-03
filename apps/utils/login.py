"""存放与用户相关的utils"""
import requests

# weibo接口页面 https://open.weibo.com/wiki/%E6%8E%88%E6%9D%83%E6%9C%BA%E5%88%B6


def get_accesstoken():
    accesstoken_url = "https://api.weibo.com/oauth2/access_token"

    re_dict = requests.post(accesstoken_url, data={
        "client_id": 1738730794,
        "client_secret": '',
        "grant_type": "authorization_code",
        "code": '',
        "redirect_uri": "http://192.168.206.134:8007/complete/weibo/"
    })
    # 得到b'{"access_token":"2.00JWNOgGE_XftB6f1f0226030WdQzu","remind_in":"157679999","expires_in":157679999,"uid":"6120791661","isRealName":"true"}'
    print(re_dict)


def get_msg():
    accesstoken_url = "https://api.weibo.com/2/users/show.json?access_token=2.00JWNOgGE_XftB6f1f0226030WdQzu&uid=6120791661"
    print(accesstoken_url)


if __name__ == '__main__':
    # get_accesstoken()
    get_msg()
