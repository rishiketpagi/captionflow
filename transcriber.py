from faster_whisper import WhisperModel


def transcribe_audio(audio_path, model_size="tiny", language=None, task="transcribe"):
    model = WhisperModel(
        model_size,
        device="cpu",
        compute_type="int8"
    )

    segments, info = model.transcribe(
        audio_path,
        language=language,
        task=task
    )

    result = []
    full_text_parts = []

    for segment in segments:
        text = segment.text.strip()
        result.append({
            "start": segment.start,
            "end": segment.end,
            "text": text
        })
        full_text_parts.append(text)

    full_text = " ".join(full_text_parts)

    return result, full_text