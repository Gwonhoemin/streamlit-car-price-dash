import streamlit as st
from app_home import run_home
from app_eda import run_eda
from app_ml import run_ml
import pathlib


def load_css():
    css_path = pathlib.Path(__file__).parent / 'styles.css'
    if css_path.exists():
        with open(css_path, 'r', encoding='utf-8') as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def main():
    st.set_page_config(page_title='자동차 구매 금액 예측', layout='wide')

    load_css()

    # Header
    st.markdown(
        "<div class='header'>"
        "<div style='flex:1'>"
        "<div class='title'>자동차 구매 금액 예측</div>"
        "<div class='subtitle'>데이터 기반으로 구매 금액을 예측하고, 간단한 EDA 도구를 제공합니다.</div>"
        "</div>"
        "<div class='kit'>"
        "<div class='metric card'>v1.0</div>"
        "</div>"
        "</div>", unsafe_allow_html=True)

    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0]:
        run_home()
    elif choice == menu[1]:
        run_eda()
    elif choice == menu[2]:
        run_ml()



if __name__ == '__main__':
    main()