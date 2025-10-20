import streamlit as st
# 모델 불러오기 위한 라이브러리
import joblib
import pandas as pd
import pathlib


@st.cache_data
def load_model(path: str):
    return joblib.load(path)


def run_ml():
    st.subheader('구매 금액 예측하기')

    st.info('아래 정보를 입력하면, 금액을 예측해드립니다.')

    gender_list = ['여자', '남자']
    gender = st.radio('성별을 입력하세요', gender_list, horizontal=True)

    gender_data = 0 if gender == gender_list[0] else 1

    c1, c2 = st.columns(2)
    with c1:
        age = st.number_input('나이', min_value=18, max_value=100, value=35)
        salary = st.number_input('연봉 (USD)', min_value=0, value=50000, step=1000)
    with c2:
        debt = st.number_input('카드빚 (USD)', min_value=0, value=5000, step=100)
        worth = st.number_input('자산 (USD)', min_value=0, value=20000, step=1000)

    model_path = pathlib.Path(__file__).parent / 'model' / 'regressor.pkl'

    if st.button('예측하기'):
        if not model_path.exists():
            st.error('모델 파일이 없습니다. 먼저 model/regressor.pkl 파일을 확인하세요.')
            return

        regressor = load_model(str(model_path))

        new_data = [{'Gender': gender_data, 'Age': age, 'Annual Salary': salary, 'Credit Card Debt': debt, 'Net Worth': worth}]
        df_new = pd.DataFrame(new_data)

        y_pred = regressor.predict(df_new)
        if len(y_pred) == 0 or y_pred[0] < 0:
            st.warning('구매 금액 예측이 어렵습니다.')
        else:
            price = format(round(y_pred[0]), ',')
            st.markdown("<div class='card'>"
                        f"<div style='font-size:1.1rem; font-weight:700'>예측 결과</div>"
                        f"<div style='margin-top:0.5rem; font-size:1.4rem' class='accent'>{price} USD</div>"
                        "</div>", unsafe_allow_html=True)