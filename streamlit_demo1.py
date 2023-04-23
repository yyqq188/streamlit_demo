import streamlit as st
import requests

def send2back(data_json):
    return requests.post("http://xxx:xx/ss",json=data_json).json()


st.title("自然语言处理2")
st.markdown("---")
option = st.selectbox("请选择你想要的功能:",('', '中文分词', '英文分词', '中文命名实体识别', '中文依存句法分析'))
content = st.text_input("请输入待分析的内容")
# if option == '中文分词':
#     if st.button("中文分词") & (content != ''):
#         data_bin = {'model_name': 'tok_zh', 'input': [content]}
#         rlt = requests.post('http://111.229.217.153:80/tok_zh', json=data_bin).json()
#         st.text(rlt['rlt'][0])
# elif option == '英文分词':
#     if st.button("英文分词") & (content != ''):
#         data_bin = {'model_name': 'tok_en', 'input': [content]}
#         rlt = requests.post('http://111.229.217.153:80/tok_en', json=data_bin).json()
#         st.text(rlt['rlt'][0])
# elif option == '中文命名实体识别':
#     if st.button("命名实体识别") & (content != ''):
#         data_bin = {'model_name': 'ner', 'input': [list(content)]}
#         rlt = requests.post('http://111.229.217.153:80/ner', json=data_bin).json()
#         st.write(rlt)
# elif option == '中文依存句法分析':
#     if st.button("依存句法分析") & (content != ''):
#         data_bin = {'model_name': 'parser', 'input': [content]}
#         rlt = requests.post('http://111.229.217.153:80/parser', json=data_bin).json()
#         st.write(rlt)
# else:
#     pass

