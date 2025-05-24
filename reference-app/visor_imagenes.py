import os
import random
import time
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class RandomImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visor de Imágenes Aleatorias")

        # Frame para los controles
        self.frame_controls = tk.Frame(root)
        self.frame_controls.pack(fill=tk.X)

        # Botón para seleccionar carpeta
        self.btn_select_folder = tk.Button(self.frame_controls, text="Seleccionar Carpeta", command=self.select_folder)
        self.btn_select_folder.pack(side=tk.LEFT, padx=5, pady=5)

        # Botón para mostrar imagen aleatoria
        self.btn_random_image = tk.Button(self.frame_controls, text="Mostrar Imagen Aleatoria", command=self.show_random_image, state=tk.DISABLED)
        self.btn_random_image.pack(side=tk.LEFT, padx=5, pady=5)

        # Campo para ingresar el tiempo de cambio automático
        tk.Label(self.frame_controls, text="Cambio cada (s):").pack(side=tk.LEFT, padx=5)
        self.interval_var = tk.StringVar(value="5")  # Por defecto, 5 segundos
        self.entry_interval = tk.Entry(self.frame_controls, textvariable=self.interval_var, width=5)
        self.entry_interval.pack(side=tk.LEFT, padx=5)

        # Botón para activar/desactivar cambio automático
        self.auto_change = False
        self.btn_toggle_auto = tk.Button(self.frame_controls, text="Iniciar Auto", command=self.toggle_auto_change)
        self.btn_toggle_auto.pack(side=tk.LEFT, padx=5, pady=5)

        # Contador de tiempo restante
        self.countdown_label = tk.Label(self.frame_controls, text="Próximo cambio en: -")
        self.countdown_label.pack(side=tk.LEFT, padx=10)

        # Lienzo para mostrar la imagen
        self.canvas = tk.Label(root)
        self.canvas.pack(expand=True, fill=tk.BOTH)

        self.image_folder = None
        self.image_paths = []
        self.current_image = None  # Guarda la imagen original
        self.auto_task = None  # Guarda la tarea programada
        self.countdown_task = None  # Guarda el contador

        self.start_time = None  # Marca de tiempo de inicio
        self.interval_seconds = 5  # Segundos entre cambios

        # Evento para redimensionar la imagen cuando cambia el tamaño de la ventana
        self.root.bind("<Configure>", self.resize_image)

        # Atajo de teclado para salir de pantalla completa
        self.root.bind("<Escape>", self.exit_fullscreen)

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.image_folder = folder
            # Buscar imágenes en la carpeta y subcarpetas
            self.image_paths = []
            for root, _, files in os.walk(folder):
                for file in files:
                    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                        self.image_paths.append(os.path.join(root, file))

            if self.image_paths:
                self.btn_random_image.config(state=tk.NORMAL)
                self.btn_toggle_auto.config(state=tk.NORMAL)
            else:
                self.btn_random_image.config(state=tk.DISABLED)
                self.btn_toggle_auto.config(state=tk.DISABLED)

    def show_random_image(self):
        if not self.image_paths:
            return

        image_path = random.choice(self.image_paths)
        self.current_image = Image.open(image_path)  # Guarda la imagen original
        self.update_displayed_image()

        self.root.attributes('-fullscreen', True)  # Modo pantalla completa

    def update_displayed_image(self):
        if self.current_image:
            # Obtener tamaño de la ventana y restar la altura de los controles
            window_width = self.root.winfo_width()
            window_height = self.root.winfo_height() - self.frame_controls.winfo_height()

            # Redimensionar la imagen manteniendo proporción
            resized_image = self.current_image.copy()
            resized_image.thumbnail((window_width, window_height))

            # Convertir a formato compatible con Tkinter
            photo = ImageTk.PhotoImage(resized_image)

            # Mostrar la imagen
            self.canvas.config(image=photo)
            self.canvas.image = photo  # Mantener referencia

    def resize_image(self, event=None):
        """ Redimensiona la imagen cuando cambia el tamaño de la ventana """
        self.update_displayed_image()

    def exit_fullscreen(self, event=None):
        """ Sale del modo pantalla completa """
        self.root.attributes('-fullscreen', False)

    def toggle_auto_change(self):
        """ Activa o desactiva el cambio automático de imágenes """
        if self.auto_change:
            self.auto_change = False
            self.btn_toggle_auto.config(text="Iniciar Auto")
            self.countdown_label.config(text="Próximo cambio en: -")
            if self.auto_task:
                self.root.after_cancel(self.auto_task)  # Detener el cambio automático
            if self.countdown_task:
                self.root.after_cancel(self.countdown_task)  # Detener el contador
        else:
            self.auto_change = True
            self.btn_toggle_auto.config(text="Detener Auto")
            self.schedule_next_image()

    def schedule_next_image(self):
        """ Programa la próxima imagen aleatoria y reinicia el contador """
        if self.auto_change and self.image_paths:
            self.show_random_image()
            try:
                self.interval_seconds = int(self.interval_var.get())  # Obtener segundos del input
            except ValueError:
                self.interval_seconds = 5  # Valor por defecto si la entrada no es válida

            self.start_time = time.time()  # Guardar tiempo de inicio
            self.update_countdown()
            self.auto_task = self.root.after(self.interval_seconds * 1000, self.schedule_next_image)

    def update_countdown(self):
        """ Sincroniza el contador con el tiempo real usando timestamps """
        if self.auto_change:
            elapsed_time = time.time() - self.start_time
            remaining_time = max(0, int(self.interval_seconds - elapsed_time))

            self.countdown_label.config(text=f"Próximo cambio en: {remaining_time} s")

            if remaining_time > 0:
                self.countdown_task = self.root.after(500, self.update_countdown)  # Se actualiza cada 500ms para mayor precisión
            else:
                self.countdown_label.config(text="Próximo cambio en: -")

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomImageApp(root)
    root.mainloop()
