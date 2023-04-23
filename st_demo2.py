import streamlit as st
x = st.slider('b')  # 👈 this is a widget
st.write(x, 'squared is', x * x)