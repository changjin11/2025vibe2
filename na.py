import streamlit as st
import random
import time
from streamlit_autorefresh import st_autorefresh

# 자동 새로고침 (1초마다)
st_autorefresh(interval=1000, key="auto_refresh")

# 게임 설정
TIME_LIMIT = 30
FISH_LIFESPAN = 1.5

# 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "fish_pos" not in st.session_state:
    st.session_state.fish_pos = (random.randint(0, 4), random.randint(0, 4))
if "fish_spawn_time" not in st.session_state:
    st.session_state.fish_spawn_time = time.time()
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# 시간 확인
now = time.time()
elapsed = int(now - st.session_state.start_time)
remaining = TIME_LIMIT - elapsed

# 게임 종료 처리
if remaining <= 0:
    st.session_state.game_over = True

# 물고기 시간 초과 시 재배치
if not st.session_state.game_over and now - st.session_state.fish_spawn_time > FISH_LIFESPAN:
    st.session_state.fish_pos = (random.randint(0, 4), random.randint(0, 4))
    st.session_state.fish_spawn_time = now

# 게임 UI
st.title("🎣 낚시 클릭 게임")
st.write(f"⏱ 남은 시간: {max(0, remaining)}초")
st.write(f"🎯 점수: {st.session_state.score}")

cols = st.columns(5)
clicked = False

# 물고기 출력 및 클릭 처리
for i in range(5):
    with cols[i]:
        for j in range(5):
            if (i, j) == st.session_state.fish_pos and not st.session_state.game_over:
                if st.button("🐟", key=f"fish_{i}_{j}_{elapsed}"):
                    st.session_state.score += 1
                    st.session_state.fish_pos = (random.randint(0, 4), random.randint(0, 4))
                    st.session_state.fish_spawn_time = time.time()
                    clicked = True
            else:
                st.write(" ")  # 빈 공간 채우기

# 게임 종료 UI
if st.session_state.game_over:
    st.success(f"게임 종료! 🎉 최종 점수: {st.session_state.score}점")
    if st.button("🔄 다시 시작"):
        st.session_state.score = 0
        st.session_state.start_time = time.time()
        st.session_state.fish_spawn_time = time.time()
        st.session_state.fish_pos = (random.randint(0, 4), random.randint(0, 4))
        st.session_state.game_over = False
