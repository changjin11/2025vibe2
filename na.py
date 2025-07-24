import streamlit as st
import random

# ---------------- 상태 초기화 ----------------
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
    st.session_state.honeymoon_level = 0  # 0~3

# ---------------- 대사 목록 ----------------
beg_quotes = [
    "형... 천 원만...", "밥 한 끼만 사주라...", "나는 왜 이러고 살까...",
    "치킨 시켜줘...", "배고파... 츄릅...", "그냥 눌러만 줘...",
    "현질 좀... 그거 안 되겠니?", "형 나 진짜 오늘은... ㅠㅠ"
]

scolding_quotes = [
    "야 전, 그게 벌 수 있는 최대야?", "일 안 해? 돈 안 벌어?",
    "전, 너 요즘 열정이 식었다?", "메가 추는 돈이 부족하단 말이야.", "전, 나 실망이다..."
]

love_quotes = [
    "전... 넌 내 전부야 ❤️", "전, 같이 있어서 행복해.", "우리 박이를 위해 더 열심히 벌자!",
    "내가 널 얼마나 좋아하는지 알아?", "사랑해, 전."
]

heart_stages = ["❤️", "💖", "💘", "💗"]

# ---------------- 페이지 설정 ----------------
st.set_page_config(page_title="추 키우기", page_icon="🐷", layout="centered")

# 💰 돈 좌측 상단에 표시
st.markdown(f"""
    <div style='position: absolute; top: 10px; left: 15px; font-size: 16px; color: gray;'>
        💰 {st.session_state.money:,}원
    </div>
""", unsafe_allow_html=True)

# ---------------- 타이틀 ----------------
st.markdown("""
    <h2 style='text-align: center; color: #ff69b4;'>💸 추 키우기</h2>
    <p style='text-align: center; font-size: 14px; color: gray;'>한 푼 두 푼 모아 부자 추 만들기</p>
""", unsafe_allow_html=True)

# ---------------- 상점 ----------------
with st.expander("🛍️ 상점", expanded=False):
    if not st.session_state.has_jeon:
        if st.button("💸 15,000원 - 전 같이 키우기"):
            if st.session_state.money >= 15000:
                st.session_state.money -= 15000
                st.session_state.has_jeon = True
                st.success("🧑 전을 영입했습니다!")
            else:
                st.warning("💰 돈이 부족해요!")

    if st.session_state.has_jeon and not st.session_state.is_mega_chu:
        if st.button("✨ 30,000원 - 추 진화 시키기"):
            if st.session_state.money >= 30000:
                st.session_state.money -= 30000
                st.session_state.is_mega_chu = True
                st.success("🦍 메가 추로 진화했습니다!")
            else:
                st.warning("💰 돈이 부족해요!")

    if st.session_state.has_jeon and st.session_state.is_mega_chu and not st.session_state.is_married:
        if st.button("💍 60,000원 - 추&전 결혼 시키기"):
            if st.session_state.money >= 60000:
                st.session_state.money -= 60000
                st.session_state.is_married = True
                st.success("💑 결혼 완료! 박 등장!")
            else:
                st.warning("💰 돈이 부족해요!")

# ---------------- 가족여행 ----------------
if st.session_state.is_married and st.session_state.honeymoon_level < 3:
    if st.button(f"🏖 가족여행 ({st.session_state.honeymoon_level}/3) - 25,000원"):
        if st.session_state.money >= 25000:
            st.session_state.money -= 25000
            st.session_state.honeymoon_level += 1
            st.success("🌈 하트가 더 커지고 화려해졌습니다!")
        else:
            st.warning("💰 가족여행 비용 부족!")

# ---------------- 캐릭터 출력 ----------------
with st.form("chu_click_form"):
    # 추 버튼 크게
    chu_emoji = "🦍" if st.session_state.is_mega_chu else "🐷"
    chu_button = f"<button type='submit' style='all: unset; cursor: pointer; font-size: 110px;'>{chu_emoji}</button>"

    # 하트 크기 증가
    heart = ""
    if st.session_state.is_married:
        level = min(st.session_state.honeymoon_level, 3)
        heart = f"<span style='font-size:{40 + level * 10}px'>{heart_stages[level]}</span>"

    # 전 캐릭터
    jeon = """
    <span style='
        font-size: 80px;
        display: inline-block;
        cursor: default;
        padding: 0 10px;
        transform: translateY(5px);
    '>🧑</span>
    """ if st.session_state.has_jeon else ""

    # 박 캐릭터
    park = "<span style='font-size:40px'>👶 박</span>" if st.session_state.is_married else ""

    # 출력
    st.markdown(f"""
        <div style='display: flex; justify-content: center; align-items: center; gap: 18px; margin-top: 20px;'>
            {chu_button}
            {heart}
            {jeon}
            {park}
        </div>
    """, unsafe_allow_html=True)

    # 클릭 처리
    clicked = st.form_submit_button()
    if clicked:
        gain = random.randint(100, 500)
        st.session_state.money += gain

        # 대사
        if st.session_state.is_married:
            st.session_state.last_quote = f"💖 <i>{random.choice(love_quotes)}</i>"
        elif st.session_state.is_mega_chu:
            st.session_state.last_quote = f"🦍 <i>{random.choice(scolding_quotes)}</i>"
        else:
            st.session_state.last_quote = f"🐽 <i>{random.choice(beg_quotes)}</i>"

        # 전 수익 보너스
        if st.session_state.has_jeon:
            st.session_state.money += gain // 2

# ---------------- 말풍선 ----------------
st.markdown(f"""
    <div style='display: flex; justify-content: center; margin-top: 10px;'>
        <div style="
            background: #fefefe;
            border-radius: 10px;
            padding: 10px 16px;
            font-size: 16px;
            color: #333;
            border: 1px solid #ccc;
            max-width: 260px;
            text-align: center;">
            💬 {st.session_state.last_quote}
        </div>
    </div>
""", unsafe_allow_html=True)
