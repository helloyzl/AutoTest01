from selenium import webdriver
import requests, time


def get_target_url():
    # 可以先使用接口登陆获得登陆cookie，后使用cookie跳过页面登陆
    # 页面登陆地址
    url = 'http://system.client.wetrade.ccccb79fa2d0f4c1f84490521291c6de4.cn-shanghai.alicontainer.com/#/login'
    driver = webdriver.Chrome()
    # 直接使用登录后的cookie
    driver.get(url)
    # 也可以在浏览器中查看cookie参数
    cookies = {'name':'Admin-Token',
               'value':'eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMjIzIiwiY29kZSI6IjEyMjMiLCJuYW1lIjoi5rWL6K-V6Jme5ZGo5p6XIiwidGltZSI6MTU4NDI3OTgwMTU1MSwiZXhwIjoxNTg2ODcxODAxfQ.TGgd9bJYrDIQjzMvpu-OJcvfd7AVBKCZ1g9OkVT2d71NLBXjQEa-oX0RmE6CDaJaTJTvlZTQCatNPlE0tvm7AOSN0DtEshYHJJdg80m8270Z5ErO4PfKGv3_6DgNn6ztlNXwSBHBHvPstzP0A-f02rAOEVw26Ec3TXaq2BaO5HE'}
    # driver.add_cookie(cookies)
    driver.add_cookie(cookie_dict=cookies)
    # driver.refresh()
    driver.get(url)
    print(driver.get_cookie('Admin-Token'))
    print(driver.title)
    driver.refresh()
    # 窗口最大化
    driver.maximize_window()
    # 刷新后 无法定位需要强制等待
    time.sleep(2)
    # print(driver.find_element_by_xpath('/html/body/div/div/ul/div/li[4]/div/span').click())  # 获取元素内内容
    driver.find_element_by_xpath('/html/body/div/div/ul/div/li[4]/div/span').click()  # 点击商品管理
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/ul/div/li[4]/ul/a/li/span').click()  # 点击商品列表
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="app"]/div/div/section/div/div[2]/div[1]/button[1]/span').click()  # 点击新增商品
    driver.find_element_by_xpath('//*[@id="app"]/div/div/section/div/div[3]/div[1]/div/div[2]/div/div[1]/form/div[1]/div/div/input').send_keys('自动化UI测试输入商品1')  # 新增商品 输入名称
    driver.find_element_by_xpath('//*[@id="app"]/div/div/section/div/div[3]/div[1]/div/div[2]/div/div[1]/form/div[3]/div/div/div[2]/input').click()  # 新增商品 选择项目\
    # # 获取元素的文本
    x1 = driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div/div[3]/div[1]/div/div[2]/div/div[1]/form/div[3]/div/div/div[2]/input').get_attribute('placeholder')
    print(x1)

    # 点击选择项目
    driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()  # 新增商品 选择第一个项目
    # 点击旁边空白区域
    driver.find_element_by_xpath('//*[@id="app"]/div/div/section/div/div[3]/div[1]/div/div[2]/div/div[1]/form/div[3]/div').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div/section/div/div[3]/div[1]/div/div[2]/div/div[1]/form/div[4]/div/div/input').send_keys('自动化UI测试输入商品品牌')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/section/div/div[3]/div[1]/div/div[2]/div/div[1]/form/div[5]/div/div/input').send_keys('自动化执行单位')
    # 选择保质期一栏
    driver.find_element_by_xpath('//*[@id="app"]/div/div/section/div/div[3]/div[1]/div/div[2]/div/div[1]/form/div[7]/div/div[2]/div/input').click()

    # 控制滚动条下拉 id为滚动条的id
    # js = "var q=document.getElementById('id').scrollTop=10000"
    # driver.execute_script(js)

    # 将滚动条拖动到需要显示的元素位置
    target = driver.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[3]/div[1]/div/div[2]/div/div[1]/form/div[8]/div/div/div/i")
    driver.execute_script("arguments[0].scrollIntoView();", target)
    # 点击保质期单位"年"
    driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[3]').click()
    # 不添加进项税/销项税的商品保存
    driver.find_element_by_xpath('//*[@id="app"]/div/div/section/div/div[3]/div[1]/div/div[3]/div/button[1]/span').click()
    # 确认创建商品，二次保存
    driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/button[2]/span')
    print('创建商品商品成功')
    time.sleep(5)




def get_img():
    img_url = 'http://system.test.cef0e73c879624990a12fcf7c3cd3ea9d.cn-shanghai.alicontainer.com/system/auth/codeMaker'
    results = requests.get(img_url).json()
    print(results)

if __name__ == '__main__':
    get_target_url()
    # get_img()




