# Plan de Producción Activo: 10 Nuevos Videos de Alta Retención (Día 09)

Este documento contiene el plan maestro de producción completo para generar **10 videos verticales (9:16) de alta retención** para TikTok y YouTube Shorts. Está diseñado para ser ejecutado y continuado desde cualquier PC.

---

## 🎯 Estándar de Producción y Retención
* **Duración por video:** Entre **35 y 55 segundos** (5 a 7 tomas cinemáticas de 8 segundos por video).
* **Resolución:** **1080x1920 Full HD (9:16 vertical)**.
* **Calidad en Google Flow:** **720p nativo**, modelo **Omni 1.1 Flash**, cantidad **x1** (12 créditos por generación).
* **Audio:** Locución documental con Gemini Flash TTS (voz *Algenib*) + mezcla de audio ambiental al 18%.
* **Subtítulos:** Generación sincronizada `.srt` y `.ass` (estilo TikTok: 2-3 palabras por línea en zona segura).
* **Carpeta Exclusiva de Salida:** `assets/day_09/videos_finales/` contendrá **únicamente los 10 archivos MP4 finales**.
* **Miniaturas de Alto CTR:** `assets/day_09/thumbnails/` (1080x1920, viñeta, titular Impact amarillo/blanco y sub-etiqueta cian).

---

## 📋 Lista de los 10 Videos a Producir

| # | Universo / Serie | Título / Tema | Hook (Primeros 3s) | CTA Narrativo (Cierre) |
|---|---|---|---|---|
| **01** | **Warhammer 40K** | *El Trono Dorado y los 1,000 Psíquicos Diarios* | "Para que la humanidad viaje por las estrellas, 1,000 personas son drenadas vivas cada día." | "¿Te sacrificarías por salvar a un billón de almas? Comenta SACRIFICIO o CONDENA." |
| **02** | **Warhammer 40K** | *Los Amos de la Noche (Night Lords) y el Terror Psicológico* | "Esta legión no bombardea tu planeta... solo transmite por radio lo que le hicieron a tu presidente." | "¿Aguantarías escuchar esa transmisión 1 minuto? Comenta AGUANTO o SILENCIO." |
| **03** | **Warhammer 40K** | *El Virus Carnívoro (Life-Eater Virus) de Isstvan III* | "Tarda menos de tres minutos en derretir tu carne, los bosques y la atmósfera entera." | "Si cae en tu ciudad, ¿qué harías en 180 segundos? Comenta REFUGIO o ACEPTAR." |
| **04** | **Anime Oscuro** | *Made in Abyss: La Maldición de la 6ta Capa* | "Bajar te da reliquias divinas... pero si intentas subir un solo metro, pierdes tu humanidad." | "¿Bajarías al fondo sabiendo que jamás podrás regresar? Comenta DESCENDER o QUEDARME." |
| **05** | **Anime Oscuro** | *Attack on Titan: El Origen Parasitario (Hallucigenia)* | "Creías que los Titanes nacieron por magia... hasta que desenterraron al parásito del árbol." | "¿Aceptarías la unión con el parásito por poder infinito? Comenta PODER o MONSTRUO." |
| **06** | **Anime Oscuro** | *Jujutsu Kaisen: La Verdadera Forma Caníbal de Sukuna* | "Sukuna no es solo una maldición: en la era Heian era un humano que cocinaba hechiceros vivos." | "¿Crees que Sukuna nació humano o maldición? Comenta HUMANO o BESTIA." |
| **07** | **Gaming Lore** | *Bloodborne: El Horripilante Secreto del Orfanato* | "Detrás de la puerta sellada de la Catedral, no había ángeles: había un laboratorio cósmico de niños." | "¿Crees que los Grandes nos guían o solo se alimentan de nuestra locura? Comenta ALIMENTO o GUÍA." |
| **08** | **Gaming Lore** | *Dark Souls: La Farsa de los Caballeros de Plata* | "Luchaste horas contra los arqueros de Anor Londo... sin saber que protegían un sol que murió hace siglos." | "¿Elegirías vivir en una mentira brillante o en la realidad oscura? Comenta ILUSIÓN o CENIZA." |
| **09** | **Gaming Lore** | *Silent Hill 2: El Simbolismo Oculto de Pyramid Head* | "Pyramid Head nunca intentó matarte: tú mismo lo creaste para que te castigara por tus crímenes." | "Si entraras a la niebla, ¿qué forma tendría tu propio monstruo? Comenta CULPA o MIEDO." |
| **10** | **Gaming Lore** | *Fallout: La Falsa Democracia del Refugio 11* | "Cada año votaban democráticamente a un vecino para ser ejecutado... pero la prueba era no obedecer." | "¿Votarías por sacrificar a un amigo para salvar al refugio? Comenta VOTAR o NEGARSE." |

---

## 🛠️ Flujo de Ejecución Paso a Paso (Para Cualquier PC)

### Paso 1: Guiones y Configuración
1. Crear la carpeta `scripts/day_09/` con los guiones `video_01_*.md` a `video_10_*.md`.
2. Crear `scripts/day_09/day_09_flow_automation.json` con todos los metadatos, prompts visuales y parámetros.

### Paso 2: Locución y Audio TTS
1. Ejecutar: `node scripts/audio_automation/generate_audio.js 09`
2. Esto genera los 10 archivos de voz en `assets/day_09/audio_notes/video_XX_narration.wav`.

### Paso 3: Generación Visual en Google Flow
1. Abrir Chrome con depuración remota en el puerto 9222:
   ```powershell
   & 'C:\Program Files\Google\Chrome\Application\chrome.exe' --remote-debugging-port=9222
   ```
2. Operar Google Flow (`flow.google.com`) con el subagente para generar los 5 a 7 clips por video.
3. Descargar y mover los clips a `assets/day_09/videos/` con la nomenclatura `video_XX_hero_clip.mp4`, `video_XX_clip_02.mp4`, etc.

### Paso 4: Subtítulos Sincronizados
1. Ejecutar `python scripts/generate_subtitles.py 09` para generar los `.srt` y `.ass` en `assets/day_09/subtitles/`.
2. Subtítulos optimizados para formato TikTok (máx. 2-3 palabras por línea, centrados con borde y resaltado amarillo).

### Paso 5: Ensamble con FFmpeg
1. Ejecutar: `python scripts/assemble_day_09_videos.py`
2. Salida: `assets/day_09/videos_finales/video_XX_*_FINAL.mp4`
3. Incluye verificación `freezedetect` para asegurar 0 fotogramas congelados.

### Paso 6: Generación de Miniaturas
1. Ejecutar: `python scripts/generate_day_09_thumbnails.py`
2. Salida: `assets/day_09/thumbnails/video_XX_thumbnail.jpg` (1080x1920).
