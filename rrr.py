import streamlit as st
import random

# ---------- 설정 ----------
st.set_page_config(page_title="가위바위보 데스매치", layout="centered")
st.title("💀 가위바위보: 데스매치")
st.markdown("### 👨‍⚖️ 진행자: '승자만이 살아남는다... 준비됐나?'")

# ---------- 이미지 URL ----------
judge_url = "https://raw.githubusercontent.com/gkswjdzz/imagecdn/main/judge.png"
gunshot_url = "https://raw.githubusercontent.com/gkswjdzz/imagecdn/main/gunshot.gif"

# ---------- 세션 상태 초기화 ----------
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

# ---------- 게임 규칙 ----------
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

# ---------- UI 출력 ----------
st.image(judge_url, caption="진행자", use_container_width=True)
st.markdown(f"### 🎲 Round {st.session_state.round} / 최대 5판")

# ---------- 가위바위보 버튼 ----------
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

# ---------- 게임 처리 ----------
if user_choice and not st.session_state.game_over:
    computer_choice = random.choice(choices)
    result = get_result(user_choice, computer_choice)

    if result == "승리":
        st.session_state.user_wins += 1
        outcome = "🎉 당신의 승리!"
        st.session_state.last_loser = "컴퓨터"
    elif result == "패배":
        st.session_state.computer_wins += 1
        outcome = "😈 컴퓨터가 이겼습니다..."
        st.session_state.last_loser = "사용자"
    else:
        outcome = "😐 무승부입니다."
        st.session_state.last_loser = None

    # 전투 기록
    log = f"Round {st.session_state.round}: 당신 {emoji[user_choice]} vs 컴퓨터 {emoji[computer_choice]} → {outcome}"
    st.session_state.battle_log.append(log)

    st.session_state.round += 1

    # 3선승 체크
    if st.session_state.user_wins == 3:
        st.session_state.game_over = True
        st.success("🎊 당신이 이겼습니다! 인간의 승리!")
    elif st.session_state.computer_wins == 3:
        st.session_state.game_over = True
        st.error("💀 당신은 패배했습니다... 총살당했습니다.")

# ---------- 결과 출력 ----------
if st.session_state.battle_log:
    st.markdown("### 📝 전투 기록")
    for log in reversed(st.session_state.battle_log):
        st.markdown(f"- {log}")

    # 마지막 총 쏘는 장면 출력
    if st.session_state.last_loser == "사용자":
        st.markdown("#### 💥 진행자: '너무 약하군...'")
        st.image(gunshot_url, caption="🔫 사용자 사망", use_container_width=True)
    elif st.session_state.last_loser == "컴퓨터":
        st.markdown("#### 🔥 진행자: 'AI를 꺾다니... 대단하군!'")
        st.image(gunshot_url, caption="🔫 컴퓨터 파괴", use_container_width=True)

# ---------- 점수 표시 ----------
st.markdown("---")
st.markdown("### 📊 현재 스코어")
st.markdown(f"👤 사용자: {st.session_state.user_wins}승")
st.markdown(f"💻 컴퓨터: {st.session_state.computer_wins}승")

# ---------- 게임 종료 ----------
if st.session_state.game_over:
    st.markdown("---")
    st.markdown("### 🧑‍⚖️ 진행자: '전투 종료...'")
    if st.button("🔄 다시 도전하기"):
        st.session_state.user_wins = 0
        st.session_state.computer_wins = 0
        st.session_state.round = 1
        st.session_state.game_over = False
        st.session_state.battle_log = []
        st.session_state.last_loser = None
