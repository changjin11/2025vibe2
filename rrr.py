import streamlit as st
import random

# ----------------- 설정 -----------------
st.set_page_config(page_title="죽음을 건 가위바위보", layout="centered")
st.title("💀 죽음을 건 가위바위보 대결")
st.markdown("인간과 AI의 **5판 3선승제** 대결...\n지면 **죽음**이 기다립니다...")

# ----------------- 초기 상태 -----------------
if "user_wins" not in st.session_state:
    st.session_state.user_wins = 0
if "computer_wins" not in st.session_state:
    st.session_state.computer_wins = 0
if "round" not in st.session_state:
    st.session_state.round = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "battle_log" not in st.session_state:
    st.session_state.battle_log = []

# ----------------- 가위바위보 로직 -----------------
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

# ----------------- 게임 중 -----------------
if not st.session_state.game_over:

    st.markdown(f"### ⚔️ Round {st.session_state.round + 1}")

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
        st.session_state.round += 1

        # 결과 반영
        if result == "승리":
            st.session_state.user_wins += 1
            outcome = "🎉 당신의 승리!"
        elif result == "패배":
            st.session_state.computer_wins += 1
            outcome = "😈 컴퓨터가 이겼습니다..."
        else:
            outcome = "😐 무승부입니다."

        # 로그 기록
        st.session_state.battle_log.append(
            f"Round {st.session_state.round}: 당신 {emoji[user_choice]} vs 컴퓨터 {emoji[computer_choice]} → {outcome}"
        )

        # 게임 종료 판정
        if st.session_state.user_wins == 3:
            st.session_state.game_over = True
            st.success("🎊 당신이 승리했습니다! 인간은 아직 끝나지 않았습니다.")
        elif st.session_state.computer_wins == 3:
            st.session_state.game_over = True
            st.error("💀 컴퓨터가 승리했습니다... 당신은 죽었습니다.")

# ----------------- 로그 출력 -----------------
st.markdown("---")
st.markdown("### 📝 전투 기록")
for log in reversed(st.session_state.battle_log):
    st.markdown(f"- {log}")

# ----------------- 현재 스코어 -----------------
if not st.session_state.game_over:
    st.markdown("---")
    st.markdown(f"👤 당신의 승수: **{st.session_state.user_wins}**")
    st.markdown(f"💻 컴퓨터의 승수: **{st.session_state.computer_wins}**")

# ----------------- 게임 종료 후 -----------------
else:
    if st.button("🔄 다시 시작하기"):
        st.session_state.user_wins = 0
        st.session_state.computer_wins = 0
        st.session_state.round = 0
        st.session_state.game_over = False
        st.session_state.battle_log = []
