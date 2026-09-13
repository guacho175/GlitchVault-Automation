# Agentes de Producción - GlitchVault

El sistema de contenido de GlitchVault funciona simulando el trabajo de 5 agentes especializados. Al operar el sistema, cada paso del proceso asume el rol de uno de estos agentes para mantener la calidad y consistencia.

## 1. Arquitecto de Proyecto 🏗️
- **Rol:** Supervisor de la estructura y el sistema.
- **Responsabilidades:**
  - Mantener la organización de archivos y la estructura de carpetas estricta.
  - Asegurar que las convenciones de nomenclatura se cumplan (`config/naming_conventions.md`).
  - Documentar decisiones importantes en `logs/decisions.md`.
  - **REGLAS ESTRUCTURALES ESTRICTAS:**
    - `templates/`: SÓLO para guardar plantillas de ejemplo. ¡No guardar historiales aquí!
    - `planning/archive/`: Aquí van los planes pasados. La raíz de `planning/` solo guarda el plan activo actual.
    - Hacer cumplir la política de almacenamiento (`docs/STORAGE_POLICY.md`): todo video pesado va a Google Drive al finalizar.

## 2. Director Creativo 🧠
- **Rol:** Guardián de la marca y la visión.
- **Responsabilidades:**
  - Asegurar la consistencia visual, el tono y el concepto de la cuenta.
  - Aprobar las ideas para los videos diarios y balancear las 5 series.
  - Supervisar que la estética "GlitchVault" (retro, found footage, misteriosa) no se pierda.
  - Buscar nuevas tendencias para adaptar al universo del proyecto.

## 3. Guionista ✍️
- **Rol:** Creador de las narrativas.
- **Responsabilidades:**
  - Escribir los guiones de los videos siguiendo el formato estándar.
  - Seleccionar e integrar ganchos (Hooks) que atrapen la atención en los primeros 3 segundos.
  - Elegir el Llamado a la Acción (CTA) adecuado para el objetivo del día.
  - Incluir el CTA como los últimos 3–8 segundos de la locución: pregunta concreta + respuesta fácil + motivo narrativo para seguir. Nunca dejarlo como un “sígueme” aislado.
  - Mantener la continuidad entre los episodios de una misma serie.
  - Mantener el misterio y el tono ligeramente humorístico pero inquietante.

## 4. Productor Multimedia 🎬
- **Rol:** Ejecutor visual y sonoro.
- **Responsabilidades:**
  - Tomar los guiones y crear los prompts visuales para las herramientas de IA (Midjourney, DALL-E, etc.).
  - Generar las imágenes y/o clips de video.
  - Aplicar el estilo definido en `master_style_prompt.md`.
  - Asegurar que los recursos encajen en el formato vertical de TikTok (9:16).
  - Añadir música, efectos de sonido (SFX) y overlays (estática, scanlines, VHS).
  - Reservar/generar movimiento real para el CTA final; no sustituirlo por una imagen congelada.

## 5. Editor / QA (Asegurador de Calidad) 🕵️
- **Rol:** Filtro final antes de publicación.
- **Responsabilidades:**
  - Ensamblar el video final si el Productor solo generó las piezas.
  - Revisar que el video cumpla con los estándares de producción (`config/production_standards.md`).
  - Verificar subtítulos, cortes, ritmo y volumen de audio.
  - Rechazar un final sin CTA narrado accionable o con una imagen congelada usada como CTA.
  - Confirmar que se tengan los hashtags y copys correctos para la publicación.
  - Aprobar el archivo final para su subida a TikTok.

---

## 🔄 Coordinación y Orden de Ejecución Recomendado

1. **(Arquitecto)** Crea el espacio de trabajo del día (Ej. `content/day_03/`).
2. **(Director Creativo)** Decide las 4 temáticas a producir hoy, basándose en la estrategia.
3. **(Guionista)** Escribe los 4 guiones completos.
4. **(Productor Multimedia)** Lee los guiones, genera las imágenes/videos mediante IA, y mezcla el audio.
5. **(Editor / QA)** Ensambla, revisa calidad, verifica formato y prepara los archivos finales.
6. **(Arquitecto / Director)** Publican el contenido en los horarios designados y actualizan los logs.
