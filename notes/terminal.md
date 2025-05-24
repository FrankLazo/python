# Terminal

## Definiciones

- Una **terminal** es un dispositivo que nos permite interactuar directamente con el ordenador, el sistema operativo o sus aplicaciones.
- Una **terminal de texto** es una terminal compuesta de una pantalla y un teclado. Generalmente se interactúa a través de **caracteres** alfanuméricos.
- Un **emulador de terminal** (de texto) es una aplicación dentro de una interfaz gráfica que simula una terminal de texto. Comúnmente al hablar de terminal nos referiremos a este tipo de aplicación.
- La **shell** es la aplicación que nos permite interactuar con el sistema operativo interpretando los comandos ingresados.
- Una **consola** es una sesión de la shell.
- Una **CLI** (Command Line Interface) es una interfaz que usa una terminal para su operación.

## Formato general

- Primero va el nombre de la aplicación o comandos a usar.
- A continuación puede ir uno o varios parámetros separados por espacios.
- Generalmente las opciones de operación de un comando inician con uno o dos guiones.

```sh
git commit -m "comentarios"
```

- `git` hace referencia a la aplicación Git.
- `commit` nombre del comando u órden a ejecutar.
- `-m` opción del comando.
- `"comentarios"` parámetro o valor que usará el comando.

## Comandos básicos

En PowerShell:

- `Get-Location` → Ruta de la carpeta actual
- `Set-Location C:\ruta\hacia\carpeta` → Cambia a la carpeta indicada
- `cd ..` → Cambia a la carpeta contenedora
- `cd \` → Cambia a la raíz del disco
- `cd ~` → Cambia a la carpeta del usuario (por defecto)
- `Get-ChildItem` → Muestra los archivos y carpetas de la ubicación actual
- `Start-Process` → Abrir archivo
- `Clear-Host` ó `cls` → Limpiar consola

En Bash:

- `pwd` → Ruta de la carpeta actual
- `cd C:\ruta\hacia\carpeta` → Cambia a la carpeta indicada
- `cd ..` → Cambia a la carpeta contenedora
- `cd /` → Cambia a la raíz del sistema
- `cd ~` → Cambia a la carpeta del usuario (por defecto)
- `ls` → Muestra los archivos y carpetas de la ubicación actual
- `clear`→ Limpiar consola

Algunas teclas útiles:

- Las **flechas arriba y abajo** permiten navegar por el historial de órdenes escritas.
- La tecla **tabulador** permite navegar por las carpetas o archivos de la ubicación actual o autocompletar sus nombres.
