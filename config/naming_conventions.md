# Convenciones de Nomenclatura (Naming Conventions)

Para que el sistema de producción de GlitchVault fluya sin confusiones, es obligatorio seguir estas reglas al nombrar archivos y carpetas. **Evita usar espacios o caracteres especiales en los nombres de archivos.**

## 📂 Organización de Días
Las carpetas de contenido diario deben mantener un formato de dos dígitos:
- `day_01`
- `day_02`
- ...
- `day_10`

## 📝 Guiones y Textos
Formato: `video_[NUMERO_EN_DIA]_[SERIE_ID]_[NOMBRE_CORTO].md`
- `video_01_vj_no_existen_mario_gore.md`
- `video_02_bosses_entidad_nula.md`

## 🖼️ Imágenes (Assets Brutos)
Formato: `video_[NUMERO]_[TIPO]_[NUMERO_ESCENA].png`
- `video_01_scene_01.png`
- `video_01_scene_02_variation.png`
- `video_02_background_01.png`

## 🎥 Videos Exportados
Formato: `video_[NUMERO]_[ESTADO].mp4`
- `video_01_draft.mp4` (Borrador para revisión)
- `video_01_final.mp4` (Aprobado y listo para subir)

## 💬 Prompts (Instrucciones para IA)
Formato: `video_[NUMERO]_[TIPO]_prompt.md`
- `video_01_image_prompt.md`
- `video_02_video_prompt.md`
- `video_03_tts_script.txt` (Para generación de voz)

## 🗂️ Identificadores de Series (Para usar en nombres)
Utiliza estas versiones en `snake_case` corto para referenciar las series:
1. Videojuegos que no existen -> `vj_no_existen`
2. Bosses imposibles -> `bosses`
3. Archivos recuperados -> `archivos`
4. Evoluciones con IA -> `evoluciones`
5. Elige tu personaje -> `elige_pj`
