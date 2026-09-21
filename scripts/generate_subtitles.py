"""
Script para generar subtítulos sincronizados (.srt y .ass) para videos de TikTok / Shorts.
Calcula los timestamps proporcionales al texto y a la duración real del archivo de audio WAV.
"""

import os
import re
import wave
import json

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DAY = "09"
SCRIPTS_DIR = os.path.join(PROJECT_ROOT, "scripts", f"day_{DAY}")
AUDIO_DIR = os.path.join(PROJECT_ROOT, "assets", f"day_{DAY}", "audio_notes")
SUBTITLES_DIR = os.path.join(PROJECT_ROOT, "assets", f"day_{DAY}", "subtitles")

os.makedirs(SUBTITLES_DIR, exist_ok=True)

def get_audio_duration(wav_path):
    """Devuelve la duración exacta en segundos de un archivo WAV."""
    if not os.path.exists(wav_path):
        return None
    try:
        with wave.open(wav_path, "rb") as wf:
            frames = wf.getnframes()
            rate = wf.getframerate()
            return frames / float(rate)
    except Exception as e:
        print(f"Error leyendo {wav_path}: {e}")
        return None

def extract_narration(script_path):
    """Extrae el texto de la sección 'Voz o narración sugerida' del guion markdown."""
    with open(script_path, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r"## Voz o narraci[oó]n sugerida\s*\n([\s\S]*?)(\n##\s|\n---|$)", content)
    if not match:
        return None
    text = match.group(1).strip()
    # Limpiar saltos de línea excesivos
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return " ".join(lines)

def split_into_phrases(text, max_words=5):
    """Divide el texto en frases cortas de 3-6 palabras ideales para subtítulos de TikTok."""
    # Dividir primero por pausas naturales (puntos, comas, signos de interrogación)
    sentences = re.split(r'(?<=[.,?!:;])\s+', text)
    phrases = []
    
    for sentence in sentences:
        words = sentence.strip().split()
        if not words:
            continue
        
        while len(words) > max_words:
            # Tomar max_words palabras
            chunk = words[:max_words]
            phrases.append(" ".join(chunk))
            words = words[max_words:]
        
        if words:
            phrases.append(" ".join(words))
            
    return phrases

def format_timestamp_srt(seconds):
    """Formatea segundos a formato SRT (00:00:00,000)."""
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hrs:02d}:{mins:02d}:{secs:02d},{millis:03d}"

def format_timestamp_ass(seconds):
    """Formatea segundos a formato ASS (0:00:00.00)."""
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    centis = int((seconds - int(seconds)) * 100)
    return f"{hrs:01d}:{mins:02d}:{secs:02d}.{centis:02d}"

def generate_subtitles_for_video(video_id, script_file, audio_duration):
    script_path = os.path.join(SCRIPTS_DIR, script_file)
    text = extract_narration(script_path)
    if not text:
        print(f"[{video_id}] No se pudo extraer la narración de {script_file}")
        return
    
    phrases = split_into_phrases(text)
    total_chars = sum(len(p) for p in phrases)
    
    # Asignar tiempo proporcional según número de caracteres con un pequeño gap
    srt_entries = []
    ass_dialogues = []
    
    current_time = 0.3  # Inicio tras 300ms de audio
    available_duration = max(audio_duration - 0.6, 5.0)
    
    for i, phrase in enumerate(phrases):
        weight = len(phrase) / float(total_chars)
        duration = weight * available_duration
        duration = max(duration, 0.9)  # Mínimo 900ms para legibilidad
        
        start_t = current_time
        end_t = min(current_time + duration, audio_duration)
        current_time = end_t + 0.05  # Gap de 50ms entre subtítulos
        
        # SRT
        srt_entries.append(f"{i+1}\n{format_timestamp_srt(start_t)} --> {format_timestamp_srt(end_t)}\n{phrase.upper()}\n")
        
        # ASS (estilo destacado para TikTok: blanco con contorno negro)
        ass_dialogues.append(
            f"Dialogue: 0,{format_timestamp_ass(start_t)},{format_timestamp_ass(end_t)},Default,,0,0,0,,{phrase.upper()}"
        )

    # Escribir archivo .srt
    srt_path = os.path.join(SUBTITLES_DIR, f"{video_id}.srt")
    with open(srt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_entries))
    print(f"[{video_id}] SRT generado: {srt_path}")

    # Escribir archivo .ass con estilo profesional vertical
    ass_path = os.path.join(SUBTITLES_DIR, f"{video_id}.ass")
    ass_content = f"""[Script Info]
Title: GlitchVault Subtitles - {video_id}
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
PlayResX: 1080
PlayResY: 1920

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Arial,68,&H00FFFFFF,&H0000FFFF,&H00000000,&H80000000,-1,0,0,0,100,100,1,0,1,4,2,2,60,60,450,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + "\n".join(ass_dialogues) + "\n"

    with open(ass_path, "w", encoding="utf-8") as f:
        f.write(ass_content)
    print(f"[{video_id}] ASS generado: {ass_path}")

def main():
    print("--- Generador de Subtítulos Sincronizados (Día 09) ---")
    script_files = sorted([f for f in os.listdir(SCRIPTS_DIR) if f.endswith(".md") and f.startswith("video_")])
    
    for sf in script_files:
        match = re.match(r"^(video_\d+)", sf)
        if not match:
            continue
        video_id = match.group(1)
        wav_path = os.path.join(AUDIO_DIR, f"{video_id}_narration.wav")
        
        duration = get_audio_duration(wav_path)
        if duration is None:
            print(f"[{video_id}] Audio {wav_path} aún no disponible, usando estimado de 45.0s...")
            duration = 45.0
            
        generate_subtitles_for_video(video_id, sf, duration)

if __name__ == "__main__":
    main()
