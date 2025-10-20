import streamlit as st

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import pathlib
from io import BytesIO


def run_eda():
    data_path = pathlib.Path(__file__).parent / 'data' / 'Car_Purchasing_Data.csv'
    df = pd.read_csv(data_path)

    st.markdown("<div class='card'><strong>데이터셋</strong> — Car_Purchasing_Data.csv</div>", unsafe_allow_html=True)

    radio_menu = ['데이터프레임', '기본통계']
    radio_choice = st.radio('선택하세요', radio_menu, horizontal=True)

    if radio_choice == radio_menu[0]:
        st.dataframe(df)
    else:
        st.dataframe(df.describe())

    st.subheader('최대 / 최소값 확인')
    min_max_menu = list(df.columns[4:])
    select_choice = st.selectbox('컬럼을 선택하세요', min_max_menu)

    st.info(f'{select_choice}는 {int(df[select_choice].min())}부터 {int(df[select_choice].max())}가 있습니다.')

    st.subheader('상관관계 분석')
    multi_menu = min_max_menu
    choice_multi_list = st.multiselect('컬럼을 2개 이상 선택하세요', multi_menu)

    if len(choice_multi_list) >= 2:
        corr = df[choice_multi_list].corr(numeric_only=True)
        st.dataframe(corr.style.background_gradient(cmap='coolwarm'))

        fig1, ax1 = plt.subplots(figsize=(6, 4))
        sb.heatmap(corr, annot=True, vmin=-1, vmax=1, cmap='coolwarm', fmt='.2f', linewidths=0.8, ax=ax1)
        st.pyplot(fig1)

    st.subheader('각 컬럼간의 Pair Plot')
    vars_for_pair = ['Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth', 'Car Purchase Amount']
    # Pairplot can be heavy; make it optional
    if st.checkbox('Pair Plot 보기 (시간이 걸릴 수 있음)'):
        with st.spinner('Pair plot 생성 중...'):
            pair = sb.pairplot(df[vars_for_pair].sample(n=min(500, len(df))), diag_kind='kde')
            buf = BytesIO()
            pair.savefig(buf, dpi=120, bbox_inches='tight')
            buf.seek(0)
            st.image(buf)
            plt.close('all')
