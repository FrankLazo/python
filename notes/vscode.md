# Visual Studio Code

## Instalación

- Descargar de la página oficial de [Visual Studio Code](https://code.visualstudio.com/).
- Asegurarse de agregar al **PATH** en el proceso de instalación.
- Instalar la extensión [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) de Microsoft.

## Comandos en la terminal

- Versión instalada

```sh
code --version
```

- Temas de ayuda

```sh
code -h
```

- Abrir aplicación

```sh
code
```

- Abrir archivo en VSC

```sh
code nombre-del-archivo
```

## Combinaciones de teclas útiles

### Movimiento del cursor

- `←` `→` → Mover cursor carácter por carácter
- `↑` `↓` → Mover cursor línea por línea
- `Ctrl + ←` `Ctrl + →` → Mover cursor palabra por palabra
- `Inicio` → Mover cursor al principio de la línea
- `Fin` → Mover cursor al final de la línea
- `Ctrl + Inicio` → Mover cursor al principio del código
- `Ctrl + Fin` → Mover cursor al final del código
- `Alt + ←` → Mover cursor a una posición anterior
- `Alt + →` → Mover cursor a una posición más actual

### Creación de multicursor

- `Alt + click` → Crear una copia del cursor
- `Ctrl + ↑` `Ctrl + ↓` → Crear una copia del cursor en la misma posición de una línea adyacente

### Selección de código

- `Shift + →` `Shift + ←` → Seleccionar código carácter por carácter
- `Shift + ↑` `Shift + ↓` → Seleccionar código línea por línea
- `Shift + Ctrl + →` `Shift + Ctrl + ←` → Seleccionar código palabra por palabra
- `Ctrl + D` → Seleccionar la siguiente coincidencia de los caracteres seleccionados y al mismo tiempo crea un nuevo cursor

### Edición de código

- `Alt + ↑` `Alt + ↓` → Mover una línea completa
- `Alt + Shift + ↑` `Alt + Shift + ↓` → Copiar una línea completa
- `Alt + Shift + U` → Convierte en mayúsculas el código seleccionado
- `Alt + Shift + L` → Convierte en minúsculas el código seleccionado
- `Alt + Shift + T` → Convierte la primera letra de cada palabra en mayúscula
- `Ctrl + SpaceBar` → Mostrar sugerencias de autocompletado

### Interfaz

- `Ctrl + B` → Mostrar/ocultar barra lateral
- `Ctrl + Ñ` → Mostrar/ocultar terminal
- `Alt + Z` → Mostrar/ocultar multilíneas de código
