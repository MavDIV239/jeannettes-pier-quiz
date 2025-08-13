# 🐢 Jennette’s Pier — Easy Renewables Quiz

An interactive, kid-friendly **renewable energy and sustainability quiz** built with [Streamlit](https://streamlit.io/).  
Features a **sea turtle theme**, **multiple-choice questions**, **read-aloud narration** (including a *British documentary* voice option), and **encouraging feedback**.

Designed to teach all ages about renewable energy, ocean sustainability, and local eco-initiatives like **Jennette’s Pier’s wastewater reuse system** in Manteo, NC.

---

## 🌟 Features

- **Simple, accessible questions** for all ages  
- **Narration options** via browser text-to-speech (Web Speech API)  
- **Positive feedback** for correct and incorrect answers  
- **Automatic restart** (kiosk mode)  
- **Customizable question bank** in Python  
- **Sea turtle image** for a friendly, educational vibe  

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/renewables-quiz.git
cd renewables-quiz

### 2. Install dependencies
pip install streamlit

### Run the Quiz
streamlit run app.py

---
🗂 Project Structure
.
├── app.py          # Main Streamlit app
├── README.md       # Project documentation (this file)
└── requirements.txt# Python dependencies (optional)
---
🎯 How It Works

Question Bank
Questions are stored in a Python list called BANK inside app.py.
Each question is a dictionary with:
* id – unique string identifier
* question – the text shown to the player
* choices – list of answer options
* answer_idx – index of the correct choice
* explain – short educational explanation
* rationales – reasons for each possible answer
---
Read-Aloud Feature
Uses the browser's Web Speech API to read questions and answers aloud.
Includes an optional British documentary style narration.
---
Kiosk Mode
Auto-restarts when all questions have been answered (good for exhibits).
---
📝 Customizing Questions
Open app.py in a code editor.
Scroll to the BANK list.
Add, edit, or remove question dictionaries.
Save and rerun streamlit run app.py.

