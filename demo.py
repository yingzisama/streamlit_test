# coding:gbk
import streamlit as st


# ������ҳ����
st.title('Elelive_TestTools')

# չʾ��������
st.subheader('����2-ģ���û�����')

option = st.selectbox(
     'ѡ�񿪲�����',
     ('XM', 'SG', 'TW','VN','ID'))

txt = st.text_area('������uid�����ŷָ�', value="������")

if st.button('ȷ��'):
    pass

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