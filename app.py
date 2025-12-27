import streamlit as st
from game_logic import game_state, day1_choice, next_day

st.title("What's Left")

# Initialize game state in session
if "state" not in st.session_state:
    st.session_state.state = game_state.copy()

state = st.session_state.state

st.write(f"### Day {state['day']}")
st.write(f"**Current Balance:** ₹{state['balance']}")

#DAY 1 UI
st.markdown("---")

if state["day"] == 1:
    st.markdown("## 🗓️ Day 1 — Settling In")
    st.markdown(
        "> It’s the start of the week. You’re still finding your rhythm.\n\n"
        "> How do you handle your basic daily expenses?"
    )

    st.markdown("### ✨ Your Choices")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🪙 Basic Living\n₹800"):
            st.session_state.state = day1_choice(state, 1)
            next_day(st.session_state.state)
            st.experimental_rerun()

    with col2:
        if st.button("☕ Comfortable Start\n₹1200"):
            st.session_state.state = day1_choice(state, 2)
            next_day(st.session_state.state)
            st.experimental_rerun()

    with col3:
        if st.button("🎉 Small Treat\n₹1500"):
            st.session_state.state = day1_choice(state, 3)
            next_day(st.session_state.state)
            st.experimental_rerun()



