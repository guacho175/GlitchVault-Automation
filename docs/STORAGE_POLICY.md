# Política de Almacenamiento y Renderizado (Storage Policy)

> **ATENCIÓN A FUTUROS AGENTES:** Esta política es obligatoria para mantener el disco duro local optimizado.

## Flujo de Trabajo Multimedia

1. **Construcción Local:**
   Toda la creación de scripts, generación de audios (TTS), procesamiento con FFmpeg y ensamblaje de videos debe realizarse de manera **LOCAL** en la carpeta `assets/` dentro del proyecto.

2. **Migración a Drive (Al Finalizar):**
   Una vez que un lote de videos haya sido renderizado, subido a YouTube (o programado), y el proceso haya concluido, **NO** deben dejarse los videos pesados en el disco local.
   
   Todos los archivos pesados deben ser movidos a la ruta de Google Drive:
   `C:\Users\galin\OneDrive\Documentos\GOOGLE-DRIVE\GlitchVault\`

   Específicamente:
   - Videos Finales MP4 -> `GOOGLE-DRIVE\GlitchVault\Videos_Publicados`
   - Miniaturas -> `GOOGLE-DRIVE\GlitchVault\Miniaturas`
   - Banco de Clips Crudos -> `GOOGLE-DRIVE\GlitchVault\Banco_Crudos` (Si se generan nuevos).

3. **Limpieza de Temporales:**
   - Eliminar siempre los audios temporales (`.wav`) que se hayan generado, ya que pueden volver a generarse sin costo usando Microsoft Edge-TTS.
   - Eliminar las carpetas vacías dentro de `assets/` tras realizar la mudanza.
