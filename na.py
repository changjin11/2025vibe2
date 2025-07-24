import streamlit as st
import random

# --- 초기 상태 설정 ---
if "money" not in st.session_state:
    st.session_state.money = 0
if "last_quote" not in st.session_state:
    st.session_state.last_quote = "🐽 <i>나를 눌러줘...</i>"
if "has_jeon" not in st.session_state:
    st.session_state.has_jeon = False

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

# --- 페이지 설정 및 타이틀 ---
st.set_page_config(page_title="추 키우기", page_icon="🐷", layout="centered")
st.markdown("""
    <h1 style='text-align: center; font-size: 48px; color: #ff69b4;'>💸 추 키우기 💸</h1>
    <p style='text-align: center; font-size: 18px; color: gray;'>한 푼 두 푼 모아 부자 추 만들기</p>
    <hr>
""", unsafe_allow_html=True)

# --- 상점 섹션 ---
with st.expander("🛍️ 상점"):
    st.markdown("### 🧑 전 같이 키우기")
    st.markdown("- 추와 함께 돈을 버는 동료입니다.")
    st.markdown("- 추를 클릭할 때마다, 전이 추가로 절반 수익을 벌어줍니다.")
    if not st.session_state.has_jeon:
        if st.button("💸 5,000원으로 전 영입하기"):
            if st.session_state.money >= 5000:
                st.session_state.money -= 5000
                st.session_state.has_jeon = True
                st.success("🧑 전을 영입했습니다!")
            else:
                st.warning("💰 돈이 부족해요!")

# --- 추 캐릭터 클릭 영역 ---
with st.form("chu_click_form"):
    st.markdown("""
        <div style='display: flex; justify-content: center; align-items: center; margin-top: 40px; gap: 50px;'>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="small")

    with col1:
        st.markdown("""
            <button type="submit"
                style="
                    all: unset;
                    font-size: 100px;
                    line-height: 1;
                    cursor: pointer;">
                🐷
            </button>
        """, unsafe_allow_html=True)

    # 전 캐릭터 등장 조건
    if st.session_state.has_jeon:
        with col2:
            st.markdown("""
                <button name="jeon_click" type="submit"
                    style="
                        all: unset;
                        font-size: 100px;
                        line-height: 1;
                        cursor: pointer;">
                    🧑
                </button>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    submitted = st.form_submit_button()
    if submitted:
        gain = random.randint(100, 500)
        st.session_state.money += gain
        st.session_state.last_quote = f"🐽 <i>{random.choice(quotes)}</i>"

        # 전이 있으면 절반 추가 수익
        if st.session_state.has_jeon:
            st.session_state.money += gain // 2

# --- 말풍선 출력 ---
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

# --- 보유 금액 표시 ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'>💰 보유 금액: {st.session_state.money:,} 원</h3>", unsafe_allow_html=True)
