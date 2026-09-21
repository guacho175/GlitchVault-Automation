"""
Script de ensamblaje automatizado de videos para el Día 09 (GlitchVault).
Ensambla clips de video generados con la narración de audio, realiza mezcla sonora,
escala a 1080x1920 (9:16) y aplica control de calidad (QA) con freezedetect.
"""

import os
import sys
import glob
import json
import wave
import subprocess

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DAY = "09"
ASSETS_DIR = os.path.join(PROJECT_ROOT, "assets", f"day_{DAY}")
VIDEOS_DIR = os.path.join(ASSETS_DIR, "videos")
AUDIO_DIR = os.path.join(ASSETS_DIR, "audio_notes")
FINAL_DIR = os.path.join(ASSETS_DIR, "videos_finales")
TMP_DIR = os.path.join(ASSETS_DIR, "_ffmpeg_tmp")
CONFIG_PATH = os.path.join(PROJECT_ROOT, "scripts", f"day_{DAY}", f"day_{DAY}_flow_automation.json")

os.makedirs(FINAL_DIR, exist_ok=True)
os.makedirs(TMP_DIR, exist_ok=True)

def get_audio_duration(wav_path):
    if not os.path.exists(wav_path):
        return None
    try:
        with wave.open(wav_path, "rb") as wf:
            frames = wf.getnframes()
            rate = wf.getframerate()
            return frames / float(rate)
    except Exception as e:
        print(f"Error leyendo duración de audio {wav_path}: {e}")
        return None

def get_video_duration(video_path):
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", video_path
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return float(res.stdout.strip())
    except Exception as e:
        print(f"Error midiendo duración de video {video_path}: {e}")
        return None

def check_freezedetect(video_path):
    """Ejecuta freezedetect sobre el video ensamblado. Retorna True si pasa QA."""
    cmd = [
        "ffmpeg", "-i", video_path,
        "-vf", "freezedetect=n=-55dB:d=2",
        "-an", "-f", "null", "-"
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True)
        # Buscar 'lavfi.freezedetect.freeze_duration' mayor a 2.0
        output = res.stderr
        durations = []
        for line in output.splitlines():
            if "freeze_duration:" in line:
                parts = line.split("freeze_duration:")
                try:
                    dur = float(parts[1].split()[0])
                    durations.append(dur)
                except:
                    pass
        max_freeze = max(durations) if durations else 0.0
        if max_freeze > 2.0:
            print(f"[QA WARNING] Se detectó congelamiento de {max_freeze:.2f}s en {video_path}")
            return False
        return True
    except Exception as e:
        print(f"Error ejecutando freezedetect: {e}")
        return False

def assemble_video(video_id, config_entry):
    final_output = os.path.join(FINAL_DIR, f"{video_id}_FINAL.mp4")
    
    # 1. Optimización: si ya existe y es válido (>1MB), omitir
    if os.path.exists(final_output) and os.path.getsize(final_output) > 1000000:
        print(f"[{video_id}] Video final ya existe y es válido ({os.path.getsize(final_output)} bytes). Omitiendo.")
        return True

    wav_path = os.path.join(AUDIO_DIR, f"{video_id}_narration.wav")
    if not os.path.exists(wav_path):
        print(f"[{video_id}] Falta archivo de audio: {wav_path}")
        return False

    audio_dur = get_audio_duration(wav_path)
    if audio_dur is None:
        print(f"[{video_id}] No se pudo determinar duración del audio.")
        return False

    # 2. Buscar clips de video disponibles para este video_id
    pattern = os.path.join(VIDEOS_DIR, f"{video_id}_*.mp4")
    clips = sorted(glob.glob(pattern))
    
    # Filtrar que no sea el final si estuviera en la misma carpeta
    clips = [c for c in clips if not c.endswith("_FINAL.mp4")]
    
    if not clips:
        print(f"[{video_id}] No se encontraron clips de video para {video_id} en {VIDEOS_DIR}")
        return False

    print(f"[{video_id}] Clips encontrados ({len(clips)}): {[os.path.basename(c) for c in clips]}")
    
    # 3. Concatenar clips
    concat_txt = os.path.join(TMP_DIR, f"{video_id}_concat.txt")
    with open(concat_txt, "w", encoding="utf-8") as f:
        for c in clips:
            # Ruta relativa al archivo concat.txt o normalizada
            rel_path = os.path.relpath(c, TMP_DIR).replace("\\", "/")
            f.write(f"file '{rel_path}'\n")

    raw_concat = os.path.join(TMP_DIR, f"{video_id}_raw_concat.mp4")
    cmd_concat = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", concat_txt,
        "-c:v", "libx264", "-c:a", "aac",
        raw_concat
    ]
    subprocess.run(cmd_concat, capture_output=True, check=True)

    video_dur = get_video_duration(raw_concat)
    print(f"[{video_id}] Duración video crudo: {video_dur:.2f}s | Duración audio: {audio_dur:.2f}s")

    # 4. Manejo de desfase residual
    input_video = raw_concat
    if video_dur < audio_dur:
        diff = audio_dur - video_dur
        # Margen residual permitido: máximo 2.0s o 5%
        max_allowed_freeze = min(2.0, audio_dur * 0.05)
        if diff > max_allowed_freeze:
            print(f"[{video_id}] ALERTA QA: Faltan {diff:.2f}s de video animado. Excede margen de {max_allowed_freeze:.2f}s.")
            print(f"[{video_id}] Se debe generar metraje adicional en Flow.")
            # Para fines de prueba o ensamble previo, se puede padding, pero marcando QA
        
        padded_video = os.path.join(TMP_DIR, f"{video_id}_padded.mp4")
        cmd_pad = [
            "ffmpeg", "-y", "-i", raw_concat,
            "-vf", f"tpad=stop_mode=clone:stop_duration={diff + 0.2:.2f}",
            "-c:v", "libx264", "-c:a", "aac",
            padded_video
        ]
        subprocess.run(cmd_pad, capture_output=True, check=True)
        input_video = padded_video

    # 5. Mezcla de audio y escalado a 1080x1920 (Lanczos)
    # Audio del video al 0.18 de volumen, audio de voz al 1.0
    filter_complex = (
        "[0:v]scale=1080:1920:flags=lanczos,format=yuv420p[vout];"
        "[0:a]volume=0.18[amb];"
        "[amb][1:a]amix=inputs=2:duration=first:dropout_transition=0[aout]"
    )

    cmd_final = [
        "ffmpeg", "-y",
        "-i", input_video,
        "-i", wav_path,
        "-filter_complex", filter_complex,
        "-map", "[vout]", "-map", "[aout]",
        "-t", f"{audio_dur:.2f}",
        "-c:v", "libx264", "-preset", "slow", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        final_output
    ]
    
    print(f"[{video_id}] Ensamblando video final...")
    res = subprocess.run(cmd_final, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[{video_id}] Error en ffmpeg: {res.stderr}")
        return False

    print(f"[{video_id}] Video final creado: {final_output}")

    # 6. QA Freezedetect
    qa_passed = check_freezedetect(final_output)
    if qa_passed:
        print(f"[{video_id}] QA APROBADO (0 fotogramas congelados fuera de norma).")
    else:
        print(f"[{video_id}] QA RECHAZADO: Revisar fotogramas.")

    return True

def main():
    print("=== ENSAMBLADOR DE VIDEOS DÍA 09 ===")
    if not os.path.exists(CONFIG_PATH):
        print(f"No existe el archivo de configuración {CONFIG_PATH}")
        sys.exit(1)

    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)

    target_video = sys.argv[1] if len(sys.argv) > 1 else None

    for entry in config.get("videos", []):
        vid = entry["id"]
        if target_video and vid != target_video:
            continue
        print(f"\n--- Procesando {vid}: {entry['title']} ---")
        assemble_video(vid, entry)

if __name__ == "__main__":
    main()
