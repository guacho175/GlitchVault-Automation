# Guía del Agente de Navegador: Automatización en Google Flow

Esta guía detalla el protocolo exacto de automatización para que un agente de IA que controle un navegador (vía extensión, CDP o Puppeteer) opere **Google Flow** (`https://labs.google/fx/tools/flow`) y genere los videos de la nueva ola (Día 08: Warhammer 40K y Anime Turbio) sin errores ni gasto excesivo de créditos.

---

## 1. Parámetros Críticos y Modelo

- **URL de la Herramienta:** `https://labs.google/fx/tools/flow`
- **Cuenta:** Google con suscripción AI Pro (Galindez175).
- **Modelo Mandatorio:** **`Omni Flash`** (~15 créditos por generación de 10s).
  - *No usar Veo 3.1 Quality* (cuesta 100 créditos por clip).
  - *No usar 'Ampliar (Veo 3.1 - Lite)'* desde el timeline: genera inconsistencias y pierde el contexto.
- **Relación de Aspecto:** **`9:16` (Vertical)** siempre.
- **Cantidad de Generaciones por Prompt:** **`x1`** (Verificar en ajustes para no gastar créditos en variantes innecesarias).

---

## 2. Flujo de Generación Paso a Paso

Para cada video definido en `scripts/day_08/day_08_flow_automation.json`:

### Paso 1: Inicialización del Proyecto
1. Navegar a `https://labs.google/fx/tools/flow`.
2. Crear un **Nuevo Proyecto** o abrir el proyecto del día.
3. Asegurar que los ajustes del agente estén en **9:16**, modelo **Omni Flash**, cantidad **x1**.

### Paso 2: Generación del Hero Clip (Clip 1)
1. Enfocar el cuadro de texto inferior (*"Describe tus cambios"* o *"Describe tu escena"*).
2. Pegar el prompt del `flow_clips[0].prompt`.
3. Hacer clic en el botón de enviar (flecha).
4. Si aparece el modal de confirmación de créditos, hacer clic en **"Aprobar y no volver a preguntar"**.
5. Esperar la finalización (monitorear el texto del progreso del 0% al 100%).

### Paso 3: Continuación Cinemática (Clip 2 y Clip 3)
1. Hacer clic sobre la miniatura del clip recién generado para abrir el visor.
2. Enfocar el cuadro de texto *"Describe tus cambios"*.
3. Pegar el prompt del siguiente clip (`flow_clips[1].prompt` para el cuerpo, o `flow_clips[2].prompt` para el clímax/CTA).
4. Enviar y esperar la generación.
5. **Regla de Cobertura Animada:** La suma de clips debe igualar o superar la duración de la locución del audio (30 a 35 segundos). No usar imágenes congeladas mayores a 1.5s.

### Paso 4: Descarga Automatizada de los Clips
1. En la vista del clip en su editor, o pasando el cursor sobre la miniatura en la grilla:
   - Clic en los tres puntos **`⋮`** $\rightarrow$ **`Descargar`** $\rightarrow$ seleccionar **`720p (Tamaño original)`**.
   - O clic directo en el icono de descarga **⬇** en la barra superior.
2. El archivo se descargará en la carpeta de descargas de Chrome (`Downloads`) temporalmente como `.tmp` y luego el sistema lo renombrará a un `.mp4`.
3. Esperar que el archivo esté completamente escrito antes de moverlo.
4. Mover y renombrar el archivo a la estructura del proyecto:
   - `assets/day_08/videos/video_0N_hero_clip.mp4`
   - `assets/day_08/videos/video_0N_continuation_raw.mp4`
   - `assets/day_08/videos/video_0N_clip_03.mp4`

---

## 3. Generación del Audio (TTS)

Antes de ensamblar el video, el audio debe estar listo para fijar la duración milimétrica del corte final:
1. Ejecutar el script ya integrado:
   ```bash
   node scripts/audio_automation/generate_audio.js 08
   ```
2. El script leerá la sección `## Voz o narración sugerida` de cada uno de los archivos `scripts/day_08/video_0N_*.md` y generará los archivos `.wav` con la voz `Algenib` en `assets/day_08/audio_notes/`.

---

## 4. Generación de Portadas / Thumbnails

Para no gastar créditos de video en imágenes estáticas:
1. Abrir en una pestaña separada **`https://gemini.google.com/app`**.
2. Pegar el `thumbnail_prompt` de cada video (que incluye la tipografía en amarillo y cian, safe zones y elementos clave).
3. Descargar la imagen resultante en 9:16 y guardarla en:
   - `assets/day_08/thumbnails/video_0N_thumbnail.jpg`.

---

## 5. Pipeline de Ensamblado (ffmpeg)

Una vez descargados los clips y el audio, se ensamblan con el script estándar:
- Concatena los clips 1, 2 y 3.
- Mezcla la voz de narración al 100% con el audio ambiental al 18%.
- Renderiza los subtítulos dentro de la zona segura.
- Verifica con `freezedetect`:
  ```bash
  ffmpeg -i assets/day_08/videos/video_0N_FINAL.mp4 -vf "freezedetect=n=-55dB:d=2" -an -f null -
  ```
- Salida lista para revisión humana previa a publicación.
