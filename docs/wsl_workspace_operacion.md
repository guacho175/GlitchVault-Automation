# Espacio de trabajo WSL para automatización del navegador

## Propósito

La automatización de Chrome de Codex falló cuando esta tarea se ejecutó desde
`/mnt/c/...`: el puente de navegador rechazó el `sandboxCwd` antes de conectar
con la extensión. Para conservar el agente en WSL se usará una copia operativa
del proyecto en el sistema de archivos Linux.

## Fuente y destino

- Fuente preservada: `C:\\Users\\galin\\OneDrive\\Documentos\\Tiktok`
- Copia operativa: `/home/galin/workspaces/Tiktok`

La copia no sustituye ni elimina la fuente. Se excluyen perfiles de navegador,
cachés y dependencias instaladas porque pueden contener sesiones autenticadas y
no son necesarios para usar la extensión de Chrome ya conectada por el usuario.

## Verificación requerida

Abrir la copia como proyecto WSL desde `\\\\wsl$\\Debian\\home\\galin\\workspaces\\Tiktok`,
manteniendo el agente configurado en WSL. La nueva tarea debe reportar un
directorio de trabajo bajo `/home/galin/workspaces/Tiktok`; solo entonces se
reintenta el puente de Chrome y la programación de YouTube.
