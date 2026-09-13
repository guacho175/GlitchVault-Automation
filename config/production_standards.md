# Production Standards - Estándares de Producción

Para mantener la calidad y asegurar que la cuenta se vea profesional y consistente, todo video producido bajo el estandarte de **GlitchVault** debe pasar por este checklist antes de marcarse como final.

## 📏 Especificaciones de Video
- **Relación de Aspecto:** 9:16 (Vertical).
- **Resolución:** 1080x1920 píxeles.
- **Duración Mandatoria (Nueva Regla):** Ventana estricta de **30 a 60 segundos** por video final (nunca menos de 30 segundos). Se combinan entre 4 y 7 clips de Flow para cubrir la narración completa. Los videos de menos de 30s quedan prohibidos para asegurar máxima retención y desarrollo narrativo.
- **Cobertura animada obligatoria:** La duración de metraje con movimiento real debe cubrir toda la narración. Ejemplo: para una voz de 38 segundos se deben generar 5 clips de 8s (40 segundos de metraje animado).
- **Fotogramas estáticos solo como margen residual:** Se permite congelar el último fotograma únicamente para completar un desfase técnico breve, con un máximo de **2 segundos o 5% de la duración final (lo que sea menor)**. Ejemplo aprobado: 30 segundos animados + 2 segundos fijos para una narración de 32 segundos.
- **Prohibido usar `tpad=stop_mode=clone` como sustituto de clips:** Nunca completar bloques narrativos o varios segundos faltantes con una imagen congelada. Si falta cobertura, generar otro clip o una continuación antes de ensamblar.
- **Cierre orientado a comunidad (obligatorio):** Tras resolver la historia, reservar normalmente **3 a 8 segundos** para un CTA hablado y visible. Debe mantener metraje con movimiento real; una pantalla final congelada no es un CTA válido salvo el margen residual técnico ya definido.
- **CTA accionable:** Pedir una sola acción principal, concreta y de respuesta fácil (por ejemplo, comentar una palabra, elegir una opción o dar una teoría) y enlazar el seguimiento con una recompensa narrativa específica. Evitar terminar solo con “sígueme”.
- **Marcas en clips generados:** Un logo, nombre o interfaz de marca incidental no invalida un clip que funciona ni justifica gastar créditos en regenerarlo. Solo se corrige si rompe la historia, es un error visual material o el usuario pide excluir la marca.

## 🖼️ Especificaciones de Imagen
- **Fuente:** Imágenes de alta resolución de Midjourney u otro generador IA.
- **Composición:** Asegurar que el punto de interés principal esté en el centro vertical. Evita información importante en los bordes extremos (se cortan en pantallas diferentes).

## 🔊 Estándares de Audio
- **Balance General:** La voz (si la hay) debe ser el elemento más alto (-3dB a -6dB).
- **Música de Fondo:** Mantenerla entre el 20% y 30% del volumen general (-18dB a -24dB) para que no entorpezca la narración.
- **Efectos (SFX):** Los jumpscares o "glitches" pueden tener picos altos para sorprender, pero no distorsionar ni lastimar los oídos.
- **Loop Perfecto:** Intenta que el audio final del video pueda mezclarse sin interrupciones con el segundo cero.

## 🔠 Texto y Subtítulos (Overlays)
- **Tamaño:** Legible en pantallas pequeñas de celular.
- **Ubicación "Safe Zone":**
  - No colocar texto en el 20% inferior de la pantalla (donde va el caption y nombre de usuario).
  - No colocar texto en el margen derecho (donde están los botones de like, comentarios, compartir).
  - Ideal: Centro exacto de la pantalla o tercio superior centrado.
- **Longitud:** Máximo 2 líneas de texto en pantalla a la vez. El texto debe parpadear rápido si es código o consola.

## ✅ Quality Assurance Checklist (Final)
Antes de presionar exportar:
- [ ] ¿El primer segundo tiene un gancho visual que retenga?
- [ ] ¿Existe movimiento visual real durante toda la narración, salvo un margen residual permitido de máximo 2 segundos o 5%?
- [ ] ¿Se verificó con `freezedetect` que no haya congelamientos continuos fuera del margen permitido?
- [ ] ¿El texto respeta la 'Safe Zone' de TikTok?
- [ ] ¿Los colores encajan con la paleta de la Brand Guide?
- [ ] ¿Hay algún error visual obvio de la IA (manos raras, texto ilegible)? *Nota: Si es un error feo, ocúltalo con un efecto de Glitch.*
- [ ] ¿Se escucha clara la voz narrativa por encima de la música?
- [ ] ¿El cierre tiene un CTA hablado y legible de 3 a 8 segundos, con una pregunta/acción concreta y una razón narrativa para seguir la cuenta?
- [ ] ¿El clip se aprovecha si funciona visualmente, sin regenerar por una marca incidental?
