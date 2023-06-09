import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# 样例 1
#   st.write 基本用法就是现实文字和使用 Markdown 语法的文本
st.write('Hello, *World!* :sunglasses:')

# 样例 2
    # 输出数字
st.write(1234)

# 样例 3
    # 输出数据框
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# 样例 4
    # 多参数输出数据框
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# 样例 5
    # 输出显示图表
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

# 样例 6
    # 输出代码
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')