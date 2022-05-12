# coding:gbk
import streamlit as st


# 设置网页标题
st.title('Elelive_TestTools')

# 展示二级标题
st.subheader('测试2-模拟用户开播')

option = st.selectbox(
     '选择开播地区',
     ('XM', 'SG', 'TW','VN','ID'))

txt = st.text_area('请输入uid，逗号分隔', value="请输入")

if st.button('确定'):
    pass

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