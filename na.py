import streamlit as st
import random
import time

# 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "fish_pos" not in st.session_state:
    st.session_state.fish_pos = (random.randint(0, 4), random.randint(0, 4))
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# 게임 설정
TIME_LIMIT = 30  # 초

st.title("🎣 낚시 클릭 게임")
st.write("30초 동안 나타나는 물고기를 클릭해 잡으세요!")

# 시간 계산
elapsed = int(time.time() - st.session_state.start_time)
remaining = TIME_LIMIT - elapsed
if remaining <= 0:
    st.session_state.game_over = True

st.write(f"⏱️ 남은 시간: {max(0, remaining)}초")
st.write(f"🎯 점수: {st.session_state.score}")

# 물고기 그리기
cols = st.columns(5)
for i in range(5):
    with cols[i]:
        for j in range(5):
            if (i, j) == st.session_state.fish_pos and not st.session_state.game_over:
                if st.button("🐟", key=f"fish_{i}_{j}"):
                    st.session_state.score += 1
                    st.session_state.fish_pos = (random.randint(0, 4), random.randint(0, 4))
            else:
                st.write(" ")  # 공백 유지

# 게임 종료
if st.session_state.game_over:
    st.success(f"⏰ 게임 종료! 최종 점수: {st.session_state.score}점")
    if st.button("🔄 다시 시작"):
        st.session_state.score = 0
        st.session_state.start_time = time.time()
        st.session_state.fish_pos = (random.randint(0, 4), random.randint(0, 4))
        st.session_state.game_over = False
