# Prompt de traspaso — Rehabilitación CTA del Día 1

Copia desde aquí hasta el final en un chat nuevo:

---

Trabaja exclusivamente en `C:\Users\galin\OneDrive\Documentos\Tiktok` para aplicar la rehabilitación CTA **solo al Día 1**. No toques los Días 2, 3 ni 4 y no publiques nada en TikTok.

Lee por completo, antes de modificar archivos:

1. `AGENTS.md`
2. `config/production_standards.md`
3. `scripts/AUTOMATION_PLAYBOOK.md`
4. `WORKFLOW.md`
5. `planning/hooks/cta_bank.md`
6. `docs/day_01_to_day_03_cta_retrofit_plan.md`
7. Los cuatro guiones de `scripts/day_01/`

Revisa el estado/diff de Git si existe repositorio; actualmente no hay uno. Conserva los MP4 publicados y no sobrescribas ni borres ningún archivo actual.

## Alcance y orden estricto

Procesa un video por vez, en este orden: **Video 4**, Video 1, Video 2 y Video 3. No empieces el siguiente hasta que el actual tenga su MP4 CTA, QA y documentación actualizada. No uses subagentes ni ejecutes varios videos en paralelo.

El Video 4 es el primero porque tiene 30 vistas. El Video 3 queda último: fue el mejor del lote (2.122 vistas) y sirve como referencia, pero igualmente recibirá su CTA al final de la fase.

## Intervención permitida

Para cada video, conserva por completo su `video_0N_FINAL.mp4` o su versión final aprobada y añade solo un cierre de 3–8 segundos. El cierre debe incluir:

1. Nueva locución TTS Algenib: pregunta concreta + palabra/opción fácil de comentar + motivo narrativo para seguir la cuenta.
2. Texto breve en safe zone que refuerce esa acción.
3. Metraje con movimiento real durante todo el CTA.

Ejemplo de estructura: “¿[pregunta]? Comenta [PALABRA]. Si quieres [próximo archivo/nivel], sígueme.” No termines solo con “sígueme”.

Usa primero los `hero_clip`, `continuation_raw` y finales ya guardados en `assets/day_01/videos/`. Si un cierre necesita mejor movimiento, puedes usar la habilidad `chrome:control-chrome` solo para revisar/descargar una variante **ya generada** desde el historial de Flow; el proyecto histórico del Día 1 conserva variantes de NPC, Leviatán, perro y palomas, y hay una tercera variante de palomas no guardada localmente. No generes clips nuevos en Flow ni gastes créditos.

Nunca uses `tpad`, un fotograma congelado o una endcard estática para el CTA. Una marca/logo incidental no es razón para descartar un clip que sirve.

## Archivos y QA

- Guardar la nueva voz como `assets/day_01/audio_notes/video_0N_cta_retrofit.wav`.
- Entregar un archivo nuevo: `assets/day_01/videos/video_0N_FINAL_CTA_v1.mp4` (incrementa la versión si ya existe).
- Validar cada video con `ffprobe`, `freezedetect` y tres capturas del CTA. Confirmar 1080×1920, 30 fps, audio presente, texto legible y movimiento continuo.
- Actualizar el guion correspondiente, `planning/weekly_plan/day_01.md` y `logs/decisions.md` tras cada video terminado.

Al finalizar el Día 1, entrega rutas absolutas, duración, CTA exacta, material reciclado y evidencia de QA. No empieces el Día 2: ese trabajo se abrirá en otro chat.
