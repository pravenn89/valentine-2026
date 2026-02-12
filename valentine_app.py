import streamlit as st
import os
import base64
from pathlib import Path
import random

# 1. Page Config
st.set_page_config(page_title="My Forever Valentine", page_icon="❤️", layout="centered")

# 2. Paths
BASE_PATH = Path(__file__).parent 
folders = ["Starting", "Understanding", "Complete Family"]
audio_path = BASE_PATH / "song.mp3"

# 3. CSS for Styling
st.markdown("""
    <style>
    /* Clean Mobile Look */
    .stApp { background-color: #fffafa; }
    
    /* Remove Sidebar */
    [data-testid="stSidebar"] { display: none; }
    
    /* Headers */
    h1, h2, h3 { color: #d62828; text-align: center; font-family: 'Arial', sans-serif; }
    p { font-size: 18px; color: #4a4a4a; line-height: 1.6; }
    
    /* Chapter Dividers */
    .divider { 
        margin-top: 50px; 
        margin-bottom: 50px; 
        border-top: 2px dashed #ffccd5; 
    }
    
    /* Image Styling */
    img { border-radius: 15px; margin-bottom: 15px; }
    
    /* Password Box */
    .unaudited-box {
        background-color: #fff0f3; 
        padding: 20px; 
        border-left: 5px solid #ff4d6d;
        border-radius: 10px; 
        font-style: italic; 
        text-align: center; 
        color: #d62828; 
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 4. Session State
if 'started' not in st.session_state:
    st.session_state.started = False

# --- AUDIO PLAYER FUNCTION ---
def autoplay_audio(file_path):
    if file_path.exists():
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            # Visible Audio Player (Most reliable for mobile)
            st.markdown(f"""
                <div style="position: sticky; top: 0; z-index: 1000; background-color: #fffafa; padding: 10px; text-align: center; border-bottom: 1px solid #ffccd5;">
                    <audio controls autoplay loop style="width: 100%; border-radius: 20px;">
                        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                    </audio>
                    <small style="color: #e63946;">Tap play if music doesn't start automatically 🎵</small>
                </div>
            """, unsafe_allow_html=True)

# --- VIEW 1: THE PROPOSAL ---
if not st.session_state.started:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.title("Will you be my Valentine forever? ❤️")
    
    col1, col2, col3 = st.columns([1, 5, 1])
    with col2:
        if st.button("YES! 😍", type="primary", use_container_width=True):
            st.session_state.started = True
            st.rerun()
        
        st.write("") # Spacer
        
        # Jumping No Button (Simulated with columns)
        r1, r2, r3 = st.columns([random.randint(1, 3), 2, random.randint(1, 3)])
        with r2:
            if st.button("No ❌"):
                st.rerun()

# --- VIEW 2: THE FULL STORY (One Long Scroll) ---
else:
    # 1. Start Music (Stays at top)
    autoplay_audio(audio_path)
    
    st.balloons()
    
    # 2. Intro
    st.markdown("<h1 style='font-size: 3rem;'>Our Beautiful Journey ❤️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Scroll down to relive our memories...</p>", unsafe_allow_html=True)
    
    # 3. Loop through Folders (Vertical Story)
    timeline_years = ["2021 - 2022", "2023 - 2024", "2025 onwards"]
    
    for idx, folder in enumerate(folders):
        st.markdown(f"<div class='divider'></div>", unsafe_allow_html=True)
        
        # Chapter Header
        st.markdown(f"## Chapter {idx+1}: {folder}")
        st.markdown(f"<h4 style='text-align:center; color:gray;'><i>{timeline_years[idx]}</i></h4>", unsafe_allow_html=True)
        
        # Images
        folder_path = BASE_PATH / folder
        if folder_path.exists():
            images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            for img in images:
                st.image(str(folder_path / img), use_container_width=True)
        else:
            st.warning(f"Please check folder name: {folder}")

    # 4. Final Message
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.title("MY FOREVER VALENTINE")
    
    st.markdown("""
    <div style="background:#fff0f3; padding:20px; border-radius:15px; text-align:center; color:#4a4a4a;">
        Happy Valentine’s Day to the woman who holds our world together. <br><br>
        Watching you as a mother this past year has only made me fall deeper in love with you. 
        You are my best friend, my partner, and my home.
    </div>
    """, unsafe_allow_html=True)
    
    # 5. Password Section
    st.write("---")
    st.subheader("🔒 A Private Message")
    pw = st.text_input("Enter engagement date (ddmmyyyy):", type="password")
    
    if pw == "19092021":
        st.success("Access Granted! ❤️")
        st.markdown("""
        <div class="unaudited-box">
            Roses are red, violets are blue, I’ve got some very 'unaudited' plans for me and you. <br>
            Tonight, let's forget about the spreadsheets and just focus on the bedsheets. <br>
            Can’t wait to have you all to myself.
        </div>
        """, unsafe_allow_html=True)
    elif pw != "":
        st.error("Incorrect Password.")
        
    st.markdown("<br><br>", unsafe_allow_html=True)