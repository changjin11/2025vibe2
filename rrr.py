import streamlit as st
import random

# ---------- 페이지 설정 ----------
st.set_page_config(page_title="🎯 숫자 맞추기 게임", layout="centered")
st.title("🎯 숫자 맞추기 게임")
st.markdown("컴퓨터가 생각한 1부터 100 사이의 숫자를 맞혀보세요!")

# ---------- 상태 초기화 ----------
if "answer" not in st.session_state:
    st.session_state.answer = random.randint(1, 100)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "hint" not in st.session_state:
    st.session_state.hint = ""

# ---------- 게임 진행 ----------
if not st.session_state.game_over:
    guess = st.number_input("숫자를 입력하세요 (1~100)", min_value=1, max_value=100, step=1)

    if st.button("제출"):
        st.session_state.attempts += 1
        if guess == st.session_state.answer:
            st.success(f"🎉 정답입니다! {st.session_state.attempts}번 만에 맞췄어요!")
            st.session_state.game_over = True
        elif guess < st.session_state.answer:
            st.session_state.hint = "🔼 업! 더 큰 수예요."
        else:
            st.session_state.hint = "🔽 다운! 더 작은 수예요."

# ---------- 힌트 출력 ----------
if st.session_state.hint and not st.session_state.game_over:
    st.info(st.session_state.hint)

# ---------- 시도 횟수 표시 ----------
st.markdown(f"**시도 횟수:** {st.session_state.attempts}회")

# ---------- 재시작 ----------
if st.session_state.game_over:
    if st.button("🔄 다시 시작하기"):
        st.session_state.answer = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.session_state.hint = ""
