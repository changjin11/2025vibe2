import streamlit as st
import random

# 초기 상태
if "money" not in st.session_state:
    st.session_state.money = 0
if "last_quote" not in st.session_state:
    st.session_state.last_quote = "🐽 <i>나를 눌러줘...</i>"

quotes = [
    "형... 천 원만...",
    "밥 한 끼만 사주라...",
    "나는 왜 이러고 살까import streamlit as st
import random

# 초기 상태
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

# 타이틀
st.markdown("""
    <h1 style='text-align: center; font-size: 48px; color: #ff69b4;'>💸 추 키우기 💸</h1>
    <p style='text-align: center; font-size: 18px; color: gray;'>한 푼 두 푼 모아 부자 추 만들기</p>
    <hr>
""", unsafe_allow_html=True)

# 캐릭터 클릭 폼
with st.form("chu_click_form"):
    st.markdown("""
        <div style='display: flex; justify-content: center; align-items: center;'>
            <button type="submit"
                style="
                    font-size: 80px;
                    background: none;
                    border: none;
                    cursor: pointer;
                    outline: none;
                ">
                🐷
            </button>
        </div>
    """, unsafe_allow_html=True)

    submitted = st.form_submit_button()
    if submitted:
        st.session_state.money += random.randint(100, 500)
        st.session_state.last_quote = f"🐽 <i>{random.choice(quotes)}</i>"

# 말풍선 스타일
st.markdown(f"""
    <div style="
        display: flex;
        justify-content: center;
        margin-top: 20px;">
        <div style="
            position: relative;
            background: #fefefe;
            border-radius: 12px;
            padding: 14px 20px;
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
                transform: translateX(-50%);
                width: 0;
                height: 0;
                border: 12px solid transparent;
                border-top-color: #ccc;
                border-bottom: 0;">
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 보유 금액
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'>💰 보유 금액: {st.session_state.money:,} 원</h3>", unsafe_allow_html=True)

    "치킨 시켜줘...",
    "배고파... 츄릅...",
    "그냥 눌러만 줘...",
    "현질 좀... 그거 안 되겠니?",
    "형 나 진짜 오늘은... ㅠㅠ"
]

# 타이틀
st.markdown("""
    <h1 style='text-align: center; font-size: 48px; color: #ff69b4;'>💸 추 키우기 💸</h1>
    <p style='text-align: center; font-size: 18px; color: gray;'>한 푼 두 푼 모아 부자 추 만들기</p>
    <hr>
""", unsafe_allow_html=True)

# 캐릭터 + 말풍선 배치 (오른쪽 정렬)
with st.form("chu_click_form"):
    st.markdown("""
        <div style="display: flex; justify-content: flex-end; align-items: center; margin-top: 30px; margin-right: 10%;">
            <div style='margin-right: 30px;'>
                <div style="
                    position: relative;
                    background: #fefefe;
                    border-radius: 12px;
                    padding: 14px 20px;
                    font-size: 20px;
                    color: #333;
                    border: 2px solid #ccc;
                    max-width: 280px;
                    ">
                    💬 """ + st.session_state.last_quote + """
                    <div style="
                        content: '';
                        position: absolute;
                        top: 50%;
                        right: -20px;
                        transform: translateY(-50%);
                        width: 0;
                        height: 0;
                        border: 12px solid transparent;
                        border-left-color: #ccc;
                        border-right: 0;">
                    </div>
                </div>
            </div>

            <button type="submit"
                style="
                    font-size: 80px;
                    background: none;
                    border: none;
                    cursor: pointer;
                    outline: none;
                ">
                🐷
            </button>
        </div>
    """, unsafe_allow_html=True)

    submitted = st.form_submit_button()
    if submitted:
        st.session_state.money += random.randint(100, 500)
        st.session_state.last_quote = f"<i>{random.choice(quotes)}</i>"

# 보유 금액 표시
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'>💰 보유 금액: {st.session_state.money:,} 원</h3>", unsafe_allow_html=True)
