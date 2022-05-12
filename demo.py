# coding:gbk
import streamlit as st
import requests
import json
import re
import time

st.set_page_config(
    page_title = "ele测试工具",    #页面标题
    page_icon = "random",        #icon
    layout = "centered",                #页面布局
    initial_sidebar_state = "auto",  #侧边栏
)


def start_studio(Test_uid,option):
    url = 'http://studio02.svc.elelive.cn/studio/startForTest'
    data = {
	"channelType": 0,
	"coverId": "",
	"title": "",
	"userId": Test_uid
    }
    header = {
        'region': option,
        'uid':Test_uid,
        'AppVersion':'4.30.0',
        'Content-Type':'application/json'
    }

    res = requests.post(url,json=data,headers=header)
    # st.text(res.text)
    userId = json.loads(res.text)['detail']['user']['userId']
    liveCode = json.loads(res.text)['detail']['liveCode']
    pushStreamUrl = json.loads(res.text)['detail']['pushStreamUrl']
    pushStreamUrl_re = re.split(r'[?,\s]\s*', pushStreamUrl)[1]
    streamId = json.loads(res.text)['detail']['streamId']
    st.text(userId+'开播成功')
    return userId,liveCode,pushStreamUrl_re,streamId

def onCallbackUsing(userId,liveCode,pushStreamUrl_re,streamId):
    url = 'http://studio02.svc.elelive.cn/multi/studio/callback'
    data = {
            "eventType":1,
            "sign":"98a7d2dadf3475d33264bc9acee2ea4a",
            "t":1652083093,
            "appId":34772,
            "userId":userId,
            "extraString":liveCode,
            "streamId":streamId,
            "streamParam":pushStreamUrl_re,
            "channelType":0,
            "sequence":"835091404392722190",
            "eventTime":1652082493000
            }
    header = {
        'Content-Type':'application/json'
    }
    res = requests.post(url,json=data,headers = header)

def ackUsing(liveCode,uid):
    url = 'http://studio02.svc.elelive.cn/studio/ack'
    data = {
        'liveCode':liveCode,
    }
    header = {
        'uid':uid,
        'Content-Type':'application/x-www-form-urlencoded'
    }
    res = requests.post(url,data=data,headers=header)

def main(list_uid):
    liveCode_list = []
    for j in range(len(list_uid)):
        test_uid = list_uid[j]
        userId,liveCode,pushStreamUrl_re,streamId = start_studio(test_uid,option)
        onCallbackUsing(userId,liveCode,pushStreamUrl_re,streamId)
        liveCode_list.append(liveCode)
    for i in range(9999):
        time.sleep(30)
        for k in range(len(list_uid)):
            try:
                test_uid2 = list_uid[k]
                liveCode2 = liveCode_list[k]
                ackUsing(liveCode2,test_uid2)
            except:
                print('连接失败')


# 设置网页标题
st.title('Elelive_TestTools')

# 展示二级标题
st.subheader('测试2-模拟用户开播')

option = st.selectbox(
     '选择开播地区',
     ('XM', 'SG', 'TW','VN','ID'))

txt = st.text_area('请输入uid，逗号分隔', value="请输入")

if st.button('确定'):
    list_uid = txt.split(",")
    main(list_uid)

st.write('———————————————————————————————————————————————————————')

# 展示二级标题
st.subheader('测试环境账号充值')

option2 = st.selectbox(
     '选择测试环境',
     ('测试环境1', '测试环境2', '测试环境3'))

text_money = st.text_input('输入小象币金额', '请输入')
if st.button('充值'):
    st.write('充值成功')

#streamlit run demo.py