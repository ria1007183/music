import streamlit as st
from utils import generate_fibonacci
from sequence_to_midi import sequence_to_midi

st.set_page_config(page_title="Fibonacci Sound Generator", layout="centered")

st.title("🎼 피보나치 수열을 음악으로!")

st.markdown("""
수열을 소리로 들어볼 수 있는 웹앱입니다.  
아래에서 피보나치 수열 항의 개수를 선택하면 자동으로 음악이 생성됩니다.
""")

n = st.slider("피보나치 항 개수 선택 (최대 30)", min_value=5, max_value=30, value=10)

if st.button("🎵 음악 생성 및 재생"):
    seq = generate_fibonacci(n)
    st.write("🔢 생성된 수열:", seq)

    midi_file = sequence_to_midi(seq)
    with open(midi_file, "rb") as f:
        st.audio(f.read(), format="audio/midi")

    st.success("🎶 음악이 생성되었습니다!")
