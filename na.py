# 캐릭터 라인 출력
with st.form("chu_click_form"):
    # 캐릭터 이모지 준비
    chu_emoji = "🦍" if st.session_state.is_mega_chu else "🐷"
    heart = ""
    if st.session_state.is_married:
        heart_stage = heart_stages[min(st.session_state.honeymoon_level, 3)]
        heart_size = 40 + st.session_state.honeymoon_level * 10
        heart = f"<span style='font-size: {heart_size}px;'>{heart_stage}</span>"

    jeon = "🧑" if st.session_state.has_jeon else ""
    park = "<span style='font-size: 40px;'>👶 박</span>" if st.session_state.is_married else ""

    # 가로 정렬된 캐릭터 줄 출력
    st.markdown(f"""
        <div style='display: flex; justify-content: center; align-items: center; gap: 20px; margin-top: 30px; font-size: 100px;'>
            <button type="submit" style="all: unset; cursor: pointer;">{chu_emoji}</button>
            {heart}
            {jeon and f"<button type='submit' style='all: unset; cursor: pointer;'>{jeon}</button>"}
            {park}
        </div>
    """, unsafe_allow_html=True)

    # 클릭 처리
    submitted = st.form_submit_button()
    if submitted:
        gain = random.randint(100, 500)
        st.session_state.money += gain

        # 대사 처리
        if st.session_state.is_married:
            st.session_state.last_quote = f"💖 <i>{random.choice(love_quotes)}</i>"
        elif st.session_state.is_mega_chu:
            st.session_state.last_quote = f"🦍 <i>{random.choice(scolding_quotes)}</i>"
        else:
            st.session_state.last_quote = f"🐽 <i>{random.choice(beg_quotes)}</i>"

        # 전 추가 수익
        if st.session_state.has_jeon:
            st.session_state.money += gain // 2
