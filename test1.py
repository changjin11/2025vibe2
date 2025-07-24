import streamlit as st
import random
import base64
import os

# ----------------- 설정 -----------------
st.set_page_config(page_title="죽은 추를 클릭하세요", layout="centered")
st.title("🐹 추를 클릭해보세요...")

# 세션 상태 초기화
if 'is_dead' not in st.session_state:
    st.session_state.is_dead = False
if 'death_count' not in st.session_state:
    st.session_state.death_count = 0
if 'last_will' not in st.session_state:
    st.session_state.last_will = ""
if 'play_sound' not in st.session_state:
    st.session_state.play_sound = False  # 사운드 재생 여부

# 유언 리스트
wills = [
    "내 최후의 말... 치즈는 냉장고 제일 아래칸에...",
    "난 사실 햄스터가 아니었어...",
    "형... 누나... 나 먼저 간다...",
    "누가 나 좀 살려줘...",
    "이럴 줄 알았으면 더 많이 놀걸...",
]

# 이미지 경로
alive_image_path = "chu_alive.png"
dead_image_path = "chu_dead.png"
sound_path = "death_sound.mp3"

# ----------------- 사운드 재생 함수 -----------------
def play_sound(sound_file):
    if not os.path.exists(sound_file):
        st.warning("🎵 사운드 파일이 없습니다. death_sound.mp3를 같은 폴더에 넣어주세요.")
        return

    with open(sound_file, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
        <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(md, unsafe_allow_html=True)

# ----------------- 메인 로직 -----------------

# 상태: 죽음
if st.session_state.is_dead:
    if os.path.exists(dead_image_path):
        st.image(dead_image_path, caption="💀 추는 죽었습니다...", use_column_width=True)
    else:
        st.error("❌ dead 이미지가 없습니다: chu_dead.png")

    st.markdown(f"📝 **유언:** _{st.session_state.last_will}_")
    st.markdown(f"☠️ 총 죽인 횟수: `{st.session_state.death_count}`")

    if st.button("🔄 다시 살리기"):
        st.session_state.is_dead = False
        st.session_state.last_will = ""

# 상태: 살아있음
else:
    if st.button("🐹 추를 클릭해서 죽이기"):
        st.session_state.is_dead = True
        st.session_state.death_count += 1
        st.session_state.last_will = random.choice(wills)
        st.session_state.play_sound = True

    if os.path.exists(alive_image_path):
        st.image(alive_image_path, caption="😊 추는 아직 살아있어요", use_column_width=True)
    else:
        st.error("❌ alive 이미지가 없습니다: chu_alive.png")

# 사운드 재생 (딜레이를 주기 위해 최하단에서 실행)
if st.session_state.play_sound:
    play_sound(sound_path)
    st.session_state.play_sound = False  # 재생 후 초기화

