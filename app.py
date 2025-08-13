# Jeannette’s Pier — Easy Renewables Quiz (MCQ + Read Aloud + Encouraging Feedback)
# Designed for Streamlit Community Cloud.

import json
import random
import streamlit as st

# -----------------------------
# Page & sidebar
# -----------------------------
st.set_page_config(page_title="Jeannette’s Pier — Easy Renewables Quiz", page_icon="🐢", layout="centered")

st.sidebar.header("Settings")
READ_ALOUD = st.sidebar.checkbox("Enable read-aloud (Web Speech API)", value=True)
NARRATION = st.sidebar.selectbox("Narration style", ["Default", "British documentary"])
AUTO_LOOP = st.sidebar.checkbox("Auto-restart when finished (kiosk)", value=True)

# Banner image (URL or local file path) — using your requested ocean image by default
DEFAULT_IMAGE = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAkhVFay0GLD0oveg4nVgUiSS-vPVmY1MJrg&s"
image_src = st.sidebar.text_input("Banner image (URL or local path)", value=DEFAULT_IMAGE)

# Minimal styles
st.markdown(
    """
<style>
.quiz-option { padding:.65rem .85rem; border:2px solid #ddd; border-radius:12px; margin:.4rem 0; }
.correct { border-color:#1b5e20 !important; background:#eaf7ea; }
.incorrect { border-color:#b71c1c !important; background:#ffebee; }
.header h1 { color:#0f766e; margin:.25rem 0; }
.small { font-size:.95rem; color:#5a5a5a; }
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Header
# -----------------------------
st.image(image_src, caption="Jeannette’s Pier exhibit banner (alt: ocean scene)", use_column_width=True)
st.markdown(
    "<div class='header'><h1>Jeannette’s Pier — Easy Renewables Quiz</h1>"
    "<p class='small'>Multiple choice • Read-aloud • Encouraging feedback</p></div>",
    unsafe_allow_html=True,
)

# -----------------------------
# Read-aloud helper (browser TTS)
# -----------------------------
def speak(text: str):
    if not READ_ALOUD or not text:
        return
    prefer_lang = "en-GB" if NARRATION == "British documentary" else "en"
    st.components.v1.html(
        f"""
        <script>
          function pickVoice(preferLang) {{
            const voices = window.speechSynthesis.getVoices();
            if (!voices || voices.length === 0) return null;
            let v = voices.find(v => v.lang && v.lang.toLowerCase().startsWith(preferLang.toLowerCase()));
            if (v) return v;
            return voices.find(v => v.lang && v.lang.toLowerCase().startsWith('en'));
          }}
          function speakNow(txt, preferLang) {{
            const u = new SpeechSynthesisUtterance(txt);
            u.rate = 1.0; u.pitch = 1.0; u.volume = 1.0;
            const trySpeak = () => {{
              const v = pickVoice(preferLang);
              if (v) u.voice = v;
              window.speechSynthesis.cancel();
              window.speechSynthesis.speak(u);
            }};
            const voices = window.speechSynthesis.getVoices();
            if (!voices || voices.length === 0) {{
              window.speechSynthesis.onvoiceschanged = () => trySpeak();
            }} else {{
              trySpeak();
            }}
          }}
          speakNow({json.dumps(text)}, {json.dumps(prefer_lang)});
        </script>
        """,
        height=0,
    )

# -----------------------------
# Your EASY question bank (from your last message)
# -----------------------------
BANK = [
    {
        "id": "what_uses_wind",
        "question": "What does a wind turbine use to make electricity?",
        "choices": [
            "The wind blowing on its blades",
            "Gasoline in a tank",
            "Batteries from your phone",
            "Lightning bolts"
        ],
        "answer_idx": 0,
        "explain": "Wind pushes the blades, which turn a generator to make electricity.",
        "rationales": [
            "Correct — moving air spins the blades!",
            "That would be a gas generator, not a wind turbine.",
            "Batteries store energy; they don’t generate it here.",
            "Lightning is powerful, but not how turbines work."
        ],
    },
    {
        "id": "which_is_renewable",
        "question": "Which of these is a renewable energy source?",
        "choices": ["Wind", "Coal", "Gasoline", "Oil"],
        "answer_idx": 0,
        "explain": "Wind keeps blowing and doesn’t run out — that’s why it’s renewable.",
        "rationales": [
            "Correct — wind is renewable.",
            "Coal is a fossil fuel; it takes millions of years to form.",
            "Gasoline is made from oil; it’s not renewable.",
            "Oil is a fossil fuel, not renewable."
        ],
    },
    {
        "id": "renewable_energy",
        "question": "What is renewable energy?",
        "choices": [
            "Energy that comes from sources that can be replaced naturally",
            "Energy that will run out soon",
            "Energy made only by machines",
            "Energy stored in batteries forever"
        ],
        "answer_idx": 0,
        "explain": "Renewable energy comes from sources like sunlight, wind, and water that are naturally replenished over time.",
        "rationales": [
            "Correct — renewable energy is made from sources that naturally replenish.",
            "Incorrect — that describes nonrenewable energy like coal or oil.",
            "Incorrect — machines can make any kind of energy, not just renewable.",
            "Incorrect — batteries store energy but do not create renewable energy."
        ],
    },
    {
        "id": "olympic_surfing",
        "question": "Which Olympic sport relies on waves of ocean energy?",
        "choices": ["Surfing", "Swimming", "Rowing", "Sailing"],
        "answer_idx": 0,
        "explain": "Surfing is an Olympic sport where athletes ride waves created by ocean energy.",
        "rationales": [
            "Correct — surfing depends directly on the motion of ocean waves.",
            "Incorrect — swimming happens in still or pool water, not on waves.",
            "Incorrect — rowing uses human power, not ocean wave energy.",
            "Incorrect — sailing uses wind power, not the energy of ocean waves."
        ],
    },
    {
        "id": "solar_power_benefit",
        "question": "What’s one big benefit of using solar power?",
        "choices": [
            "It makes clean energy",
            "It smells nice",
            "It keeps the Sun warm",
            "It repels insects"
        ],
        "answer_idx": 0,
        "explain": "Solar power is a renewable energy source that produces clean electricity without creating pollution.",
        "rationales": [
            "Correct — solar power makes clean energy from sunlight without harmful emissions.",
            "Incorrect — solar power has no special smell.",
            "Incorrect — the Sun stays warm on its own, no help needed!",
            "Incorrect — solar panels do not repel insects."
        ],
    },
    {
        "id": "renewable_environment_help",
        "question": "How does renewable energy help the environment?",
        "choices": [
            "It makes less pollution",
            "It makes more trash",
            "It makes the air dirty",
            "It makes the oceans smaller"
        ],
        "answer_idx": 0,
        "explain": "Renewable energy, like solar and wind power, makes electricity without creating dirty smoke or harmful waste.",
        "rationales": [
            "Correct — renewable energy makes less pollution, which keeps air and water cleaner.",
            "Incorrect — it does not make more trash.",
            "Incorrect — it helps make the air cleaner, not dirtier.",
            "Incorrect — it does not change the size of the oceans."
        ],
    },
    {
        "id": "renewable_community_help",
        "question": "How does renewable energy help your community?",
        "choices": [
            "It can create new jobs",
            "It makes the streets turn green",
            "It makes houses float",
            "It teaches birds to fly"
        ],
        "answer_idx": 0,
        "explain": "Building and using renewable energy like solar panels and wind turbines can create jobs for people in the community.",
        "rationales": [
            "Correct — renewable energy can create jobs for workers in the community.",
            "Incorrect — it does not paint the streets green.",
            "Incorrect — it does not make houses float.",
            "Incorrect — birds already know how to fly!"
        ],
    },
    {
        "id": "jennettes_pier_wastewater",
        "question": "How does Jennette’s Pier take care of dirty water so it’s safe and helps save water?",
        "choices": [
            "They clean and reuse water for toilets",
            "They pour it into the ocean without cleaning",
            "They throw it on the beach",
            "They mix it with juice"
        ],
        "answer_idx": 0,
        "explain": "Jennette’s Pier has a special system that cleans wastewater and uses the recycled water to flush toilets, helping to reduce the town’s water use.",
        "rationales": [
            "Correct — the pier cleans its used water and reuses it in toilets, saving a lot of clean water.",
            "Incorrect — they don’t send dirty water into the ocean without treatment.",
            "Incorrect — they don’t dump it on the beach.",
            "Incorrect — they definitely don’t mix wastewater with juice!"
        ],
    },
]

# -----------------------------
# Session state (robust next/skip)
# -----------------------------
if "order" not in st.session_state:
    st.session_state.order = random.sample(range(len(BANK)), k=len(BANK))
if "idx" not in st.session_state:
    st.session_state.idx = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "graded" not in st.session_state:
    st.session_state.graded = False
if "last_choice" not in st.session_state:
    st.session_state.last_choice = None

total = len(BANK)
i = st.session_state.idx

# Finish screen / auto-loop
if i >= total:
    st.success(f"Quiz complete! Score: {st.session_state.score} / {total}")
    if AUTO_LOOP:
        st.session_state.order = random.sample(range(len(BANK)), k=len(BANK))
        st.session_state.idx = 0
        st.session_state.score = 0
        st.session_state.graded = False
        st.rerun()
    st.stop()

q = BANK[st.session_state.order[i]]

# -----------------------------
# Read-aloud controls & question
# -----------------------------
c1, c2, c3 = st.columns([1, 1, 1])
with c1:
    if st.button("🔊 Read question", key=f"rq_{i}"):
        speak(q["question"])
with c2:
    if st.button("🔊 Read choices", key=f"rc_{i}"):
        speak("Choices: " + "; ".join(q["choices"]))
with c3:
    if st.button("Skip / Next →", key=f"skip_{i}"):
        st.session_state.graded = False
        st.session_state.last_choice = None
        st.session_state.idx += 1
        st.rerun()

st.subheader(f"Question {i+1} of {total}")
st.markdown(f"**{q['question']}**")

# Start unselected (placeholder)
choices_with_placeholder = ["-- Select an answer --"] + q["choices"]
raw_idx = st.radio(
    "Select your answer:",
    options=list(range(len(choices_with_placeholder))),
    format_func=lambda j: choices_with_placeholder[j],
    index=0,
    key=f"choices_{i}"
)
choice_idx = None if raw_idx == 0 else raw_idx - 1

# -----------------------------
# Submit / feedback / Next
# -----------------------------
submit = st.button("Submit", type="primary", disabled=(choice_idx is None), key=f"submit_{i}")

if submit and choice_idx is not None:
    st.session_state.graded = True
    st.session_state.last_choice = choice_idx
    correct = (choice_idx == q["answer_idx"])

    # Visual feedback list
    for j, text in enumerate(q["choices"]):
        klass = "correct" if j == q["answer_idx"] else ("incorrect" if j == choice_idx else "")
        st.markdown(f"<div class='quiz-option {klass}'><strong>{chr(65+j)}.</strong> {text}</div>", unsafe_allow_html=True)

    if correct:
        st.success("✅ Correct! Great job!")
        speak("Correct. Great job!")
        st.session_state.score += 1
    else:
        st.info("💪 Nice effort! Here’s a helpful tip:")
        st.warning(f"Why that choice isn’t the best: {q['rationales'][choice_idx]}")
        st.info(f"Key idea: {q['explain']}")
        speak("Nice effort. Here's a helpful tip. " + q["explain"])

    if st.button("Next →", key=f"next_{i}"):
        st.session_state.graded = False
        st.session_state.last_choice = None
        st.session_state.idx += 1
        st.rerun()

elif not st.session_state.graded:
    # Neutral list before grading
    for j, text in enumerate(q["choices"]):
        st.markdown(f"- {text}")
else:
    # Already graded but not advanced yet — keep showing feedback and a persistent Next
    choice_idx = st.session_state.last_choice
    for j, text in enumerate(q["choices"]):
        klass = "correct" if j == q["answer_idx"] else ("incorrect" if j == choice_idx else "")
        st.markdown(f"<div class='quiz-option {klass}'><strong>{chr(65+j)}.</strong> {text}</div>", unsafe_allow_html=True)
    if st.button("Next →", key=f"next_repeat_{i}"):
        st.session_state.graded = False
        st.session_state.last_choice = None
        st.session_state.idx += 1
        st.rerun()

# -----------------------------
# Sidebar scoreboard
# -----------------------------
st.sidebar.markdown("---")
st.sidebar.subheader("Score")
st.sidebar.metric("Correct", f"{st.session_state.score}")
st.sidebar.metric("Question", f"{i+1} / {total}")
