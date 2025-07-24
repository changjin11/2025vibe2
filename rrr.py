import streamlit as st
import random

# ----------------- 설정 -----------------
st.set_page_config(page_title="가위바위보 대결!", layout="centered")
st.title("✊ ✌️ ✋ 가위바위보 대결!")
st.markdown("컴퓨터와 대결해보세요!")

# ----------------- 세션 상태 초기화 -----------------
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0
if "draw_count" not in st.session_state:
    st.session_state.draw_count = 0
if "last_result" not in st.session_state:
    st.session_state.last_result = ""

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

# ----------------- 버튼 UI -----------------
st.subheader("당신의 선택은?")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✌️ 가위"):
        user_choice = "가위"
        computer_choice = random.choice(choices)
        result = get_result(user_choice, computer_choice)
        st.session_state.last_result = (user_choice, computer_choice, result)
        if result == "승리":
            st.session_state.user_score += 1
        elif result == "패배":
            st.session_state.computer_score += 1
        else:
            st.session_state.draw_count += 1

with col2:
    if st.button("✊ 바위"):
        user_choice = "바위"
        computer_choice = random.choice(choices)
        result = get_result(user_choice, computer_choice)
        st.session_state.last_result = (user_choice, computer_choice, result)
        if result == "승리":
            st.session_state.user_score += 1
        elif result == "패배":
            st.session_state.computer_score += 1
        else:
            st.session_state.draw_count += 1

with col3:
    if st.button("✋ 보"):
        user_choice = "보"
        computer_choice = random.choice(choices)
        result = get_result(user_choice, computer_choice)
        st.session_state.last_result = (user_choice, computer_choice, result)
        if result == "승리":
            st.session_state.user_score += 1
        elif result == "패배":
            st.session_state.computer_score += 1
        else:
            st.session_state.draw_count += 1

# ----------------- 결과 출력 -----------------
if st.session_state.last_result:
    user, computer, result = st.session_state.last_result
    st.markdown("### 🧾 결과")
    st.markdown(f"당신: {emoji[user]} **{user}**")
    st.markdown(f"컴퓨터: {emoji[computer]} **{computer}**")
    if result == "승리":
        st.success("🎉 당신이 이겼습니다!")
    elif result == "패배":
        st.error("😥 컴퓨터에게 졌어요...")
    else:
        st.info("😐 무승부입니다.")

# ----------------- 점수판 -----------------
st.markdown("---")
st.markdown("### 📊 현재 점수")
st.markdown(f"👤 당신: {st.session_state.user_score}승")
st.markdown(f"💻 컴퓨터: {st.session_state.computer_score}승")
st.markdown(f"⚖️ 무승부: {st.session_state.draw_count}회")

# ----------------- 초기화 버튼 -----------------
if st.button("🔄 점수 초기화"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.draw_count = 0
    st.session_state.last_result = ""
