import streamlit as st
import random

# --- 상태 초기화 ---
if "money" not in st.session_state:
    st.session_state.money = 0
if "last_quote" not in st.session_state:
    st.session_state.last_quote = "🐽 <i>나를 눌러줘...</i>"
if "has_jeon" not in st.session_state:
    st.session_state.has_jeon = False
if "is_mega_chu" not in st.session_state:
    st.session_state.is_mega_chu = False
if "is_married" not in st.session_state:
    st.session_state.is_married = False
if "honeymoon_level" not in st.session_state:
    st.session_state.honeymoon_level = 0  # 최대 3

# --- 대사 목록 ---
beg_quotes = [
    "형... 천 원만...",
    "밥 한 끼만 사주라...",
    "나는 왜 이러고 살까...",
    "치킨 시켜줘...",
    "배고파... 츄릅...",
    "그냥 눌러만 줘...",
    "현질 좀... 그거 안 되겠니?",
    "형 나 진짜 오늘은... ㅠㅠ"
]

scolding_quotes = [
    "야 전, 그게 벌 수 있는 최대야?",
    "일 안 해? 돈 안 벌어?",
    "전, 너 요즘 열정이 식었다?",
    "메가 추는 돈이 부족하단 말이야.",
    "전, 나 실망이다..."
]

love_quotes = [
    "전... 넌 내 전부야 ❤️",
    "전, 같이 있어서 행복해.",
    "우리 박이를 위해 더 열심히 벌자!",
    "내가 널 얼마나 좋아하는지 알아?",
    "사랑해, 전."
]

heart_stages = ["❤️", "💖", "💘", "💗"]

# --- 타이틀 ---
st.set_page_config(page_title="추 키우기", page_icon="🐷", layout="centered")
st.markdown("""
    <h1 style='text-align: center; font-size: 48px; color: #ff69b4;'>💸 추 키우기 💸</h1>
    <p style='text-align: center; font-size: 18px; color: gray;'>한 푼 두 푼 모아 부자 추 만들기</p>
    <hr>
""", unsafe_allow_html=True)

# --- 상점 ---
with st.expander("🛍️ 상점"):
    st.markdown("### 🧑 전 같이 키우기")
    if not st.session_state.has_jeon:
        if st.button("💸 15,000원으로 전 영입하기"):
            if st.session_state.money >= 15000:
                st.session_state.money -= 15000
                st.session_state.has_jeon = True
                st.success("🧑 전을 영입했습니다!")
            else:
                st.warning("💰 돈이 부족해요!")

    if st.session_state.has_jeon:
        st.markdown("### 🦍 추 진화 시키기")
        if not st.session_state.is_mega_chu:
            if st.button("✨ 30,000원으로 메가 추 진화"):
                if st.session_state.money >= 30000:
                    st.session_state.money -= 30000
                    st.session_state.is_mega_chu = True
                    st.success("🦍 메가 추로 진화했습니다!")
                else:
                    st.warning("💰 돈이 부족해요!")

    if st.session_state.has_jeon and st.session_state.is_mega_chu:
        st.markdown("### 💍 추&전 결혼 시키기")
        if not st.session_state.is_married:
            if st.button("💖 60,000원으로 결혼하기"):
                if st.session_state.money >= 60000:
                    st.session_state.money -= 60000
                    st.session_state.is_married = True
                    st.success("💍 추와 전이 결혼했습니다!")
                else:
                    st.warning("💰 돈이 부족해요!")

# --- 가족여행 버튼 ---
if st.session_state.is_married and st.session_state.honeymoon_level < 3:
    if st.button(f"🏖 가족여행 떠나기 ({st.session_state.honeymoon_level}/3회) - 비용: 25,000원"):
        if st.session_state.money >= 25000:
            st.session_state.money -= 25000
            st.session_state.honeymoon_level += 1
            st.success("가족여행을 다녀왔습니다! ❤️ 하트가 커졌어요!")
        else:
            st.warning("💰 가족여행 비용이 부족해요!")

# --- 캐릭터 영역 ---
with st.form("chu_click_form"):
    st.markdown("""
        <div style='display: flex; justify-content: center; align-items: center; margin-top: 40px; gap: 20px;'>
    """, unsafe_allow_html=True)

    # 추 캐릭터
    chu_emoji = "🦍" if st.session_state.is_mega_chu else "🐷"
    st.markdown(f"""
        <button type="submit"
            style="
                all: unset;
                font-size: 100px;
                line-height: 1;
                cursor: pointer;">
            {chu_emoji}
        </button>
    """, unsafe_allow_html=True)

    # 하트
    if st.session_state.is_married:
        heart = heart_stages[min(st.session_state.honeymoon_level, 3)]
        st.markdown(f"<div style='font-size: {40 + st.session_state.honeymoon_level * 10}px;'>{heart}</div>", unsafe_allow_html=True)

    # 전
    if st.session_state.has_jeon:
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

    # 박 (자녀)
    if st.session_state.is_married:
        st.markdown("<div style='font-size: 40px;'>👶 박</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # 클릭 처리
    submitted = st.form_submit_button()
    if submitted:
        gain = random.randint(100, 500)
        st.session_state.money += gain

        # 대사
        if st.session_state.is_married:
            st.session_state.last_quote = f"💖 <i>{random.choice(love_quotes)}</i>"
        elif st.session_state.is_mega_chu:
            st.session_state.last_quote = f"🦍 <i>{random.choice(scolding_quotes)}</i>"
        else:
            st.session_state.last_quote = f"🐽 <i>{random.choice(beg_quotes)}</i>"

        if st.session_state.has_jeon:
            st.session_state.money += gain // 2

# --- 말풍선 ---
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

# --- 보유 금액 ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'>💰 보유 금액: {st.session_state.money:,} 원</h3>", unsafe_allow_html=True)
