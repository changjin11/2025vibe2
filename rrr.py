import streamlit as st
import random

# ----------------- 설정 -----------------
st.set_page_config(page_title="가위바위보 데스매치", layout="centered")

# ----------------- 상태 초기화 -----------------
if "user_wins" not in st.session_state:
    st.session_state.user_wins = 0
if "computer_wins" not in st.session_state:
    st.session_state.computer_wins = 0
if "round" not in st.session_state:
    st.session_state.round = 1
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "judge_speech" not in st.session_state:
    st.session_state.judge_speech = "승자만이 살아남는다... 준비됐나?"

# ----------------- 이모지 및 선택 -----------------
choices = ["가위", "바위", "보"]
emoji = {"가위": "✌️", "바위": "✊", "보": "✋"}

# ----------------- 결과 판정 함수 -----------------
def get_result(user, computer):
    if user == computer:
        return "무승부"
    elif (user == "가위" and computer == "보") or \
         (user == "바위" and computer == "가위") or \
         (user == "보" and computer == "바위"):
        return "승리"
    else:
        return "패배"

# ----------------- 상단 스코어 -----------------
score_text = f"👤 {st.session_state.user_wins} : {st.session_state.computer_wins} 🤖"
st.markdown(f"<h3 style='text-align: left;'>{score_text}</h3>", unsafe_allow_html=True)

# ----------------- 중앙: 진행자 캐릭터 -----------------
st.markdown("<div style='text-align: center;'>"
            "<img src='https://raw.githubusercontent.com/gkswjdzz/imagecdn/main/judge.png' width='120'>"
            "</div>", unsafe_allow_html=True)

# ----------------- 진행자 말풍선 -----------------
st.markdown(f"<div style='text-align: center; font-size: 18px; padding: 10px; border: 2px solid #ccc; border-radius: 10px; width: 70%; margin: auto;'>{st.session_state.judge_speech}</div>", unsafe_allow_html=True)

# ----------------- 플레이어 캐릭터 -----------------
col_left, col_center, col_right = st.columns([2, 1, 2])
with col_left:
    st.markdown("<h3 style='text-align: center;'>👤 사용자</h3>", unsafe_allow_html=True)
with col_right:
    st.markdown("<h3 style='text-align: center;'>컴퓨터 🤖</h3>", unsafe_allow_html=True)

# ----------------- 하단 선택 버튼 -----------------
if not st.session_state.game_over:
    st.markdown("---")
    st.markdown("### ✊ ✌️ ✋ 선택하세요!")
    col1, col2, col3 = st.columns(3)
    user_choice = None

    with col1:
        if st.button("✌️ 가위"):
            user_choice = "가위"
    with col2:
        if st.button("✊ 바위"):
            user_choice = "바위"
    with col3:
        if st.button("✋ 보"):
            user_choice = "보"

    if user_choice:
        computer_choice = random.choice(choices)
        result = get_result(user_choice, computer_choice)

        if result == "승리":
            st.session_state.user_wins += 1
            st.session_state.judge_speech = f"👨‍⚖️ 심판: {emoji[user_choice]} vs {emoji[computer_choice]} → 인간의 승리!"
        elif result == "패배":
            st.session_state.computer_wins += 1
            st.session_state.judge_speech = f"👨‍⚖️ 심판: {emoji[user_choice]} vs {emoji[computer_choice]} → 컴퓨터의 승리!"
        else:
            st.session_state.judge_speech = f"👨‍⚖️ 심판: {emoji[user_choice]} vs {emoji[computer_choice]} → 무승부다."

        st.session_state.round += 1

        # 게임 종료 여부 확인
        if st.session_state.user_wins == 3:
            st.session_state.game_over = True
            st.session_state.judge_speech = "🎉 인간이 승리했다! 살아남았다!"
        elif st.session_state.computer_wins == 3:
            st.session_state.game_over = True
            st.session_state.judge_speech = "💀 컴퓨터가 이겼다... 인간은 죽었다."

# ----------------- 게임 종료 시 다시하기 -----------------
if st.session_state.game_over:
    st.markdown("---")
    if st.button("🔁 다시하기"):
        st.session_state.user_wins = 0
        st.session_state.computer_wins = 0
        st.session_state.round = 1
        st.session_state.game_over = False
        st.session_state.judge_speech = "승자만이 살아남는다... 준비됐나?"
