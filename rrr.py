import streamlit as st
import random

# ---------- 기본 설정 ----------
st.set_page_config(page_title="가위바위보 데스매치", layout="centered")
st.title("💀 가위바위보: 데스매치")
st.markdown("### 👨‍⚖️ 진행자: '승자만이 살아남는다... 준비됐나?'")

# ---------- 이미지 URL ----------
judge_url = "https://raw.githubusercontent.com/gkswjdzz/imagecdn/main/judge.png"
gunshot_url = "https://raw.githubusercontent.com/gkswjdzz/imagecdn/main/gunshot.gif"

# ---------- 상태 초기화 ----------
if "user_wins" not in st.session_state:
    st.session_state.user_wins = 0
if "computer_wins" not in st.session_state:
    st.session_state.computer_wins = 0
if "round" not in st.session_state:
    st.session_state.round = 1
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "battle_log" not in st.session_state:
    st.session_state.battle_log = []
if "last_loser" not in st.session_state:
    st.session_state.last_loser = None

# ---------- 가위바위보 ----------
choices = ["가위", "바위", "보"]
emoji = {"가위": "✌️", "바위": "✊", "보": "✋"}

def get_result(user, computer):
    if user == computer:
        return "무승부"
    elif (user == "가위" and computer == "보") or \
         (user == "바위" and computer == "가위") or \
         (user == "보" and computer == "바위"):
        return "승리"
    else:
        return "패배"

# ---------- 진행자 이미지 ----------
st.image(judge_url, caption="👨‍⚖️ 심판", use_container_width=True)
st.markdown(f"### 🎲 Round {st.session_state.round} / 최대 5판")

# ---------- 선택 버튼 ----------
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

# ---------- 진행 ----------
if user_choice and not st.session_state.game_over:
    computer_choice = random.choice(choices)
    result = get_result(user_choice, computer_choice)

    if result == "승리":
        st.session_state.user_wins += 1
        st.session_state.last_loser = "컴퓨터"
        outcome = "🎉 당신의 승리!"
    elif result == "패배":
        st.session_state.computer_wins += 1
        st.session_state.last_loser = "사용자"
        outcome = "😈 컴퓨터의 승리..."
    else:
        st.session_state.last_loser = None
        outcome = "😐 무승부입니다."

    log = f"Round {st.session_state.round}: 당신 {emoji[user_choice]} vs 컴퓨터 {emoji[computer_choice]} → {outcome}"
    st.session_state.battle_log.append(log)
    st.session_state.round += 1

    if st.session_state.user_wins == 3:
        st.session_state.game_over = True
        st.success("🎊 당신이 최종 승자입니다!")
    elif st.session_state.computer_wins == 3:
        st.session_state.game_over = True
        st.error("💀 컴퓨터가 당신을 제거했습니다...")

# ---------- 전투 기록 ----------
if st.session_state.battle_log:
    st.markdown("### 📝 전투 기록")
    for log in reversed(st.session_state.battle_log):
        st.markdown(f"- {log}")

    # 총 쏘는 연출
    if st.session_state.last_loser == "사용자":
        st.markdown("#### 💥 심판: '인간은 여기까지인가...'")
        st.image(gunshot_url, caption="🔫 사용자 사망", use_container_width=True)
    elif st.session_state.last_loser == "컴퓨터":
        st.markdown("#### 🔥 심판: 'AI를 파괴하다니... 대단하군!'")
        st.image(gunshot_url, caption="🔫 컴퓨터 파괴", use_container_width=True)

# ---------- 스코어판 ----------
def get_score_icons(wins, icon="●", empty="○"):
    return icon * wins + empty * (3 - wins)

user_score = get_score_icons(st.session_state.user_wins)
comp_score = get_score_icons(st.session_state.computer_wins)

st.markdown("---")
st.markdown("### ⚖️ 스코어 현황")
st.markdown(f"👤 사용자: {user_score}  VS  {comp_score} :컴퓨터 🤖")

# ---------- 재시작 ----------
if st.session_state.game_over:
    st.markdown("---")
    st.markdown("### 🧑‍⚖️ 심판: '전투 종료...'")
    if st.button("🔄 다시 도전하기"):
        st.session_state.user_wins = 0
        st.session_state.computer_wins = 0
        st.session_state.round = 1
        st.session_state.game_over = False
        st.session_state.battle_log = []
        st.session_state.last_loser = None
