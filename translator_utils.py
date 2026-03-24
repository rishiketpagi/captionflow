from deep_translator import GoogleTranslator


def translate_segments(segments, target_language="hi"):
    translated_segments = []

    for segment in segments:
        text = segment["text"].strip()

        if not text:
            translated_text = ""
        else:
            translated_text = GoogleTranslator(
                source="auto",
                target=target_language
            ).translate(text)

        translated_segments.append({
            "start": segment["start"],
            "end": segment["end"],
            "text": translated_text
        })

    return translated_segments


def translate_full_text(text, target_language="hi"):
    if not text.strip():
        return ""

    return GoogleTranslator(
        source="auto",
        target=target_language
    ).translate(text)