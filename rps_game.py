import streamlit as st
import random

st.set_page_config(page_title="Rock-Paper-Scissors", page_icon="🎮", layout="centered")

st.title("🎮 Rock-Paper-Scissors Game")
st.markdown("#### Select your move:")

options = ["Rock", "Paper", "Scissors"]
user_choice = st.radio("", options, horizontal=True)

if "user_score" not in st.session_state:
    st.session_state.user_score = 0
    st.session_state.computer_score = 0

if st.button("Play"):
    computer_choice = random.choice(options)

    result = ""
    if user_choice == computer_choice:
        result = "😐 It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "✅ You Win!"
        st.session_state.user_score += 1
    else:
        result = "❌ Computer Wins!"
        st.session_state.computer_score += 1

    st.markdown(f"**You chose:** {user_choice}  \n**Computer chose:** {computer_choice}")
    st.markdown(f"### {result}")
    st.success(f"Score ➤ You: {st.session_state.user_score} | Computer: {st.session_state.computer_score}")

if st.button("Reset Game"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.info("Game reset! Scores cleared.")
