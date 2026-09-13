# Playbook de Automatización — GlitchVault

Guía técnica de cómo se produjeron realmente los videos del Día 1 con herramientas automatizadas (Gemini API + Google Flow + ffmpeg). Este documento complementa a `WORKFLOW.md` (que describe el proceso creativo/manual) con el flujo técnico real y los tropiezos ya resueltos, para que la próxima sesión no tenga que redescubrirlos.

## Orden correcto del pipeline (importante)

**Guion → Audio (TTS) → Video → Ensamblaje.** NO al revés. Se generó el audio primero para conocer su duración exacta, y luego se generó/extendió el video hasta cubrir esa duración (tope 30s por video). Hacerlo al revés (video primero) obliga a cortar narración o dejar video de más, que es lo que pasó con el Día 1 al principio y tocó corregir.

### Regla crítica: cobertura animada completa

- La suma de clips con movimiento real debe ser igual o mayor que la duración de la narración.
- Para 30 segundos de voz, generar 30 segundos animados: por ejemplo, 3 clips de 10s o 4 clips de 8s unidos con cortes/transiciones.
- Un fotograma congelado solo puede completar un margen residual de **máximo 2 segundos o 5% del video final (lo que sea menor)**. Ejemplo aprobado: 30s animados + 2s fijos para una voz de 32s.
- Está prohibido ahorrar créditos reemplazando escenas faltantes con `tpad=stop_mode=clone`. Si faltan más de 2 segundos, volver a Flow y generar otro clip o una continuación.
- Esta regla aplica a todos los días futuros y prevalece sobre prompts históricos que indiquen generar un único clip de 10 segundos.

### Regla crítica: cierre para interacción y seguidores

- Todo guion debe terminar con un CTA de **3 a 8 segundos** después de resolver la historia. Esa locución forma parte de la voz total que se genera antes de calcular los clips.
- El CTA pide una respuesta pequeña y específica (una palabra, una teoría o una elección) como acción primaria; el follow se conecta a una recompensa narrativa concreta, por ejemplo: “Comenta ‘OMEGA’. Si quieres que abramos otro archivo, sígueme.”
- No cerrar con “sígueme” aislado ni sustituir el CTA hablado por texto en el caption. El texto visible puede reforzarlo, con un máximo de dos líneas y respetando la safe zone.
- El metraje sigue animado durante el CTA: generar o reservar un clip final con acción visible. Un fotograma congelado no sirve como endcard, salvo el desfase técnico residual ya permitido.
- No regenerar ni descartar un clip solamente por un logo, nombre o interfaz de marca incidental. Si el clip sirve a la historia, se aprovecha; solo se corrige si la marca causa un error material de continuidad o el usuario solicita excluirla.

## 1. Audio (narración TTS)

- Script: `scripts/audio_automation/generate_audio.js` — lee `scripts/day_XX/*.md`, extrae la sección `## Voz o narración sugerida`, genera un `.wav` por video en `assets/day_XX/audio_notes/`.
- Uso: `node generate_audio.js 01` (cambia el número de día). Para producir solo un video sin tocar los demás: `node generate_audio.js 04 video_03`. Omite archivos que ya existen — borra el `.wav` si quieres regenerar.
- **Voz elegida y aprobada por el usuario: `Algenib`** (gravelly/rasposa, pega con el tono gamer/meme). Ya es el default en el script — no cambiarla sin confirmar con el usuario.
- Para probar otras voces rápido: `node sample_voice.js <voz> "<texto>" <salida.wav>`. Lista completa de 30 voces en los comentarios del código o pregúntame.
- **API key** en `scripts/audio_automation/.env` (`GEMINI_API_KEY=...`), nunca la subas a ningún lado.

### Cuotas gratuitas — el problema real que nos bloqueó
La capa gratuita de Gemini tiene límites **por modelo, por día**, no por minuto:
- `gemini-2.5-flash-preview-tts`: ~10 solicitudes/día gratis. Se agota rápido (cada voz de prueba cuenta).
- `gemini-2.5-pro-preview-tts`: **0 solicitudes gratis** (no disponible sin facturación).
- `gemini-3.1-flash-tts-preview`: cupo gratis SEPARADO del anterior (bucket distinto por ser otro modelo) — úsalo como respaldo cuando el primero se agote. **Ya es el default actual** en `generate_audio.js`.
- Si ambos se agotan en el mismo día: esperar al reset (24h) o activar facturación en Google AI Studio (decisión de dinero del usuario, no la tomes tú).
- Override manual: `GEMINI_TTS_MODEL="gemini-3.1-flash-tts-preview" node generate_audio.js 01`.

## 2. Video (Google Flow)

- URL correcta: **`https://labs.google/fx/tools/flow`**. NO `aistudio.google.com` (es Google AI Studio, una herramienta distinta — este fue el error original de Antigravity que impidió usar Flow).
- Login: la cuenta Google Flow del usuario es **AI Pro** con **1.000 créditos/mes**. Créditos ya usados hoy: ~150-200 (revisar con "Dame información sobre los costes de generación" dentro del chat de Flow).
- Costos por generación (usuarios no-Ultra): Veo 3.1 Lite 10 créditos, Veo 3.1 Fast 20, Veo 3.1 Quality 100, **Omni Flash ~15 créditos por clip de 10s** (el que se usó, mejor relación costo/calidad para volumen alto).
- Configuración recomendada al crear un proyecto nuevo: en Ajustes del agente, formato de video **9:16**, cantidad **x1** (no x4, gasta créditos de más), modelo Veo 3.1 Lite u Omni Flash.

### Flujo real que funciona (probado en 4 videos)
1. Abrir el proyecto existente ("18-ago, 05:01 p. m." por ahora — un proyecto nuevo por día si se quiere mantener organizado).
2. Clic en la miniatura del clip que quieres continuar.
3. Escribir el prompt de continuación en el cuadro de texto inferior ("Describe tus cambios", junto al ícono "Omni Flash").
4. Enviar (flecha). Si pide confirmación de créditos, clic en **"Aprobar y no volver a preguntar"** para no repetir el diálogo en cada generación.
5. Esperar 30-90s (a veces "en cola por alta demanda", puede tardar 3-4 min). Usar `get_page_text` para ver el % de progreso — si el screenshot falla con "Browser pane is not displayed" no es error real, seguir consultando `get_page_text` hasta que el % desaparezca.
6. Clic en la nueva miniatura generada → clic en el ícono de descarga (⬇, arriba a la derecha).
7. El archivo baja a `C:\Users\<usuario>\Downloads\` como `.tmp` y se renombra solo a un `.mp4` descriptivo tras unos segundos. Detectarlo con `ls -lat Downloads` y moverlo con `mv` al proyecto.

### Descarga de clips — método confiable (aprendido en Día 3, con paralelización en 2 navegadores)
El ícono de descarga (⬇) en la barra superior del editor de un clip es **poco confiable** al hacer clic directo la primera vez — a veces no dispara nada. Flujo confiable:
1. Abre el clip en su propio editor (URL `.../project/<id>/edit/<clipId>`, o doble clic en la miniatura).
2. Clic en el ícono ⬇ de la barra superior. Si no pasa nada en ~5s, reintenta el mismo clic una vez más (normalmente la 2ª vez sí dispara la descarga).
3. Alternativa igual de confiable: hover sobre la miniatura en la grilla → clic en "⋮" → "Descargar" → elegir resolución "720p (Tamaño original)" del submenú flotante. Este submenú a veces no aparece al primer clic en "Descargar"; si el menú se cierra sin mostrar resoluciones, reabre "⋮" y vuelve a intentar.
4. El archivo baja como `<uuid-random>.tmp` y Chrome lo renombra solo a un nombre descriptivo (`Nombre_del_clip_YYYYMMDDHHMM.mp4`) tras unos segundos — espera antes de mover/leer el archivo.
5. **Cuidado con paralelizar descargas en 2 pestañas/navegadores a la vez**: es fácil perder de vista cuál miniatura corresponde a cuál video si vas alternando rápido entre superficies. Confirma SIEMPRE con un screenshot que el texto bajo la miniatura (ej. "Cat morphing into...") coincide con el video que crees estar descargando antes de hacer clic — un descuido puede hacer que descargues el mismo clip dos veces bajo dos nombres distintos (verificar con `md5sum` si hay duda).
6. No intentes "cazar" el archivo `.tmp` con un script en bucle rápido (`while` con `sleep 0.1`) para copiarlo antes de que "desaparezca" — es contraproducente: puede capturar un `.tmp` a medio escribir (archivo corrupto/truncado) o un `.tmp` completamente ajeno de otra descarga en curso en el sistema. Es más lento pero más seguro simplemente esperar el renombrado automático y verificar con `file` + `ffprobe -show_entries format=duration` antes de mover el archivo.

### ⚠️ Función a EVITAR: "Ampliar (Veo 3.1 - Lite)"
El menú "+" en el timeline ofrece "Añadir clip" y "Ampliar (Veo 3.1 - Lite)". **"Ampliar" es poco confiable por automatización** — los clics en el menú no siempre registran, deja el timeline en un estado ambiguo, y en las pruebas terminó generando variantes sueltas de 10s en vez de extender de verdad. Usar en su lugar el flujo simple del punto anterior (escribir en "Describe tus cambios" sin pasar por ningún menú), que genera un clip nuevo de 10s con el mismo estilo — se une después con ffmpeg. Si aparece un menú/dropdown en pantalla, cerrarlo con `Escape` antes de escribir en cualquier cuadro de texto, o el texto no se registra.

### Narración/edición nativa de Flow (alternativa, no la que usamos)
Flow permite editar un clip existente ("Gemini Omni Flash — Edición de vídeo existente", 40 créditos) escribiendo algo como "Add a voiceover saying: ...". Funciona pero: (a) cuesta 40 créditos vs. casi gratis por la API de Gemini, y (b) es más difícl controlar el idioma/duración exacta. Se descartó a favor de generar el audio por separado con la API y mezclarlo con ffmpeg.

## 3. Ensamblaje final (ffmpeg)

Todo el ensamblaje (concatenar clips, agregar texto en pantalla, mezclar audio) se hace con `ffmpeg` por línea de comandos. Patrón completo y ya probado:

```bash
cd "assets/day_01"                    # o el día correspondiente
mkdir -p _ffmpeg_tmp
cp "/c/Windows/Fonts/arialbd.ttf" _ffmpeg_tmp/font.ttf   # Arial Bold: soporta tildes/ñ, a diferencia de Impact

# 1. Concatenar clip original + continuación
#    OJO: las rutas dentro del .txt son relativas AL ARCHIVO .txt, no al cwd
printf "file '../videos/video_0N_hero_clip.mp4'\nfile '../videos/video_0N_continuation_raw.mp4'\n" > _ffmpeg_tmp/concat_list.txt
ffmpeg -y -f concat -safe 0 -i _ffmpeg_tmp/concat_list.txt -c:v libx264 -c:a aac _ffmpeg_tmp/raw_20s.mp4

# 2. Solo si queda un desfase residual permitido (máximo 2s o 5%), rellenar con frame congelado.
#    Si falta más tiempo, DETENER el ensamblaje y generar otro clip animado en Flow.
ffmpeg -y -i _ffmpeg_tmp/raw_20s.mp4 -vf "tpad=stop_mode=clone:stop_duration=X" -c:v libx264 -c:a aac _ffmpeg_tmp/raw_padded.mp4

# 3. Textos en pantalla: un .txt por línea (usar Write tool, UTF-8, SIN emojis — Arial Bold no los renderiza bien)
#    Si una línea supera ~20 caracteres a fontsize 44 en 720px de ancho, partirla con salto de línea real dentro del .txt
#    (drawtext NO hace word-wrap automático — si no, el texto se corta en los bordes)

FONT="_ffmpeg_tmp/font.ttf"
DT_COMMON="fontfile=${FONT}:fontcolor=white:fontsize=44:box=1:boxcolor=black@0.45:boxborderw=16:x=(w-text_w)/2:y=h*0.72:line_spacing=6"

FILTER="[0:v]drawtext=textfile=_ffmpeg_tmp/line1.txt:${DT_COMMON}:enable='between(t\,0\,T1)',drawtext=textfile=_ffmpeg_tmp/line2.txt:${DT_COMMON}:enable='between(t\,T1\,T2)'[vout];[0:a]volume=0.18[amb];[amb][1:a]amix=inputs=2:duration=longest:dropout_transition=0[aout]"

ffmpeg -y -i _ffmpeg_tmp/raw_20s.mp4 -i audio_notes/video_0N_narration.wav \
  -filter_complex "$FILTER" -map "[vout]" -map "[aout]" -t DURACION_TOTAL \
  -c:v libx264 -pix_fmt yuv420p -c:a aac -movflags +faststart \
  videos/video_0N_FINAL.mp4

rm -rf _ffmpeg_tmp
```

### Gotchas de Windows con ffmpeg
- **NUNCA** uses rutas con letra de unidad (`C:/Windows/Fonts/...`) directo dentro de un filtro de ffmpeg — el `:` rompe el parser de `filter_complex`, incluso escapado con `\:`. Solución: copiar el archivo (fuente, .txt) a una carpeta relativa local y referenciarlo sin `C:`.
- El demuxer `concat` resuelve rutas relativas al archivo `.txt`, no al directorio de trabajo (`cwd`).
- Mezcla de audio: narración al volumen original + audio ambiente del clip a **volumen 0.18** (para que no compita con la voz) vía `amix`.

## 4. Verificación antes de enviar

Extraer 2-4 fotogramas de muestra (`ffmpeg -ss X -update 1 -frames:v 1 salida.jpg`) y revisarlos con la herramienta Read (visión) antes de dar por bueno un video — así se detectó y corrigió el desborde de texto fuera de pantalla en la primera pasada del Día 1.

Además, ejecutar detección de congelamiento sobre el archivo final:

```bash
ffmpeg -i videos/video_0N_FINAL.mp4 -vf "freezedetect=n=-55dB:d=2" -an -f null -
```

Si aparece un tramo congelado continuo mayor al margen residual permitido, el video **no aprueba QA**: se debe generar metraje animado adicional y volver a ensamblar.

## 5. Nomenclatura de archivos usada

- `assets/day_XX/audio_notes/video_0N_narration.wav` — narración TTS.
- `assets/day_XX/videos/video_0N_hero_clip.mp4` — primer clip generado en Flow (10s).
- `assets/day_XX/videos/video_0N_continuation_raw.mp4` — clip de continuación generado en Flow.
- `assets/day_XX/videos/video_0N_clip_03.mp4` (y siguientes) — clips animados adicionales necesarios para cubrir toda la narración.
- `assets/day_XX/videos/video_0N_FINAL.mp4` — entregable listo para revisión/publicación.

## 5.1 Portadas / thumbnails estáticas (imágenes, sin usar Flow)

Para portadas de YouTube/miniaturas (imágenes estáticas, no video) **NO uses Flow** — gastaría créditos de video innecesariamente. Tampoco la API de Gemini (`generate_audio.js`-style): el modelo de imagen (`gemini-2.5-flash-image` / Nano Banana vía API) tiene **cupo gratis 0** en esta cuenta (`limit: 0` en el error 429), requiere facturación.

**Flujo que funciona:** usar Gemini en el navegador (`https://gemini.google.com/app`) con la misma cuenta de Google ya logueada (Galindez175) — pestaña NUEVA y separada de la de Flow, para no confundir créditos. El modelo web (Nano Banana) SÍ renderiza texto nítido embebido en la imagen (títulos, HUD, sellos) sin necesitar compositing posterior con ffmpeg — confirmado calidad equivalente a las miniaturas de Antigravity del Día 1.

Pasos:
1. `tabs_create` una pestaña nueva, `navigate` a `https://gemini.google.com/app`.
2. Click en el textbox (ref del `textbox "Introduce una petición para Gemini"`), `type` el prompt completo (incluye TODO el texto exacto a renderizar entre comillas).
3. **OJO:** `key Return` con texto largo/multilínea solo agrega un salto de línea, no envía. Hay que `read_page` y hacer click en el botón real "Enviar mensaje".
4. Esperar ~15-20s, `read_page` de nuevo — aparece un botón "Descargar imagen a tamaño completo" (a veces directo en el hilo, a veces hay que abrir el lightbox haciendo click en la imagen primero).
5. El archivo baja a Descargas como `Gemini_Generated_Image_xxxx.jpg` o a veces queda como `<uuid>.tmp` (igual es un JPEG válido, `file` lo confirma) — mover con `mv` y renombrar a `video_0N_thumbnail.jpg`.
6. Para la siguiente imagen, click "Nueva conversación" (evita que el modelo mezcle personajes/estilo entre miniaturas).
7. Verificar dimensiones con `ffprobe` (sale ~1536x2752, ratio 9:16 aproximado).

Prompt: combinar el prefijo/sufijo de la serie en `master_style_prompt.md` + contenido específico del guion + especificar EXACTAMENTE qué texto renderizar y en qué formato (título grande, HUD, sellos, watermark "GlitchVault"), replicando la plantilla visual ya usada por serie en `assets/day_01/thumbnails/`.

## 6. Publicación en TikTok — pendiente

No automatizada todavía. Requiere la extensión "Claude in Chrome" conectada (para operar el TikTok real logueado del usuario) y confirmación explícita del usuario antes de publicar cada video (política de seguridad: publicar contenido público siempre requiere permiso explícito, no se puede dejar en automático). Verificar también si la cuenta de TikTok a usar es `@GlitchVault_` (la del proyecto) o `@error_404_world` (la que apareció logueada en una captura) — parecen ser cuentas distintas, confirmar con el usuario antes de subir nada.
