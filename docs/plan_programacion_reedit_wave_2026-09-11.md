# Plan de programación — ola de reedición GlitchVault

**Estado:** pendiente de aprobación explícita. No se ha publicado ni programado contenido con este plan.

## Base verificada

- Hay 22 videos finales pendientes en `assets/reedit_wave`; cada uno cuenta con MP4, miniatura JPG, narración, título y copy.
- El registro local `reedit_upload_log.json` está vacío.
- El destino es YouTube Studio, canal `@glitchvault_u`.
- El script existente `scripts/subir_reedit_wave.py` apunta a YouTube Studio, pero conserva la pauta anterior de 17:00/21:00; no se usará sin adaptar y verificar sus fechas y horarios.
- La captura del canal muestra caída reciente de alcance (3, 9, 95, 149, 287 y 494 visualizaciones en los últimos Shorts visibles). No atribuirla únicamente a la hora: se medirá por franja, pieza y retención disponible.

## Objetivo y cadencia

1. Publicar **A01** hoy, 11 de septiembre, inmediatamente después de la aprobación, como una publicación directa (no programada).
2. Desde el 12 de septiembre, programar **dos videos diarios** en hora de Chile:
   - **09:00** — prueba de mañana.
   - **23:30** — prueba nocturna tardía para gaming/misterio.
3. Sustituye de forma clara la pauta anterior de 17:00/21:00. Mantener ambas franjas constantes durante este lote permite evaluar horarios sin mezclarlos con otro cambio de calendario.
4. El día final tendrá una sola publicación, pues el lote contiene 22 piezas.

## Calendario propuesto

| Fecha | Hora CLT | ID | Activo | Acción |
|---|---:|---|---|---|
| 2026-09-11 | al aprobar | A01 | `01_perro_nivel_100` | Publicar directo |
| 2026-09-12 | 09:00 | A02 | `02_monturas_prohibidas` | Programar |
| 2026-09-12 | 23:30 | A03 | `03_armas_absurdas` | Programar |
| 2026-09-13 | 09:00 | A04 | `04_pokemon_cartucho_maldito` | Programar |
| 2026-09-13 | 23:30 | A05 | `05_mario_prototipo_oculto` | Programar |
| 2026-09-14 | 09:00 | A06 | `06_speedrun_sala_prohibida` | Programar |
| 2026-09-14 | 23:30 | B01 | `01_dona_carmen_fase2` | Programar |
| 2026-09-15 | 09:00 | B02 | `02_michi_nivel_1000` | Programar |
| 2026-09-15 | 23:30 | B03 | `03_espada_ruta_corrupta` | Programar |
| 2026-09-16 | 09:00 | B04 | `04_robot_protocolo_titan` | Programar |
| 2026-09-16 | 23:30 | C01 | `01_gta_paloma_el_golpe` | Programar |
| 2026-09-17 | 09:00 | C02 | `02_paloma_vs_dona_carmen` | Programar |
| 2026-09-17 | 23:30 | C03 | `03_michi_vs_perro_dioses` | Programar |
| 2026-09-18 | 09:00 | C04 | `04_leviatan_oceano_profundo` | Programar |
| 2026-09-18 | 23:30 | C05 | `05_servidor_ruso_disquete_maldito` | Programar |
| 2026-09-19 | 09:00 | C06 | `06_tren_metro_escuela_pesadilla` | Programar |
| 2026-09-19 | 23:30 | C07 | `07_planta_mutante_vs_robot` | Programar |
| 2026-09-20 | 09:00 | C08 | `08_sega_vs_pokemon_cartuchos` | Programar |
| 2026-09-20 | 23:30 | C09 | `09_payaso_carnaval_nina_glitch` | Programar |
| 2026-09-21 | 09:00 | C10 | `10_carreras_infernales_speedrun` | Programar |
| 2026-09-21 | 23:30 | C11 | `11_email_2003_npc_olvidado` | Programar |
| 2026-09-22 | 09:00 | C12 | `12_tetris_vivo_biblioteca_mortal` | Programar |

## Paquete obligatorio por publicación

Para cada ID se tomará el material correspondiente desde `assets/reedit_wave/package_*` y el texto exacto desde `descripciones_y_control/descripciones_shorts.docx`:

- Video final MP4.
- Título de YouTube Shorts en su campo independiente.
- Descripción completa, conservando el CTA y los hashtags del paquete.
- Miniatura `thumbnail/thumbnail.jpg` cargada como miniatura personalizada en YouTube Studio.
- Primer comentario anclado solo cuando ayude al lore; no sustituye el CTA del video.

## Ejecución y control de calidad tras aprobar

1. Abrir YouTube Studio con la extensión/navegador y verificar visualmente que el canal activo sea `@glitchvault_u` antes de actuar.
2. Revisar los Shorts programados en YouTube Studio para no duplicar un título, video o fecha que no figure en el log local.
3. Publicar A01 y comprobar en el canal que quedó público con video, miniatura, título, descripción y hashtags correctos.
4. Cargar y programar los otros 21 uno por uno, verificando antes de confirmar cada fila: archivo, fecha, hora CLT, caption y portada.
5. Guardar el identificador, fecha/hora y estado real de cada publicación en `reedit_upload_log.json`; no marcar un ítem como programado sin confirmación visible de YouTube Studio.
6. Tras 72 horas de cada franja, registrar vistas, retención, comentarios, compartidos y seguidores atribuibles. Si una franja queda consistentemente por debajo, reajustar solo el horario en el siguiente lote.

## Criterio de aprobación

La aprobación debe autorizar expresamente la publicación pública inmediata de A01 y la programación de las otras 21 filas en YouTube Studio, canal `@glitchvault_u`. Una vez aprobada, se usará la extensión del navegador y se detendrá ante cualquier cuenta distinta, fallo de miniatura o conflicto de programación.
