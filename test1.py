import streamlit as st
import random
import base64
import requests

# ----------------- 설정 -----------------
st.set_page_config(page_title="죽은 추를 클릭하세요", layout="centered")
st.title("🐹 추를 클릭해보세요...")

# ----------------- 세션 상태 초기화 -----------------
if 'is_dead' not in st.session_state:
    st.session_state.is_dead = False
if 'death_count' not in st.session_state:
    st.session_state.death_count = 0
if 'last_will' not in st.session_state:
    st.session_state.last_will = ""
if 'play_sound' not in st.session_state:
    st.session_state.play_sound = False

# ----------------- 리소스 -----------------
alive_image_url = "https://raw.githubusercontent.com/gkswjdzz/imagecdn/main/chu_alive.png"
dead_image_url = "https://raw.githubusercontent.com/gkswjdzz/imagecdn/main/chu_dead.png"
sound_url = "https://github.com/gkswjdzz/imagecdn/raw/main/death_sound.mp3"

wills = [
    "내 최후의 말... 치즈는 냉장고 제일 아래칸에...",
    "난 사실 햄스터가 아니었어...",
    "형... 누나... 나 먼저 간다...",
    "누가 나 좀 살려줘...",
    "이럴 줄 알았으면 더 많이 놀걸...",
]

# ----------------- 사운드 재생 함수 -----------------
def play_sound_from_url(url):
    try:
        response = requests.get(url)
        b64 = base64.b64encode(response.content).decode()
        md = f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(md, unsafe_allow_html=True)
    except:
        st.warning("🎵 사운드 재생 실패!")

# ----------------- 버튼 처리 -----------------
col1, col2 = st.columns(2)

with col1:
    if st.button("💀 추 죽이기"):
        if not st.session_state.is_dead:
            st.session_state.is_dead = True
            st.session_state.death_count += 1
            st.session_state.last_will = random.choice(wills)
            st.session_state.play_sound = True
            st.rerun()

with col2:
    if st.button("❤️ 추 살리기"):
        if st.session_state.is_dead:
            st.session_state.is_dead = False
            st.session_state.last_will = ""
            st.rerun()

# ----------------- 화면 출력 -----------------
if st.session_state.is_dead:
    st.image(dead_image_url, caption="💀 추는 죽었습니다...", use_container_width=True)
    st.markdown(f"📝 **유언:** _{st.session_state.last_will}_")
    st.markdown(f"☠️ 총 죽인 횟수: `{st.session_state.death_count}`")
else:
    st.image(alive_image_url, caption="😊 추는 아직 살아있어요", use_container_width=True)

# ----------------- 사운드 출력 -----------------
if st.session_state.play_sound:
    play_sound_from_url(sound_url)
    st.session_state.play_sound = False
