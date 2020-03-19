from selenium import webdriver
import unittest
import requests
import redis
import HtmlTestRunner


class MyTest1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.homepage_url = 'http://client-system.test.cef0e73c879624990a12fcf7c3cd3ea9d.cn-shanghai.alicontainer.com'
        cls.login_url = 'http://system.test.cef0e73c879624990a12fcf7c3cd3ea9d.cn-shanghai.alicontainer.com/system/auth/codeImgLogin'
        cls.img_url = 'http://system.test.cef0e73c879624990a12fcf7c3cd3ea9d.cn-shanghai.alicontainer.com/system/auth/codeMaker'
        cls.redis_host = 'r-uf63qvrxbx4ep1h8ukpd.redis.rds.aliyuncs.com'
        cls.redis_port = '6379'
        cls.redis_password = 'YdBx0EUq8XAHFAf9I4VjFw'
        cls.redis_db = 9
        print('执行开始')


    # 获取验证码token
    def test_1_imgtoken(self):
        # 用例定义全局变量
        global img_token
        response = requests.get(self.img_url).json()
        img_token = response.get('result').get('token')
        print('请求验证码为：', img_token)
        print('Requests获取验证码接口成功')
        return img_token

    # 获取验证码token对应数字
    def test_2_getredisnum(self):
        global token_num
        pool = redis.ConnectionPool(host=self.redis_host,port=self.redis_port,password=self.redis_password,db=self.redis_db)
        resutl = redis.Redis(connection_pool=pool)
        # 传入图片token
        token_num = eval(resutl.get(img_token))
        print('对应图片token的数字为：',token_num)
        print('获取Redis中对应验证码数据成功')
        return token_num


    #
    def test_3_getcookie(self):
        global cookie_value,cookie_name
        self.params = {
            "codeImg": token_num,
            "password": "123456",
            "token": img_token,
            "username": "yuzhoulin"
        }
        # 请求方式为post
        response = requests.post(self.login_url,json=self.params).json()
        cookie_value = response.get('result').get('token')
        cookie_name = 'MAN-Admin-Token'
        print('cookie_value的值是：',cookie_value)
        print('使用前两个接口的值，接口登录成功')
        return cookie_name, cookie_value


    def test_4_login(self):
        self.driver.get(self.homepage_url)
        # 添加cookie
        self.driver.add_cookie({'name' : cookie_name, 'value' : cookie_value})
        self.driver.refresh()
        # UI自动化执行后，刷新浏览器，打印当前界面主题
        print(self.driver.title)


    @classmethod
    def tearDownClass(cls):
        print('执行结束')


if __name__ == '__main__':
    unittest.main()





