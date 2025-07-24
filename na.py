import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="추 키우기", page_icon="🐾", layout="centered")

# 2. 상태 초기화
if "money" not in st.session_state:
    st.session_state.money = 0
if "last_quote" not in st.session_state:
    st.session_state.last_quote = "나를 눌러줘..."

# 3. 대사 리스트
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

# 4. 타이틀 꾸미기
st.markdown("""
    <h1 style='text-align: center; font-size: 48px; color: #ff69b4;'>💸 추 키우기 💸</h1>
    <p style='text-align: center; font-size: 18px; color: gray;'>한 푼 두 푼 모아 부자 추 만들기</p>
""", unsafe_allow_html=True)

st.markdown("---")

# 5. 중앙 캐릭터 영역
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

if st.button("🐷 추 (클릭해서 구걸하기)", key="chu_click", help="눌러서 추에게 돈을 주세요"):
    st.session_state.money += random.randint(100, 500)  # 랜덤 수입
    st.session_state.last_quote = random.choice(quotes)

# 말풍선 출력
st.markdown(f"""
    <div style='margin-top: 20px; background-color: #f0f0f0; border-radius: 12px;
                padding: 15px; display: inline-block; font-size: 20px;'>
        💬 <i>{st.session_state.last_quote}</i>
    </div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# 6. 돈 표시
st.markdown("---")
st.markdown(f"<h3 style='text-align: center;'>💰 보유 금액: {st.session_state.money} 원</h3>", unsafe_allow_html=True)
