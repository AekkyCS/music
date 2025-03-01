import streamlit as st
import time

def display_lyrics(display_time=2, fade_time=0.5):
    lyrics = [
        "Flashback when you met me",
        "Your buzzcut and my hair bleached",
        "Even in my worst times",
        "You could see the best of me",
        "Flashback to my mistakes",
        "My rebounds, my earthquakes",
        "Even in my worst lies",
        "You saw the truth in me",
        "And I woke up just in time",
        "Now I wake up by your side",
        "My one and only, my lifeline",
        "I woke up just in time",
        "Now I wake up by your side",
        "My hands shake, I can't explain this ah, ha, ha, ha"
    ]
    
    lyric_placeholder = st.empty()
    
    for line in lyrics:
        # Fade in effect
        for opacity in range(0, 101, 10):
            fade_in_text = f"""
            <div style='display: flex; justify-content: center; align-items: center; height: 80vh;'>
                <h1 style='text-align: center; font-size: 50px; opacity: {opacity / 100};'>{line}</h1>
            </div>
            """
            lyric_placeholder.markdown(fade_in_text, unsafe_allow_html=True)
            time.sleep(fade_time / 10)
        
        time.sleep(display_time)
        
        # Fade out effect
        for opacity in range(100, -1, -10):
            fade_out_text = f"""
            <div style='display: flex; justify-content: center; align-items: center; height: 80vh;'>
                <h1 style='text-align: center; font-size: 50px; opacity: {opacity / 100};'>{line}</h1>
            </div>
            """
            lyric_placeholder.markdown(fade_out_text, unsafe_allow_html=True)
            time.sleep(fade_time / 10)
        
        lyric_placeholder.empty()  # Clear the previous lyric before displaying the next one
        time.sleep(0.5)  # Short pause between lyrics
    
    st.stop()  # End the Streamlit app after showing all lyrics

# Display the lyrics immediately when the page loads (no button, no prompt)
display_lyrics(display_time=1.2, fade_time=0.1)
