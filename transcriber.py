from faster_whisper import WhisperModel

def transcribe_audio(audio_path, model_size="base"):

    model = WhisperModel(
        model_size,
        device="cpu",        # IMPORTANT
        compute_type="int8"  # IMPORTANT
    )

    segments, info = model.transcribe(audio_path)

    result = []

    for segment in segments:
        result.append({
            "start": segment.start,
            "end": segment.end,
            "text": segment.text.strip()
        })

    return result