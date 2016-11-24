import requests


def getVCode():
    params = {}
    params['mobileNum'] = '18026995241'
    r = requests.post('http://192.168.0.147:8081/com.fsbest.edu.app.web/app/common/getVcode', json=params)
    print(r.text)


def checkVCode():
    params = {}
    params['mobileNum'] = '18026995241'
    params['vcode'] = '2074'
    r = requests.post('http://192.168.0.202:8081/com.fsbest.edu.app.web/app/common/validVcode', json=params)
    print(r.text)


def regist():
    params = {}
    params['mobileNum'] = '18320863170'
    params['password'] = '654321'
    params['smsCode'] = '8071'
    r = requests.post('http://192.168.0.147:8081/com.fsbest.edu.app.web/app/teacher/register', json=params)
    print(r.text)


def forgetpwd():
    params = {}
    params['mobileNum'] = '18320963170'
    params['password'] = '654321'
    params['smsCode'] = '8071'
    r =requests.post('http://192.168.0.147:8081/com.fsbest.edu.app.web/app/teacher/forgetPwd', json=params)
    print(r.text)

def home():
    params = {}
    params['mobileNum'] = '18026995241'
    params['password'] = '123456'
    params['smsCode'] = '1814'
    r =requests.post('http://192.168.0.147:8081/com.fsbest.edu.app.web/app/teacher/forgetPwd', json=params)
    print(r.text)

#getVCode()
#checkVCode()
#regist()
#forgetpwd()