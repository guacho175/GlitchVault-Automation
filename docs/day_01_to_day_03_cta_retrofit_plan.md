# Plan de rehabilitación con CTA — Días 1 a 3

## Objetivo

Crear versiones nuevas de los 12 videos ya producidos de los días 1, 2 y 3 para mejorar la
conversión a comentarios y seguidores. Se preservan los MP4 publicados y se reutiliza material
existente; no se vuelve a producir cada video desde cero ni se publica automáticamente.

## Métricas incorporadas (capturas del 30-08-2026)

Las capturas muestran visualizaciones, fecha y comentarios. No muestran likes, retención ni
compartidos. La señal transversal más relevante es que todos los videos visibles tienen **0
comentarios**, salvo el primer video del Día 1 con 1; esto respalda probar el cierre de
conversión antes de cambiar por completo los conceptos visuales.

No se debe tratar como fallo definitivo un video publicado el 30 de agosto: necesita al menos
24–48 horas para compararlo con publicaciones del 19, 21, 23, 26 y 28 de agosto.

| Día | Video | Vistas | Interacciones | Prioridad | CTA propuesto |
| --- | --- | ---: | --- | --- | --- |
| 1 | 01 — juego del año | 1.221 | 1 comentario | Media | Pregunta ligada a su mundo + palabra/elección concreta |
| 1 | 02 — Leviatán del puerto | 1.418 | 0 comentarios | Media | Pregunta ligada a su mundo + palabra/elección concreta |
| 1 | 03 — NPC que nadie recuerda | 2.122 | 0 comentarios | Baja | Mantener como referencia creativa; rehabilitar después |
| 1 | 04 — Perro nivel 1→100 | 30 | 0 comentarios | **Muy alta** | Preguntar qué criatura llevar al nivel 100 + follow para la siguiente evolución |
| 2 | 01 — luchador callejero | 815 | 0 comentarios | Media | Elección concreta del personaje + follow para próxima selección |
| 2 | 02 — Minecraft del océano | 336 | 0 comentarios | Alta | Decisión de supervivencia + follow para otro mapa imposible |
| 2 | 03 — Doña Carmen | 1.352 | 0 comentarios | Media | Pregunta concreta de estrategia + follow para próximo boss |
| 2 | 04 — speedrun/cinta VHS | 164 | 0 comentarios | Alta | Pregunta de riesgo/decisión + follow para otro archivo |
| 3 | 01 — Michi al dios cósmico | 339 | 0 comentarios | Observación | Publicado el 30-08; esperar 24–48 h antes de priorizar |
| 3 | 02 — Es hora de ser el malo | 14 | 0 comentarios | Observación urgente | Publicado el 30-08; revisar de nuevo en 24–48 h y rehabilitar si no despega |
| 3 | 03 | No visible en captura | — | Pendiente | Pregunta ligada a su mundo + palabra/elección concreta |
| 3 | 04 | No visible en captura | — | Pendiente | Pregunta ligada a su mundo + palabra/elección concreta |

## Orden de trabajo recomendado

### Fase 1 — Un chat exclusivo para el Día 1

Procesar **solo** los cuatro videos del Día 1 y hacerlo secuencialmente: Video 4 (30 vistas),
Video 1, Video 2 y Video 3. No iniciar el siguiente hasta dejar terminado el anterior con su
MP4 CTA, QA y documentación. El Video 3 se procesa al final porque sus 2.122 vistas lo hacen
la mejor referencia visual del lote, no porque se deba descartar.

### Fase 2 — Otro chat exclusivo para el Día 2

Activar solo después de cerrar el Día 1. Orden interno: Video 4, Video 2, Video 1, Video 3.

### Fase 3 — Otro chat exclusivo para el Día 3

Esperar 24–48 h y capturar métricas actualizadas antes de abrirlo. No decidir por las 14 o 339
vistas del mismo día de publicación.

## Regla de intervención

1. Mantener sin cambios el corte narrativo y visual existente.
2. Añadir al final un segmento de **3 a 8 segundos**, como en
   `assets/day_04/videos/video_01_FINAL_v3.mp4`.
3. Añadir una locución TTS Algenib específica para el CTA: pregunta concreta + respuesta de baja
   fricción + recompensa narrativa de seguir la cuenta. Ejemplo: “¿Tú lo jugarías? Comenta
   OMEGA. Si quieres que abramos otro archivo, sígueme.”
4. Reutilizar clips ya presentes en `assets/day_01` a `assets/day_03` y, solo si aportan una
   mejora real, variantes históricas ya generadas que sigan archivadas en Flow. Recortar un tramo
   que conserve movimiento real; se permite reordenar solo ese cierre. No generar nuevos clips
   en Flow para esta rehabilitación.
5. No usar `tpad`, una imagen congelada ni una endcard estática para cubrir el CTA.
6. Un logo o marca incidental no es motivo para descartar material útil.
7. Crear un archivo nuevo sin sobrescribir ni borrar publicados: `video_0N_FINAL_CTA_v1.mp4`.
   Si ese nombre ya existe, subir el sufijo de versión.

## Inventario de reciclaje verificado

Primero se reutiliza el material local. Además, Flow conserva generaciones históricas que no
deben asumirse perdidas solo porque no estén en `assets/`.

| Lote | Material local reutilizable | Archivo histórico de Flow | Hallazgo |
| --- | --- | --- | --- |
| Día 1 | 4 `hero_clip` + 4 `continuation_raw` | 4 colecciones: NPC (2 variantes), Leviatán (2), perro astral (2), palomas (3) | Hay 9 variantes en Flow frente a 8 clips fuente locales. La tercera variante de palomas no está descargada localmente y se debe revisar como candidata al CTA. |
| Día 2 | 4 `hero_clip` + 1 `continuation_raw` | No se identificó un proyecto histórico correspondiente entre los proyectos visibles; los clips locales son la fuente inicial. | Revisar primero los hero clips y la continuación existente antes de buscar otro material. |
| Día 3 | 4 `hero_clip` | Flow conserva la colección de biblioteca cósmica y la de Tetris orgánico. | Sirven como respaldo descargable, aunque cada una muestra una sola variante visible y probablemente ya coincide con su hero clip local. |

### Fase 0 — Recuperación antes de editar

1. Comparar visualmente cada `hero_clip`, `continuation_raw` y el FINAL publicado para identificar
   los 3–8 segundos con más movimiento.
2. Abrir en Flow únicamente las variantes históricas relevantes; revisar miniatura, prompt y
   movimiento antes de descargar.
3. Descargar solo una variante cuando aporte un cierre mejor que el material local; esto no
   genera clips ni consume créditos de Flow.
4. Guardar el recuperado como `video_0N_recovered_variant_0N.mp4`, documentar su procedencia y
   usarlo únicamente para el segmento CTA.
5. Si el archivo ya existente ofrece movimiento suficiente, no descargar ni producir nada extra.

## Ejecución por video

1. Leer el guion original y definir un CTA distinto que corresponda a su serie.
2. Medir el `FINAL` con `ffprobe`; extraer y revisar varios fotogramas de los clips existentes
   (`hero_clip`, `continuation_raw` si existe y el final) para elegir 3–8 segundos animados.
3. Generar solo el WAV adicional: `audio_notes/video_0N_cta_retrofit.wav` con Algenib.
4. Crear el segmento CTA con texto en safe zone, voz clara y ambiente bajo.
5. Concatenar el `FINAL` existente y el segmento CTA, sin reensamblar los primeros segundos.
6. Validar cada nuevo MP4 con `ffprobe`, `freezedetect` y tres capturas del CTA.
7. Actualizar el guion, el plan diario y `logs/decisions.md` con el archivo resultante y la
   evidencia de QA.

## Entrega y publicación

- Entregar los MP4 nuevos por separado; los originales publicados no se borran, editan ni se
  sustituyen.
- No publicar en TikTok. La decisión de republicar y su calendario corresponde al usuario.
- Reportar qué material existente se reutilizó, la duración añadida, la CTA exacta y cualquier
  limitación real por falta de movimiento en los clips disponibles.

## Instrucción de traspaso para otro chat

Abrir un chat por día. El primer chat usa el prompt
`docs/day_01_cta_retrofit_handoff_prompt.md` y no toca Días 2–3. Cada chat posterior debe
mantener el mismo trabajo secuencial: no paralelizar videos, no empezar el siguiente antes del
QA/documentación del actual y no publicar en TikTok.
