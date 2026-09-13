# GlitchVault - Máquina de Contenido para TikTok

Bienvenido al repositorio central de **GlitchVault** (@GlitchVault_), un sistema de producción de contenido diseñado para dominar el algoritmo de TikTok mediante videos virales de misterio, rarezas visuales, y videojuegos que no existen, generados por inteligencia artificial.

## 🚀 Qué es este proyecto
Este proyecto funciona como una "fábrica" de contenido. En lugar de crear videos uno por uno sin rumbo, utilizamos un sistema estructurado con series definidas, un flujo de trabajo optimizado y un universo narrativo (el "vault" de los glitches) para captar la atención de los usuarios y construir una comunidad leal de gamers y entusiastas de lo extraño.

## 🎯 Objetivo Principal
El objetivo inmediato es **crecer la cuenta a 10,000 seguidores en el primer mes** publicando 4 videos diarios consistentes en estilo y calidad. El objetivo a largo plazo es construir una audiencia fiel para realizar **transmisiones en vivo de gaming** de forma exitosa.

## 📁 Estructura de Carpetas
El proyecto está organizado para separar la planificación, configuración y la producción diaria:

- `/`: Archivos principales de documentación (README, visión general, flujo, agentes).
- `/config`: Reglas del sistema, estándares de calidad, normas de publicación y convenciones de nombres.
- `/planning`: El cerebro creativo. Contiene bancos de ganchos (hooks), CTAs y detalles de cada una de las 5 series principales.
- `/prompts`: Prompts maestros y de sistema para garantizar que la IA siempre genere el mismo estilo visual (GlitchVault).
- `/logs`: Bitácoras de generación y registro de decisiones creativas y de proyecto.
- `/content`: (Generado diariamente) Aquí se organizan las subcarpetas de contenido diario (`day_01`, `day_02`, etc.) con sus guiones, audios, imágenes y videos exportados.

## 📅 Cómo usarlo en el día a día
1. **Revisar métricas y comentarios:** Inicia el día revisando qué funcionó ayer.
2. **Seleccionar las 4 ideas del día:** Ve a `CONTENT_STRATEGY.md` y a los archivos de `/planning/series` para elegir las ideas a producir. Asegúrate de rotar las series.
3. **Escritura (Agente Guionista):** Genera los guiones para los 4 videos. Usa los bancos de ganchos y CTAs en `/planning/hooks`.
4. **Generación (Agente Productor):** Ejecuta los prompts visuales basados en `/prompts/system/master_style_prompt.md`.
5. **Edición y Exportación:** Ensambla los recursos asegurando los estándares descritos en `/config/production_standards.md`.
6. **Publicación:** Publica siguiendo `/config/publishing_rules.md`.

## ➡️ Cómo continuar desde el Día 2 en adelante
La producción es un ciclo. A partir del Día 2:
1. Crea la carpeta `content/day_02/`.
2. Sigue el `WORKFLOW.md` para producir los 4 videos correspondientes.
3. Actualiza el `logs/generation_log.md`.
4. Revisa `TODO.md` para avanzar en las tareas semanales.
5. Sigue iterando. No reinventes la rueda, confía en el sistema y mantén la consistencia visual.

## ⚡ Guía rápida de inicio
- Lee **PROJECT_OVERVIEW.md** para entender el concepto.
- Revisa **BRAND_GUIDE.md** para empaparte del tono visual y narrativo.
- Ve a **WORKFLOW.md** cuando estés listo para producir tu primer video.
- **¡Empieza con la carpeta `day_01`!**
