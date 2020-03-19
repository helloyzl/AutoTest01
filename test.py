import redis
import requests
from requests.cookies import RequestsCookieJar
from requests.utils import dict_from_cookiejar


redis_host = 'r-uf63qvrxbx4ep1h8ukpd.redis.rds.aliyuncs.com'
redis_port = '6379'
redis_password = 'YdBx0EUq8XAHFAf9I4VjFw'
redis_db = 9

# 获取图片token
def fun1():
    global token
    r = requests.get('http://system.test.cef0e73c879624990a12fcf7c3cd3ea9d.cn-shanghai.alicontainer.com/system/auth/codeMaker').json()
    token = r.get('result').get('token')
    print(r.get('result').get('token'))
    return token


# 获取token对应的图片数字
def test_2_get_redis_num(value):
    global token_num
    pool = redis.ConnectionPool(host=redis_host,port=redis_port,password=redis_password,db=redis_db)
    r = redis.Redis(connection_pool=pool)
    # 传入图片token,eval()转换
    token_num = eval(r.get(value))
    print('对应图片token的数字为：',token_num)
    print(type(token_num))
    return token_num


def test_3_getcookie():
    url = 'http://system.test.cef0e73c879624990a12fcf7c3cd3ea9d.cn-shanghai.alicontainer.com/system/auth/codeImgLogin'
    params = {
        "codeImg": token_num,
        "password": "123456",
        "token": token,
        "username": "yuzhoulin"
    }
    cookiejar = requests.post(url,json=params).cookies
    print(cookiejar)
    print(type(cookiejar))
    # 通过RequestsCookieJar直接获取
    r = dict_from_cookiejar(cookiejar)
    print(r,type(r))
    r2 = RequestsCookieJar().keys()
    r3 = RequestsCookieJar().values()
    print(r3)
    json = requests.post(url,json=params).json()
    print(json.get('result').get('token'))



if __name__ == '__main__':
    t = fun1()
    test_2_get_redis_num(t)
    test_3_getcookie()