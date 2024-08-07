import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt

# 12.データ分析関連のウィジェット
df = pd.read_csv('./data/Temp.csv', index_col='月')
# st.dataframe(df)
# st.table(df)
st.line_chart(df)
st.bar_chart(df['2021年'], x_label="月")

# # 13.matplotlob
# fig, ax = plt.subplots()
# ax.plot(df.index, df['2021年'])
# ax.set_title('matplotlib graph')
# st.pyplot(fig)
