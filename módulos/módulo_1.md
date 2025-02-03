# Introducción a la programación

- [Conceptos básicos](#conceptos-básicos)
- [Python](#python)
- [Terminal](#terminal)
- [Visual Studio Code](#visual-studio-code)
- [Hola Mundo!](#hola-mundo)

## Conceptos básicos

### Programación

- Una **computadora** u **ordenador** es una máquina  capaz de seguir una serie de instrucciones u órdenes para procesar cierta información y devolver determinados resultados.
- La parte física de un ordenador se denomina **hardware**.
- La parte intangible de un ordenador se denomina **software**.
- El conjunto de instrucciones dadas a un ordenador se denomina **programa**.
- De ahí que el conjunto de acciones para crear, mantener o garantizar el funcionamiento de un programa se denomina **programación**.
- Y el ente ejecutor de tales acciones es el **programador**.

### Lenguaje de programación

- Así como el lenguaje humano que nos permite comunicarnos entre sí, para comunicarse con el ordenador se usa un tipo especial de lenguaje.
- Un **lenguaje de programación** es cualquier lenguaje formal que nos permite comunicar al ordenador el conjunto de instrucciones o programa que debe ejecutar.
- El ordenador entiende sólo el denominado **lenguaje** o **código máquina**, el cual se compone sólo de números 0 y 1 (sistema binario).
- Aunque su representación se realiza generalmente en sistema hexadecimal.
- El ordenador no entiende un lenguaje de programación directamente, por ello deben ser traducidos al código máquina con algún procedimiento de **compilación** o **interpretación**.

### Nivel del lenguaje

- Se denomina **lenguaje de bajo nivel** al que sus instrucciones permiten controlar de manera directa el hardware del ordenador. Por ejemplo los lenguajes **ensamblador**.
- Se denomina **lenguaje de alto nivel** al que sus instrucciones se adecúan más al lenguaje humano, por lo general tienen muy poco o nulo control directo sobre el hardware. Por ejemplo **Python**.
- Se denomina **lenguaje de medio nivel** al que con una sintaxis de alto nivel, permite cierto control directo sobre el hardware. Por ejemplo **C**.

## Python

### Características

- Lenguaje de programación de alto nivel.
- Lenguaje de programación **multiparadigma** y **multiplataforma**.
- Sintaxis simple, muy adecuada para introducirse en la programación.
- Es **open source** o de **código abierto**.
- Es **interpretado**, de **tipado dinámico** y **tipado fuerte**.
- Y muy versátil, para aplicaciones de escritorio, servidores y aplicaciones web.

### Instalación

- Descargar la última versión de la página oficial de [Python](https://www.python.org/).
- Asegurarse de agregar al **PATH** en el proceso de instalación.
- Confirmar la versión instalada en alguna terminal:

```sh
python --version
```

## Terminal

### Definiciones

- Una **terminal** es un dispositivo que nos permite interactuar directamente con el ordenador, el sistema operativo o sus aplicaciones.
- Una **terminal de texto** es una terminal compuesta de una pantalla y un teclado. Generalmente se interactúa a través de **caracteres** alfanuméricos.
- Un **emulador de terminal** (de texto) es una aplicación dentro de una interfaz gráfica que simula una terminal de texto. Comúnmente al hablar de terminal nos referiremos a este tipo de aplicación.
- La **shell** es la aplicación que nos permite interactuar con el sistema operativo interpretando los comandos ingresados.
- Una **consola** es una sesión de la shell.
- Una **CLI** (Command Line Interface) es una interfaz que usa una terminal para su operación.

### Formato general

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

### Comandos básicos

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
- La tecla **tabulador** permite navegar por las carpetas o archivos de la ubicación actual.

## Visual Studio Code

### Instalación

- Descargar de la página oficial de [Visual Studio Code](https://code.visualstudio.com/).
- Asegurarse de agregar al **PATH** en el proceso de instalación.
- Instalar la extensión [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) de Microsoft.
- Comandos en el terminal:

```sh
# Versión instalada
code --version

# Ayuda
code -h

# Abrir aplicación
code

# Abrir archivo en VSC
code nombre-del-archivo
```

### Combinaciones de teclas útiles

- `Flechas del teclado` → Para mover cursor entre caracteres
- `Shift + flechas` → Para seleccionar código entre caracteres o líneas
- `Ctrl + flechas izquierda o derecha` → Para mover cursor entre palabras del código
- `Ctrl + flechas arriba o abajo` → Para crear una copia del cursor
- `Alt + click` → Para crear una copia del cursor
- `Alt + flechas arriba o abajo` → Para mover una línea completa
- `Alt + Shift + flechas arriba o abajo` → Para crear una copia de una línea completa
- `Alt + Shift + U` → Convierte en mayúsculas lo seleccionado
- `Alt + Shift + L` → Convierte en minúsculas lo seleccionado
- `Alt + Shift + T` → Convierte la primera letra de cada palabra en mayúscula
- `Ctrl + D` → Selecciona la siguiente coincidencia de los caracteres seleccionados
- `Ctrl + SpaceBar` → Muestra sugerencias de autocompletado
- `Ctrl + Ñ` → Muestra la terminal de VSC

## Hola Mundo!

- Programa simple que se usa para verificar la disponibilidad y funcionamiento de un lenguaje.
- Un código python tiene como extensión **`.py`**

```py
print( "Hola Mundo!" )
```

- `print()` → Función que permite escribir en consola el valor dado
- `"Hola Mundo!"` → Valor del tipo **string** que se mostrará en consola
