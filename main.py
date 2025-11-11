import streamlit as st
from gtts import gTTS
from io import BytesIO

# ✅ Page setup
st.set_page_config(page_title="Free TTS Web App", page_icon="🗣️")

# ✅ Title & description
st.title("🗣️ Free Text-to-Speech (TTS) Web App")
st.write("Type your text below and convert it into speech for free!")

# ✅ Input area
text = st.text_area("Enter your text:", height=200, placeholder="Type or paste text here...")

# ✅ Language selector
lang = st.selectbox("Select language:", ["en", "ur", "hi", "fr", "de"])

# ✅ Convert button
if st.button("🎧 Convert to Speech"):
    if text.strip():
        try:
            # Convert text to speech
            tts = gTTS(text=text, lang=lang)
            audio_fp = BytesIO()
            tts.write_to_fp(audio_fp)
            audio_fp.seek(0)

            # Play & download
            st.success("✅ Conversion successful!")
            st.audio(audio_fp, format="audio/mp3")
            st.download_button(
                label="⬇️ Download Audio",
                data=audio_fp,
                file_name="tts_output.mp3",
                mime="audio/mp3"
            )

        except Exception as e:
            # Error handling
            st.error(f"⚠️ An error occurred during conversion:\n\n{e}")
            st.info("💡 Try again after checking your internet connection or input text.")

    else:
        st.warning("Please enter some text before converting!")

# ✅ Footer
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit and Google Text-to-Speech (gTTS)")
