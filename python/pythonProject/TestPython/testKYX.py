import requests
import json

host = 'http://120.25.239.118:8080/com.fsbest.edu.app.web'
proxy = '192.168.0.142:8888'
token = "1_72a997617cb341748f48ecba9d6e748c"
teacherToken = '2_a1796af759904af1897de34c45b64b9b'
def login():
    path = '/app/student/login'
    url = host + path
    session = requests.Session()
    session.trust_env = False
    r = session.post(url, json={'userName':'Liuqi7', 'password':'123456'})
    print(r.text)
    j = json.loads(r.text)
    if j['code'] == 0:
        token = j['data']['token']
        print(token)



def addHomeWork():
    path = '/app/student/addHomework'
    url = host + path
    session = requests.Session()
    session.trust_env = False
    r = session.post(url, json={ "imageUrl":"http://www.wndhw.com/koujue/wuli/images/wuli2.jpg", "description":"ask3", "awardNum":16, "subjectId":"25", "type":1},
                     headers={'token':token},
                     proxies={'http':proxy})
    print(r.text)

def getStudentHomeWork():
    path = '/app/student/getHomework'
    url = host + path
    session = requests.Session()
    session.trust_env = False
    r = session.post(url, json={'gradeId':'', 'classId':'', 'subjectId':'', 'page':'1'},
                     headers={'token': token},
                     proxies={'http': proxy})
    print(r.text)

def getTeacherHomeWork():
    path = '/app/teacher/getHomework'
    url = host + path
    session = requests.Session()
    session.trust_env = False
    r = session.post(url, json={'gradeId': '', 'classId': '', 'subjectId': '', 'page': '1'},
                     headers={'token': teacherToken},
                     proxies={'http': proxy})
    print(r.text)


def getHomeWorkRsponse(homeworkId):
    path = '/app/teacher/getHomewordResponse'
    url = host + path
    session = requests.Session()
    session.trust_env = False
    r = session.get(url, params={'homeworkId': homeworkId, 'page': '1'},
                     headers={'token': teacherToken},
                     proxies={'http': 'http://192.168.56.1:8888'})
    print(r.text)


def answerHomeWork(homeworkId):
    path = '/app/teacher/answerHomework'
    url = host + path
    session = requests.Session()
    session.trust_env = False
    r = session.post(url, json={"imageUrl":"http://img1.imgtn.bdimg.com/it/u=943185022,3561258397&fm=21&gp=0.jpg,http://pic10.nipic.com/20101103/5063545_000227976000_2.jpg", "content":"abcdefg", 'homeworkId': homeworkId},
                     headers={'token': teacherToken},
                     proxies={'http': proxy})
    print(r.text)


def getSchoolInfo():
    path = '/app/teacher/getUniqueSchool'
    url = host + path
    session = requests.Session()
    session.trust_env = False
    r = session.post(url,
                     headers={'token': teacherToken},
                     proxies={'http': proxy})
    print(r.text)

def getClassInfo():
    path = '/app/common/getClassList'
    url = host + path
    session = requests.Session()
    session.trust_env = False
    r = session.post(url, json={"schoolId":'f14ccaf8542747c8aa2f906d350f55dc', "gradeId":18},
                     headers={'token': teacherToken},
                     proxies={'http': proxy})
    print(r.text)


def acceptHomeworkResponse(id):
    path = '/app/student/acceptHomeworkResponse'
    url = host + path
    session = requests.Session()
    session.trust_env = False
    r = session.post(url, params={"id": id},
                     headers={'token': token},
                     proxies={'http': proxy})
    print(r.text)


#answerHomeWork('6652af29f6b1419aa5fe66212cda284f')
#addHomeWork()
#getHomeWorkRsponse("aa60823ce30a4d449d924880936d8c76")
#getSchoolInfo()
#getClassInfo()
acceptHomeworkResponse('e1efeea5687045ef9951d16c4c3f4c5f')