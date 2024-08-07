import streamlit as st
from PIL import Image

st.title('myfirstapp')
st.caption('streamlitの仕様理解のためのテストアプリ')
# streamlit run app.py　で自動的にwebブラウザが開く
# http://localhostのwebサイトは自分のPC内でwebアプリが起動している状態

# 2.画像 (pip install pillowで画像を使用できるようにする)
image = Image.open('./data/image_molecule.png')
st.image(image, width = 400)