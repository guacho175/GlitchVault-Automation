# Decision Log (Registro de Decisiones)

Este documento registra las decisiones clave, creativas y estructurales, tomadas durante la vida del proyecto **GlitchVault**. Registrar el "por qué" de las cosas ayuda a no repetir errores en el futuro.

---

## 📅 Fecha: 2026-08-18 (Setup Inicial)

### 1. Nombre de la Cuenta: `GlitchVault`
**Razón:** "Vault" sugiere un archivo o contenedor de cosas clasificadas, lo cual encaja con el formato de series ("Archivo 01", etc.). "Glitch" conecta inmediatamente con la cultura de videojuegos y errores de sistema. Fácil de recordar y pronunciar.

### 2. Meta de 4 Videos Diarios
**Razón:** El algoritmo actual premia la constancia extrema y el volumen en cuentas nuevas. Al tener formato de series, el volumen alto permite a los usuarios consumir varios episodios rápido, acelerando el proceso de fidelización. Si hacemos menos, el crecimiento inicial será muy lento.

### 3. Separación de Agentes en AGENTS.md
**Razón:** Para mantener la calidad. Generar IA de forma masiva puede llevar a resultados "genéricos" y plásticos. Forzar al operador a pensar con "sombreros" distintos (Guionista vs Productor) asegura que el lore y la narrativa se mantengan sólidos, en lugar de ser solo un montón de imágenes IA sin sentido.

### 4. Transición a Livestream como End-Game
**Razón:** TikTok recompensa el contenido de VOD (Video on Demand) pero monetiza mucho mejor los directos (Lives). La audiencia atraída por el terror, misterio y videojuegos es la demográfica exacta que consume transmisiones de juegos de terror independientes (Fears to Fathom, Chilla's Art) o juegos retro extraños, creando un embudo de conversión perfecto.

---

## 📅 Fecha: 2026-08-23 (Auditoría y reconstrucción de `video_04` — Perro Nivel 1→100)

### Contexto
`video_04_evolucion_perro` (Día 1) obtuvo ~23 vistas en TikTok, muy por debajo del resto del
mismo día (NPC 1.900, Leviatán 1.400, Palomas 1.200).

### Causa raíz encontrada (auditoría con ffmpeg, frame-by-frame)
El `video_04_FINAL.mp4` publicado mostraba **exclusivamente el clip de la forma Nivel 100**
(`hero_clip` + `continuation_raw` concatenados) durante los 22.3s completos — nunca aparecían
las etapas Nivel 1 / 30 / 70. Causa: solo se generó video animado (Google Flow) para la forma
final; las otras 3 etapas quedaron solo como paneles estáticos dentro del collage
`video_04_scene_01.jpg`, y el editor las omitió al armar el FINAL. El audio narraba las 4 etapas
completas mientras el video no mostraba ninguna transición — desincronía total audio/visual.
Esto explica el colapso de rendimiento mucho mejor que el hook o la portada (que también tenían
problemas, pero secundarios): el video no cumplía la promesa de su propio título.

### Decisión: reconstruir (no descartar)
Se reconstruyó usando material ya existente, sin generar video IA nuevo:
- **Guion v2:** `scripts/day_01/video_04_evolucion_perro_v2.md` (hook reformulado como
  "experimento de IA", consistente con `planning/series/evoluciones_ia.md` y
  `planning/hooks/hook_bank.md` — el guion original no usaba ningún hook del banco).
- **Audio v2:** `assets/day_01/audio_notes/video_04_narration_v2.wav`, generado con
  `scripts/audio_automation/generate_audio_v2_perro.js` (mismo pipeline y voz `Algenib` de
  `generate_audio.js`, apuntando a un archivo separado para no pisar el original).
- **Video v2:** `assets/day_01/videos/video_04_FINAL_v2.mp4` (25.4s). Estructura: teaser con
  `hero_clip` (0–6.6s, muestra el resultado como flash-forward) → Nivel 1/30/70 con Ken Burns
  sobre los paneles recortados del collage ya existente (6.6–18.2s) → clímax con
  `continuation_raw` (18.2–25.4s). Técnica: `ffmpeg zoompan` sobre cada panel recortado
  (`crop` del collage 768x1376 en 4 franjas de 344px) en vez de generar clips nuevos en Flow —
  ahorra créditos y resuelve el problema de raíz (ausencia de progresión visual real).
- **Portada v2:** `assets/day_01/thumbnails/video_04_thumbnail_v2.jpg`. Split vertical
  cachorro/lobo cósmico sobre fondo negro sólido, un solo titular ("NIVEL 1 → NIVEL 100"), sin
  barras de XP ni nombres inventados — corrige que la portada original violaba dos red flags de
  `BRAND_GUIDE.md` ("no demos genéricos de IA", "no estéticas limpias/corporativas").

### Publicación
El `video_04_FINAL.mp4` original se deja público (no se elimina ni se oculta). La v2 se publica
como pieza nueva (no repost), esperando unos días para no canibalizar señales del original.
Pendiente de aprobación explícita del usuario antes de subir cualquier cosa a TikTok (ver
`scripts/AUTOMATION_PLAYBOOK.md`, sección 6).

---
*(Añadir nuevas decisiones importantes debajo)*

---

## 📅 Fecha: 2026-08-30 — Retrofit CTA Día 1, Video 4

### Decisión
Se preservó íntegramente `assets/day_01/videos/video_04_FINAL_v2.mp4` y se creó, sin publicar,
`assets/day_01/videos/video_04_FINAL_CTA_v1.mp4`. Se añadieron 6,69 s de cierre sobre el tramo
03,00–09,69 s de `video_04_continuation_raw.mp4`, que mantiene el movimiento de la forma cósmica.

### CTA
Locución Algenib adicional: “¿Qué animal subimos al nivel cien? Comenta DRAGÓN. Si quieres ver
su evolución, sígueme.” Texto visible: “¿QUÉ ANIMAL SUBIMOS? / COMENTA: DRAGÓN”. La pregunta y
la palabra concreta reducen la fricción del comentario; el follow promete una evolución siguiente.

### QA
El resultado dura 32,07 s y tiene 1080×1920 a 30 fps, con audio AAC. `freezedetect=n=-55dB:d=2`
no informó congelamientos; las capturas 26,25 s, 28,50 s y 31,30 s confirman texto legible dentro
de safe zone y cambio visual continuo. No se usó `tpad`, endcard estática, Flow ni créditos.

---

## 📅 Fecha: 2026-08-30 — Corrección de narración, Día 1 Video 4

### Problema detectado
La pista heredada abría hablando de pedir una evolución a inteligencia artificial y no acompañaba
los niveles mostrados. Eso desviaba el video hacia la herramienta de producción en vez de la
fantasía del videojuego y debilitaba su progresión.

### Corrección
Se creó `assets/day_01/audio_notes/video_04_narration_retrofit_v4.wav` (Algenib, 25,25 s) con
esta secuencia: videojuego de un perro que sube de nivel → Nivel 1 cachorro → Nivel 25 armadura
y alas → Nivel 50 máquina de guerra → Nivel 100 deidad cósmica/jefe final. Se creó
`assets/day_01/videos/video_04_FINAL_CTA_v2.mp4`, preservando los MP4 anteriores y el mismo CTA
animado de 6,69 s.

### QA
La salida dura 32,07 s, tiene 1080×1920 a 30 fps y audio AAC. `freezedetect=n=-55dB:d=2` no
detectó eventos; las capturas CTA están en `_cta_retrofit_tmp/qa_video_04_v2/`. No se usó Flow,
créditos, `tpad` ni una endcard estática.

---

## 📅 Fecha: 2026-08-30 — Retrofit CTA Día 1, Video 1

### Decisión
Se preservó `assets/day_01/videos/video_01_FINAL.mp4` y se creó, sin publicar,
`assets/day_01/videos/video_01_FINAL_CTA_v1.mp4`. El cierre reutiliza 7,29 s del movimiento de
calle de `video_01_continuation_raw.mp4` (02,30–09,59 s), incluyendo a la paloma caminando y
alzando las alas.

### CTA y QA
La voz Algenib dice: “¿Jugarías este GTA de palomas? Comenta PALOMA. Si quieres abrir otra ciudad
criminal, sígueme.” El resultado dura 27,63 s, tiene 1080×1920 a 30 fps y audio AAC. No hubo
eventos con `freezedetect=n=-55dB:d=2`; las capturas 21,10 s, 23,90 s y 26,80 s muestran texto
legible en safe zone y movimiento continuo. No se usó `tpad`, Flow ni créditos.

---

## 📅 Fecha: 2026-08-30 — Retrofit CTA Día 1, Video 2

### Decisión y CTA
Se preservó `assets/day_01/videos/video_02_FINAL.mp4` y se creó, sin publicar,
`assets/day_01/videos/video_02_FINAL_CTA_v1.mp4`. El CTA reutiliza 6,01 s de
`video_02_continuation_raw.mp4` (03,00–09,01 s): Leviatán, oleaje y tentáculos siguen en
movimiento. La voz Algenib dice: “¿Con qué arma lo derrotas? Comenta ANCLA. Si quieres ver al
próximo boss, sígueme.”

### QA
El MP4 dura 21,53 s, tiene 1080×1920 a 30 fps y audio AAC. `freezedetect=n=-55dB:d=2` no devolvió
eventos; las capturas 16,20 s, 18,70 s y 20,90 s confirman texto legible en safe zone y
movimiento continuo. No se usó `tpad`, Flow ni créditos.

---

## 📅 Fecha: 2026-08-30 — Retrofit CTA Día 1, Video 3

### Decisión y CTA
Se preservó `assets/day_01/videos/video_03_FINAL.mp4` y se creó, sin publicar,
`assets/day_01/videos/video_03_FINAL_CTA_v1.mp4`. El CTA recicla 7,29 s de
`video_03_continuation_raw.mp4` (00,50–07,79 s): estática VHS, avance del NPC y glitch rojo,
todo con movimiento. La voz Algenib dice: “¿Abrimos el archivo cero cuarenta y cinco? Comenta
ARCHIVO. Si quieres ver qué lo controla, sígueme.”

### QA
El MP4 dura 24,50 s, tiene 1080×1920 a 30 fps y audio AAC. `freezedetect=n=-55dB:d=2` no informó
eventos; las capturas 18,00 s, 21,00 s y 24,00 s muestran el CTA legible en safe zone y cambios
visuales constantes. No se usó `tpad`, Flow ni créditos.

---

## 📅 Fecha: 2026-08-30 — Formato obligatorio de conversión

### Decisión
Todos los videos futuros de GlitchVault terminan con un CTA narrado de 3–8 segundos sobre
metraje que siga animado. Su fórmula es: pregunta concreta + respuesta de baja fricción
(palabra, opción o teoría) + razón narrativa para seguir la cuenta.

### Razón
El video del Día 4, Video 1 funcionó creativamente como historia de 19.13 s, pero necesitaba
un cierre que convirtiera la atención en comentarios y seguidores. La versión
`video_01_FINAL_v3.mp4` añadió 7.85 s: “¿Tú lo jugarías? Escribe OMEGA en los comentarios.
Si quieres que abramos otro archivo perdido, sígueme.” El resultado conservó el corte original,
añadió movimiento real y pasó `freezedetect` sin congelamientos continuos.

### Aplicación
- El CTA se incluye dentro de la sección **Voz o narración sugerida** antes de generar TTS.
- Debe tener cobertura visual real; no se permite rellenarlo con `tpad`, fotograma congelado ni endcard estático.
- Los guiones pendientes del Día 4 ya adoptan el formato.
- Las guías globales y el QA lo convierten en requisito para los días posteriores.
- No se regenera un clip útil solo por una marca/logo incidental; se prioriza la calidad narrativa y visual.

---

## 📅 Fecha: 2026-08-30 — Señales explícitas de videojuego inventado

### Decisión
En las piezas que presenten juegos ficticios o elecciones RPG, el metraje y la edición deben dejar claro desde el primer segundo que se trata de un videojuego: nombre/título ficticio, HUD o interfaz persistente, cursor/selección, elementos de estado y lenguaje de captura gameplay.

### Razón
Una animación fantástica aislada puede funcionar visualmente, pero no comunica por sí sola la premisa central de GlitchVault: descubrir juegos que no existen. Para el Video 3 del Día 4 se usó el juego ficticio `MOUNT//NULL`, una interfaz de selección y rótulos controlados en edición, de modo que la lectura no dependa de que la IA renderice texto correcto.

### Aplicación
- Priorizar prompts de Flow que describan captura de gameplay e interfaz visible, no solo arte conceptual.
- Añadir en edición texto/HUD verificable cuando el generador no dé señales inequívocas de juego.
- Mantener el HUD en zona segura y sin reemplazar el movimiento real ni el CTA final.
