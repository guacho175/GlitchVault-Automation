# Guía de Solución de Problemas para Automatización de YouTube Studio

Esta guía documenta los problemas encontrados y las soluciones implementadas al automatizar la subida de videos a YouTube Studio usando Playwright/Puppeteer, para evitar que futuros agentes cometan los mismos errores.

## 1. Conexión al Navegador Abierto del Usuario (Modo Depuración)
Si el usuario indica que "el navegador ya está abierto en modo depuración" o que "hay que usar la extensión del navegador":
- **NO** uses `launch_persistent_context`. Esto iniciará un navegador oculto en Session 0 o fallará si el perfil ya está en uso.
- **SÍ** usa `connect_over_cdp` hacia el WebSocket activo del usuario.
- **Cómo obtener el WebSocket:** El puerto suele ser `9222`, pero el endpoint cambia. Lee el archivo `DevToolsActivePort`:
  ```python
  port_file = os.path.join(os.environ['LOCALAPPDATA'], 'Google', 'Chrome', 'User Data', 'DevToolsActivePort')
  with open(port_file, 'r') as f:
      lines = f.read().strip().split('\n')
      ws_endpoint = f"ws://127.0.0.1:{lines[0]}{lines[1]}"
  
  browser = await p.chromium.connect_over_cdp(ws_endpoint)
  ```

## 2. Limpieza de Cajas de Texto (Títulos y Descripciones)
YouTube usa `divs` con `contenteditable` para los campos de texto (`#textbox`).
- **Problema:** Simular `Control+A` y `Backspace` muchas veces falla, lo que causa que el nuevo título se concatene con el nombre del archivo (ej. `video_01_mechanicus... POV: Tu vida...`).
- **Solución:** Vacía el contenido manipulando el DOM directamente antes de hacer `.fill()`:
  ```python
  title_box = page.locator('#textbox').nth(0)
  await title_box.click()
  await title_box.evaluate("el => el.textContent = ''")
  await title_box.fill("Nuevo Título")
  ```

## 3. Seleccionar el Botón de Programar
- **Problema:** Usar `document.querySelector('#schedule-radio-button')` mediante `page.evaluate()` puede devolver `null` debido a que YouTube usa Web Components con Shadow DOM.
- **Solución:** Usa el localizador nativo de Playwright, que penetra automáticamente los Shadow DOM y espera a que el elemento sea visible. Además, incluye un selector de respaldo:
  ```python
  schedule_radio = page.locator('#schedule-radio-button, tp-yt-paper-radio-button[name="SCHEDULE"]').first
  await schedule_radio.wait_for(state="visible", timeout=30000)
  await schedule_radio.click()
  ```

## 4. Esperar a que el Video se Suba
- **Problema:** Avanzar demasiado rápido a la última pestaña y presionar "Programar" puede hacer que YouTube bloquee la acción o que se buguee porque el video sigue subiéndose (`Subiéndose: X%`). El proceso se queda atascado y requiere intervención manual.
- **Solución:** Espera explícitamente a que el texto "Subiéndose:" desaparezca del DOM antes de hacer clic en "Siguiente" por primera vez.
  ```python
  # Esperar hasta 5 minutos a que desaparezca el estado de subiendo
  await page.wait_for_function("!document.body.innerText.includes('Subiéndose:')", timeout=300000)
  ```
