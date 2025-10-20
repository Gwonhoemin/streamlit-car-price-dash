import streamlit as st
import pandas as pd
import pathlib


def run_home():
    st.subheader('자동차 데이터를 분석하고, 예측하는 앱')
    # Resolve data and image paths relative to this file
    data_path = pathlib.Path(__file__).parent / 'data' / 'Car_Purchasing_Data.csv'
    image_path = pathlib.Path(__file__).parent / 'image' / 'car.jpg'

    # Load dataset counts (if available) to show in metrics
    n_rows = '--'
    n_cols = '--'
    try:
        if data_path.exists():
            df = pd.read_csv(data_path)
            n_rows = f"{len(df):,}"
            n_cols = f"{df.shape[1]}"
    except Exception:
        # keep defaults if read fails
        pass

    # Brief cards
    col1, col2, col3 = st.columns([1.5, 1, 1])
    with col1:
        st.markdown("<div class='card'>"
                    "<div style='font-size:1.1rem; font-weight:600'>소개</div>"
                    "<div class='info-muted small' style='margin-top:0.4rem'>탐색적 데이터분석(EDA)과 머신러닝 기반의 자동차 구매 금액 예측을 제공합니다.</div>"
                    "</div>", unsafe_allow_html=True)
    with col2:
        st.metric(label='데이터 행 수', value=n_rows)
    with col3:
        st.metric(label='특성 수', value=n_cols)

    # Card with description + image (use st.image to ensure Streamlit serves the file correctly)
    st.markdown("<div style='margin-top:1rem' class='card'>", unsafe_allow_html=True)
    c1, c2 = st.columns([3, 1])
    with c1:
        st.markdown("<div style='font-size:1rem; font-weight:700'>시작하기</div>", unsafe_allow_html=True)
        st.markdown("<div class='small info-muted'>사이드바에서 EDA 또는 ML 페이지로 이동해보세요.</div>", unsafe_allow_html=True)
    with c2:
        if image_path.exists():
            st.image(str(image_path), use_container_width=False)
        else:
            st.markdown("<div class='small info-muted'>이미지 파일이 없습니다: image/car.jpg</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
