import streamlit as st
import random

# --- 설정 ---
st.set_page_config(page_title="추 키우기", page_icon="🐷", layout="centered")

# --- 상태 초기화 ---
if "money" not in st.session_state:
    st.session_state.money = 0
if "last_quote" not in st.session_state:
    st.session_state.last_quote = "🐽 <i>나를 눌러줘...</i>"

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

# --- 타이틀 ---
st.markdown("""
    <h1 style='text-align: center; font-size: 48px; color: #ff69b4; margin-bottom: 0;'>💸 추 키우기 💸</h1>
    <p style='text-align: center; font-size: 18px; color: gray; margin-top: 4px;'>한 푼 두 푼 모아 부자 추 만들기</p>
    <hr>
""", unsafe_allow_html=True)

# --- 중앙 캐릭터 영역 ---
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

# 🐷 캐릭터 버튼 크게 표시
if st.button("🐷", key="chu_click", help="눌러서 추에게 돈을 주세요"):
    st.session_state.money += random.randint(100, 500)
    st.session_state.last_quote = f"🐽 <i>{random.choice(quotes)}</i>"

# 말풍선 스타일
st.markdown(f"""
    <div style="
        display: inline-block;
        position: relative;
        background: #fefefe;
        border-radius: 12px;
        padding: 14px 20px;
        margin-top: 20px;
        font-size: 20px;
        color: #333;
        border: 2px solid #ccc;
        max-width: 300px;">
        {st.session_state.last_quote}
        <div style="
            content: '';
            position: absolute;
            bottom: -20px;
            left: 50%;
            margin-left: -12px;
            width: 0;
            height: 0;
            border: 12px solid transparent;
            border-top-color: #ccc;
            border-bottom: 0;
            margin-top: -1px;
        "></div>
    </div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- 보유 금액 ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'>💰 보유 금액: {st.session_state.money:,} 원</h3>", unsafe_allow_html=True)
