# coding:gbk
import streamlit as st
import requests
import json
import re
import time

st.set_page_config(
    page_title = "ele���Թ���",    #ҳ�����
    page_icon = "random",        #icon
    layout = "centered",                #ҳ�沼��
    initial_sidebar_state = "auto",  #�����
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
    st.text(userId+'�����ɹ�')
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
                print('����ʧ��')


# ������ҳ����
st.title('Elelive_TestTools')

# չʾ��������
st.subheader('����2-ģ���û�����')

option = st.selectbox(
     'ѡ�񿪲�����',
     ('XM', 'SG', 'TW','VN','ID'))

txt = st.text_area('������uid�����ŷָ�', value="������")

if st.button('ȷ��'):
    list_uid = txt.split(",")
    main(list_uid)

st.write('��������������������������������������������������������������������������������������������������������������')

# չʾ��������
st.subheader('���Ի����˺ų�ֵ')

option2 = st.selectbox(
     'ѡ����Ի���',
     ('���Ի���1', '���Ի���2', '���Ի���3'))

text_money = st.text_input('����С��ҽ��', '������')
if st.button('��ֵ'):
    st.write('��ֵ�ɹ�')

#streamlit run demo.py