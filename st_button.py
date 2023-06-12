# 导入streamlit
import streamlit as st
# 显示标题
st.header('按钮')

# if/esle模块实现按钮显示及点击功能
if st.button('say hello~'):
    st.write('hello clicked')
else:
    st.write('goodbye')
