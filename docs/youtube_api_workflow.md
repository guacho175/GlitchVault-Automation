# Workflow Definitivo para Subir a YouTube por API

Debido a los constantes fallos de la interfaz de YouTube Studio (Shadow DOM, popups de "Abandonar sitio", cambios de diseño, etc.), **está estrictamente prohibido automatizar la subida de videos a YouTube usando Playwright o simulando clics en el navegador.**

Todas las subidas a YouTube deben realizarse usando la YouTube Data API v3 a través de scripts de Python.

## El Script: `youtube_uploader_api.py`
Se ha creado un script base en la raíz (`youtube_uploader_api.py`) que:
1. Lee las credenciales de `credentials.json` y los tokens de `token.json` (que incluyen permisos de lectura y escritura).
2. Sube el archivo `.mp4` en ráfaga (Resumable Upload).
3. Sube la miniatura correspondiente `.jpg` en la misma ejecución utilizando el endpoint `youtube.thumbnails().set()`.
4. Programa el video (`publishAt`) como `private`.

## Pasos para el Agente (Cuando tengas que subir un nuevo día)
1. Modifica las rutas en `youtube_uploader_api.py` para que apunten a la carpeta del nuevo día (Ej: `day_09`).
2. Asegúrate de extraer bien los Títulos, Descripciones y Hashtags de los archivos `.md`.
3. Ejecuta `python youtube_uploader_api.py`. ¡El script se encargará de los videos y las miniaturas a la vez sin abrir el navegador!

## Sobre las Miniaturas en YouTube Shorts
Recuerda: YouTube a veces ignora las miniaturas personalizadas de los Shorts en la interfaz de usuario de los teléfonos o en el "Shelf" de Shorts. Sin embargo, la API siempre sube la imagen y la ancla a los metadatos del video exitosamente. No intentes re-subir miniaturas infinitamente si la API devolvió un código 200 OK.
