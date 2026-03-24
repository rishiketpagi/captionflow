import streamlit as st
import os
from video_utils import extract_audio_from_video
from transcriber import transcribe_audio
from subtitle_generator import generate_srt

st.set_page_config(page_title="AI Subtitle Generator", page_icon="🎬", layout="wide")

st.title("🎬 AI Video Subtitle Generator")
st.markdown("Generate subtitles automatically from uploaded videos.")

left, right = st.columns([2, 1])

with left:
    uploaded_file = st.file_uploader(
        "Upload Video File",
        type=["mp4", "mov", "avi", "mkv"]
    )

with right:
    model_size = st.selectbox(
        "Whisper Model",
        ["tiny", "base", "small"],
        index=1
    )

if uploaded_file is not None:
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("audio", exist_ok=True)
    os.makedirs("subtitles", exist_ok=True)

    video_path = os.path.join("uploads", uploaded_file.name)

    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())

    st.video(video_path)

    if st.button("🚀 Generate Subtitles"):
        try:
            audio_filename = os.path.splitext(uploaded_file.name)[0] + ".mp3"
            audio_path = os.path.join("audio", audio_filename)

            with st.spinner("Extracting audio..."):
                extract_audio_from_video(video_path, audio_path)

            with st.spinner("Transcribing speech..."):
                segments = transcribe_audio(audio_path, model_size=model_size)

            with st.spinner("Creating subtitle file..."):
                srt_content = generate_srt(segments)

            srt_filename = os.path.splitext(uploaded_file.name)[0] + ".srt"

            st.success("✅ Subtitles generated successfully!")

            st.subheader("Subtitle Preview")
            st.text_area("SRT Output", srt_content, height=350)

            st.download_button(
                "⬇ Download Subtitle File",
                data=srt_content,
                file_name=srt_filename,
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"❌ {e}")