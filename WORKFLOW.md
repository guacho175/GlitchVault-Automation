# Flujo de Trabajo de Producción (Workflow)

El secreto de GlitchVault no es solo tener buenas ideas, sino ejecutarlas a la velocidad necesaria para dominar el algoritmo (4 videos al día). Para lograrlo, sigue estrictamente este flujo de trabajo de 8 pasos.

---

## Paso 1: Ideación 💡
- **Objetivo:** Definir los 4 conceptos del día.
- **Acción:** 
  1. Revisa las tendencias de TikTok en gaming/terror.
  2. Selecciona 4 series diferentes de `/planning/series`.
  3. Escribe 1 frase de premisa para cada video.
- **Tip:** No sobre-pienses. A veces las ideas más absurdas ("Un Tamagotchi que demanda sacrificios") son las más virales.

## Paso 2: Guion y Estructura ✍️
- **Objetivo:** Crear el esqueleto del video.
- **Acción:**
  1. Crea el archivo de guion (Ej. `content/day_01/video_01_tamagotchi_maldito.md`).
  2. Selecciona un Gancho de `/planning/hooks/hook_bank.md`.
  3. Desarrolla el cuerpo (3-5 puntos clave o "imágenes" a mostrar).
  4. Agrega al final de la **Voz o narración sugerida** un CTA obligatorio de 3–8 segundos tomado/adaptado de `/planning/hooks/cta_bank.md`: pregunta concreta + respuesta fácil (palabra, opción o teoría) + razón narrativa para seguir la cuenta. No basta con “sígueme”.
- **Tip:** Escribe como si fueras una IA o un investigador cansado. Frases cortas. Directo al grano.

## Paso 3: Generación de Prompts Visuales 🖼️
- **Objetivo:** Traducir el guion a instrucciones para la IA.
- **Acción:**
  1. Abre `/prompts/system/master_style_prompt.md`.
  2. Por cada escena del guion, crea un prompt combinando el "Estilo Maestro" con la acción específica.
  3. Guárdalos en el log o en el archivo del guion para referencia futura.

## Paso 4: Generación de Imágenes / Recursos 🤖
- **Objetivo:** Crear el material visual crudo.
- **Acción:**
  1. Usa tu herramienta de IA preferida (Midjourney v6, DALL-E 3, etc.).
  2. Genera los assets asegurando un formato que se adapte bien a vertical o pide explícitamente relación de aspecto 9:16 (ej. `--ar 9:16` en Midjourney).
  3. Guarda las mejores imágenes en `content/day_X/assets/`.
- **Pitfall Común:** Evita que las imágenes se vean "demasiado limpias" o corporativas. Si es necesario, guárdalas y procésalas luego para ensuciarlas.

## Paso 5: Generación de Audio y Video 🎥
- **Objetivo:** Animar los recursos y darles atmósfera.
- **Acción:**
  1. Si usas IA de video (Runway, Pika, Luma), anima sutilmente las imágenes (paneos, zoom in, glitch effects).
  2. **Voz en Off (TTS):** Genera la voz usando ElevenLabs u otro TTS (voz robótica, de VHS, o misteriosa profunda).
  3. **Música y SFX:** Selecciona música ambiental de tensión o synthwave oscuro. Añade sonidos de errores (beeps de sistema, ruido estático).
  4. Reserva/genera metraje con movimiento real para el CTA final; el clip sigue activo mientras se escucha y se ve la llamada a la acción.

## Paso 6: Ensamblaje y Exportación ✂️
- **Objetivo:** Crear la pieza final en CapCut, Premiere o DaVinci.
- **Acción:**
  1. Importa todos los recursos.
  2. Ajusta el formato a **1080x1920 (9:16)**.
  3. Agrega las **superposiciones de marca** (scanlines, texto estilo consola, "REC").
  4. Genera subtítulos dinámicos en pantalla.
  5. Exporta como `.mp4` a 60fps (para una sensación fluida de gameplay falso).

## Paso 7: Revisión (QA) 🔎
- **Objetivo:** Control de calidad previo a la publicación.
- **Acción:**
  1. Revisa contra `/config/production_standards.md`.
  2. ¿El gancho visual ocurre en el segundo 1?
  3. ¿El texto de los subtítulos no tapa los botones de TikTok (zona derecha inferior y menú derecho)?
  4. ¿El volumen está balanceado (Voz clara, música de fondo sin saturar)?
  5. ¿El final contiene el CTA narrado de 3–8 segundos, con comentario/elección concreto y promesa de continuidad?
  6. ¿Hay movimiento real durante el CTA, sin extender una imagen fija?

## Paso 8: Publicación y Logs 📱
- **Objetivo:** Subir a la plataforma y documentar.
- **Acción:**
  1. Sube el video a TikTok.
  2. Añade el copy y los hashtags definidos en `/config/publishing_rules.md`.
  3. Configura la portada (selecciona el frame más impactante).
  4. Registra el video completado en `logs/generation_log.md`.
  5. (Opcional) Publica simultáneamente en YouTube Shorts e Instagram Reels si la estrategia lo dicta.
