# 🐢 Jennette’s Pier — Easy Renewables Quiz

An interactive, kid-friendly **renewable energy and sustainability quiz** built with [Streamlit](https://streamlit.io/).  
Features **multiple-choice questions**, **read-aloud narration**, and **encouraging feedback**.

Designed to teach all ages about renewable energy, ocean sustainability, and local eco-initiatives like **Jennette’s Pier’s wastewater reuse system** in Manteo, NC.

---

## 🌟 Features

- **Simple, accessible questions** for all ages  
- **Narration options** via browser text-to-speech (Web Speech API)  
- **Positive feedback** for correct and incorrect answers  
- **Automatic restart** (kiosk mode)  
- **Customizable question bank** in Python  


---

🚀 Getting Started

1. Clone the repository
git clone https://github.com/YOUR-USERNAME/renewables-quiz.git

2. Install dependencies
pip install streamlit

3. Run the quiz
streamlit run app.py

---
🗂 Project Structure
├── app.py # Main Streamlit app
├── README.md # Project documentation (this file)
---
🎯 How It Works
Question Bank

Questions are stored in a Python list called BANK inside app.py.
Each question is a dictionary with:
--**id-unique string indentifier**
--**question-the text shown to the player**
--**choices-list of answer options**
--**answer_idx**-index of the correct choice
--**explain**-short educational explanation
--**rationales-reasons for each possible answer**

---
**Read-Aloud Feature**
Use the browser's Web Speech API to read question and answer cloud.
---
Kiosk Mode
Auto-restarts when all questions have been answered(this is good for exhibits)
---
📝 Customizing Questions
1. Open app.py in code editor
2. Scroll to the BANK list.
3. Add, edit, or remove question dictionaries.
4. Save and rerun:
streamlit run app.py
---
📜 Acknowledgements

This material is based upon work supported by the National Science Foundation under grant no. DGE-2125684.
Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.

<img width="720" height="231" alt="image" src="https://github.com/user-attachments/assets/3aa8b687-9abd-4cd6-a8d5-238d1979caf6" />

