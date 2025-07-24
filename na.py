import streamlit as st
import random

# --- 페이지 설정 ---
st.set_page_config(page_title="추 키우기", page_icon="🐷", layout="centered")

# --- 상태 초기화 ---
if "money" not in st.session_state:
    st.session_state.money = 0
if "last_quote" not in st.session_state:
    st.session_state.last_quote = "🐽 <i>나를 눌러줘...</i>"

# --- 대사 목록 ---
quotes = [
    "형... 천 원만...",
    "밥 한 끼만 사주라...",
    "나는 왜 이러고 살까...",
    "치킨 시켜줘...",
    "배고파... 츄릅...",
    "그냥 눌러만 줘...",
    "현질 좀... 그거 안 되겠니?",
    "형 나 진짜 오늘은... ㅠㅠ"
]

# --- 타이틀 영역 ---
st.markdown("""
    <h1 style='text-align: center; font-size: 48px; color: #ff69b4;'>💸 추 키우기 💸</h1>
    <p style='text-align: center; font-size: 18px; color: gray;'>한 푼 두 푼 모아 부자 추 만들기</p>
    <hr>
""", unsafe_allow_html=True)

# --- 캐릭터 및 클릭 처리 ---
with st.form("chu_click_form"):
    st.markdown("""
        <div style='display: flex; justify-content: center; align-items: center; margin-top: 40px;'>
            <button type="submit"
                style="
                    all: unset;
                    font-size: 100px;
                    line-height: 1;
                    cursor: pointer;">
                🐷
            </button>
        </div>
    """, unsafe_allow_html=True)

    submitted = st.form_submit_button()
    if submitted:
        st.session_state.money += random.randint(100, 500)
        st.session_state.last_quote = f"🐽 <i>{random.choice(quotes)}</i>"

# --- 말풍선 출력 (중앙 아래) ---
st.markdown(f"""
    <div style='display: flex; justify-content: center; margin-top: 20px;'>
        <div style="
            position: relative;
            background: #fefefe;
            border-radius: 12px;
            padding: 14px 20px;
            font-size: 20px;
            color: #333;
            border: 2px solid #ccc;
            max-width: 300px;
            text-align: center;">
            💬 {st.session_state.last_quote}
            <div style="
                content: '';
                position: absolute;
                top: -16px;
                left: 50%;
                transform: translateX(-50%);
                width: 0;
                height: 0;
                border: 10px solid transparent;
                border-bottom-color: #ccc;">
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 돈 표시 ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'>💰 보유 금액: {st.session_state.money:,} 원</h3>", unsafe_allow_html=True)
