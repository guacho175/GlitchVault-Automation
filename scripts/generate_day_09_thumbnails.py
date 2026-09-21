"""
Script para generar miniaturas de alto CTR para el Día 09 (1080x1920).
Extrae un fotograma clave del video o renderiza un fondo temático con tipografía
de impacto (amarillo/blanco), sombras y badge de serie seguro para TikTok/Shorts.
"""

import os
import sys
import glob
import json
import subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DAY = "09"
ASSETS_DIR = os.path.join(PROJECT_ROOT, "assets", f"day_{DAY}")
VIDEOS_DIR = os.path.join(ASSETS_DIR, "videos")
THUMBNAILS_DIR = os.path.join(ASSETS_DIR, "thumbnails")
CONFIG_PATH = os.path.join(PROJECT_ROOT, "scripts", f"day_{DAY}", f"day_{DAY}_flow_automation.json")

os.makedirs(THUMBNAILS_DIR, exist_ok=True)

FONT_PATH = "C:/Windows/Fonts/arialbd.ttf"
if not os.path.exists(FONT_PATH):
    FONT_PATH = "C:/Windows/Fonts/impact.ttf"

def extract_keyframe(video_path, output_img):
    """Extrae un fotograma clave en el segundo 2 para evitar artefactos de inicio."""
    cmd = [
        "ffmpeg", "-y", "-ss", "00:00:02", "-i", video_path,
        "-vframes", "1", "-q:v", "2", output_img
    ]
    try:
        subprocess.run(cmd, capture_output=True, check=True)
        return os.path.exists(output_img)
    except Exception as e:
        print(f"Error extrayendo fotograma de {video_path}: {e}")
        return False

def draw_text_with_outline(draw, position, text, font, fill_color, outline_color, outline_width=6):
    x, y = position
    # Dibujar contorno
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx * dx + dy * dy <= outline_width * outline_width:
                draw.text((x + dx, y + dy), text, font=font, fill=outline_color)
    # Dibujar texto principal
    draw.text((x, y), text, font=font, fill=fill_color)

def generate_thumbnail(video_id, config_entry):
    output_path = os.path.join(THUMBNAILS_DIR, f"{video_id}_thumbnail.jpg")
    print(f"[{video_id}] Generando miniatura...")

    # 1. Buscar fotograma base
    pattern = os.path.join(VIDEOS_DIR, f"{video_id}_*.mp4")
    clips = sorted(glob.glob(pattern))
    clips = [c for c in clips if not c.endswith("_FINAL.mp4")]
    
    tmp_frame = os.path.join(THUMBNAILS_DIR, f"{video_id}_raw_frame.jpg")
    base_img = None
    
    if clips and extract_keyframe(clips[0], tmp_frame):
        base_img = Image.open(tmp_frame).convert("RGB")
        # Redimensionar a 1080x1920
        base_img = base_img.resize((1080, 1920), Image.Resampling.LANCZOS)
        if os.path.exists(tmp_frame):
            os.remove(tmp_frame)
    else:
        # Si aún no hay clips generados, crear un fondo oscuro cinematográfico con gradiente
        base_img = Image.new("RGB", (1080, 1920), color=(15, 15, 20))
        draw_bg = ImageDraw.Draw(base_img)
        # Dibujar gradiente oscuro
        for y in range(1920):
            r = int(10 + (y / 1920.0) * 25)
            g = int(10 + (y / 1920.0) * 15)
            b = int(20 + (y / 1920.0) * 35)
            draw_bg.line([(0, y), (1080, y)], fill=(r, g, b))

    # Aumentar contraste y saturación ligeramente
    enhancer = ImageEnhance.Contrast(base_img)
    base_img = enhancer.enhance(1.15)
    enhancer_sat = ImageEnhance.Color(base_img)
    base_img = enhancer_sat.enhance(1.1)

    # 2. Capa de viñeta oscura arriba y abajo para máxima legibilidad
    vignette = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
    v_draw = ImageDraw.Draw(vignette)
    
    # Degradado superior (para el gancho)
    for y in range(500):
        alpha = int(200 * (1.0 - (y / 500.0)))
        v_draw.line([(0, y), (1080, y)], fill=(0, 0, 0, alpha))
        
    # Degradado inferior (para el subtítulo)
    for y in range(1400, 1920):
        alpha = int(220 * ((y - 1400.0) / 520.0))
        v_draw.line([(0, y), (1080, y)], fill=(0, 0, 0, alpha))

    base_img = Image.alpha_composite(base_img.convert("RGBA"), vignette).convert("RGB")
    draw = ImageDraw.Draw(base_img)

    # Cargar fuentes
    try:
        font_large = ImageFont.truetype(FONT_PATH, 82)
        font_medium = ImageFont.truetype(FONT_PATH, 64)
        font_badge = ImageFont.truetype(FONT_PATH, 38)
    except Exception as e:
        print(f"Usando fuente predeterminada por error de carga: {e}")
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_badge = ImageFont.load_default()

    # Badge de serie (arriba a la izquierda, en zona segura)
    series_text = config_entry.get("series", "GLITCHVAULT").split("(")[0].strip().upper()
    badge_x, badge_y = 70, 220
    draw_text_with_outline(draw, (badge_x, badge_y), f"● {series_text}", font_badge, (0, 240, 255), (0, 0, 0), outline_width=4)

    # Texto Superior (Hook)
    overlays = config_entry.get("text_overlays", [])
    top_text_1 = overlays[0] if len(overlays) > 0 else config_entry["title"].upper()
    top_text_2 = overlays[1] if len(overlays) > 1 else ""

    y_pos = 320
    bbox1 = draw.textbbox((0, 0), top_text_1, font=font_large)
    w1 = bbox1[2] - bbox1[0]
    draw_text_with_outline(draw, ((1080 - w1) // 2, y_pos), top_text_1, font=font_large, fill_color=(255, 230, 0), outline_color=(0, 0, 0), outline_width=8)

    if top_text_2:
        y_pos += 95
        bbox2 = draw.textbbox((0, 0), top_text_2, font=font_large)
        w2 = bbox2[2] - bbox2[0]
        draw_text_with_outline(draw, ((1080 - w2) // 2, y_pos), top_text_2, font=font_large, fill_color=(255, 255, 255), outline_color=(0, 0, 0), outline_width=8)

    # Texto Inferior (Impacto)
    bottom_text = overlays[4] if len(overlays) > 4 else "VERDAD OCULTA"
    bbox_b = draw.textbbox((0, 0), bottom_text, font=font_medium)
    wb = bbox_b[2] - bbox_b[0]
    draw_text_with_outline(draw, ((1080 - wb) // 2, 1600), bottom_text, font=font_medium, fill_color=(255, 50, 50), outline_color=(0, 0, 0), outline_width=7)

    # Watermark inferior
    wm_text = "GLITCHVAULT ARCHIVES"
    bbox_wm = draw.textbbox((0, 0), wm_text, font=font_badge)
    wwm = bbox_wm[2] - bbox_wm[0]
    draw_text_with_outline(draw, ((1080 - wwm) // 2, 1720), wm_text, font=font_badge, fill_color=(180, 180, 180), outline_color=(0, 0, 0), outline_width=3)

    # Guardar imagen con alta calidad
    base_img.save(output_path, "JPEG", quality=95)
    print(f"[{video_id}] Miniatura guardada en: {output_path}")

def main():
    print("=== GENERADOR DE MINIATURAS DÍA 09 ===")
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
        generate_thumbnail(vid, entry)

if __name__ == "__main__":
    main()
