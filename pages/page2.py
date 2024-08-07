import streamlit as st
import datetime

with st.form(key = 'profile_form'): # 引数keyにこのフォームの名前を任意で設定
    # 3.テキストボックス
    name = st.text_input('名前') # 戻り値nameにテキストボックス内の文字が入る
    address = st.text_input('住所')

    # 6.セレクトボックス
    age_category = st.selectbox( # セレクトボックス
        '年齢',
        ('', '18歳未満', '18歳以上')
    )
    age_category = st.radio( #ラジオボタン
        '年齢',
        ('18歳未満', '18歳以上')
    )
    
    # 7.複数選択
    hobby = st.multiselect(
        '趣味',
        ('スポーツ', '読書', 'プログラミング', 'アニメ・映画', '釣り', '料理' )
    )
    
    # 8.チェックボックス
    mail_subscribe = st.checkbox('メールマガジンを購読する')
    
    # 9.スライダー
    height = st.slider('身長', min_value=110, max_value=200)
    
    # 10.日付
    start_date = st.date_input(
        '開始日',
        datetime.date(2022, 7, 2)
    )
    
    # 11.カラーピッカー
    color = st.color_picker('テーマカラー', '#0000F0')
    
    # 4.ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    # submit_btn = st.button('送信') # 戻り値はy/n(ボタンが押されたかどうか)
    # cancel_btn = st.button('キャンセル')
    # 戻り値をPython側で表示
        # print(f'submit_btn: {submit_btn}')
        # print(f'cancel_btn: {cancel_btn}')
    
    if submit_btn:
        st.text(f'ようこそ！{name}さん!{address}に書籍をお送りしました！')
        st.text(f'年齢層：{age_category}')
        st.text(f'趣味：{", ".join(hobby)}')