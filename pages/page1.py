import streamlit as st

# 1.テキスト
st.subheader('自己紹介')
st.text('テスト１')
code = '''
import streamlit as st
st.title('myfirstapp')
'''
st.code(code, language='python')