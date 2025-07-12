# 🎵 Seq2Sound: 피보나치 수열을 음악으로!

> 수학과 음악의 만남. 피보나치 수열을 들어보세요!

<img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python">
<img src="https://img.shields.io/badge/Streamlit-1.0+-brightgreen?logo=streamlit">
<img src="https://img.shields.io/badge/MIDI-Music-yellow?logo=musicbrainz">

---

## 📌 소개

**Seq2Sound**는 피보나치 수열을 기반으로 음을 생성하고,  
그 수열을 MIDI 형식의 음악으로 바꾸어 **직접 들어볼 수 있는 웹앱**입니다.  
Streamlit으로 구현되어 간편하게 웹에서 실행할 수 있어요!

---

## 🎥 데모 화면

<img src="https://github.com/사용자ID/프로젝트명/assets/00000000/demo.gif" width="600">

---

## 🧠 작동 원리

1. 사용자가 피보나치 수열의 항 개수를 지정
2. 각 숫자를 음 높이로 매핑 (예: 60 + n % 24 → C4 이상 음)
3. `pretty_midi` 라이브러리를 사용해 MIDI 음악 생성
4. Streamlit에서 바로 재생

---

## 🚀 설치 및 실행

### 1. 클론하기

```bash
git clone https://github.com/사용자ID/seq2sound.git
cd seq2sound
