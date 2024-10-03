import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Importar Pillow para cargar imágenes
from logica_eneagrama import LogicaEneagrama

class CuestionarioEneagrama:
    def __init__(self, root):
        self.root = root
        self.logica = LogicaEneagrama()
        self.root.title("Cuestionario Eneagrama")
        self.root.geometry("600x400")

        # Inicializar puntajes para cada eneatipo (ejemplo: 9 eneatipos)
        self.score = [0] * 9  # Array para acumular puntos por eneatipo

        # Cargar la imagen de fondo
        self.bg_image = Image.open("C:\\Users\\rocio\\Documents\\Otros programas\\cuestionario_eneagrama\\eneagrama3.jpg")
        self.bg_image = self.bg_image.resize((600, 400))  # Redimensionar la imagen
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Crear un Canvas para poner la imagen de fondo
        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack(fill="both", expand=True)

        # Colocar la imagen en el Canvas
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Crear widgets sobre el Canvas
        self.current_question = 0

        # Etiqueta de la pregunta
        self.question_label = tk.Label(self.root, text=self.logica.preguntas[self.current_question][0], wraplength=400, bg="white")
        self.canvas.create_window(300, 100, window=self.question_label)  # Posición de la etiqueta en el Canvas

        # Botón "Sí"
        self.si_button = tk.Button(self.root, text="Sí", command=lambda: self.responder(1))
        self.canvas.create_window(200, 300, window=self.si_button)  # Posición del botón en el Canvas

        # Botón "No"
        self.no_button = tk.Button(self.root, text="No", command=lambda: self.responder(0))
        self.canvas.create_window(400, 300, window=self.no_button)  # Posición del botón en el Canvas

    def responder(self, respuesta):
        # Asegurarse de que no se exceda el número de preguntas
        if self.current_question < len(self.logica.preguntas):
            eneatipo = self.logica.preguntas[self.current_question][1]  # Obtener el eneatipo asociado
            self.score[eneatipo - 1] += respuesta  # Sumar el puntaje basado en la respuesta

            # Avanzar a la siguiente pregunta
            self.current_question += 1
            if self.current_question < len(self.logica.preguntas):
                self.question_label.config(text=self.logica.preguntas[self.current_question][0])
            else:
                self.mostrar_resultado()
        else:
            self.mostrar_resultado()

    def mostrar_resultado(self):
        # Obtener los eneatipos con mayor puntuación, en orden descendente
        eneatipos_ordenados = sorted(range(len(self.score)), key=lambda i: self.score[i], reverse=True)
        
        # Preguntar al usuario si se identifica con el eneatipo más alto
        self.preguntar_identificacion(eneatipos_ordenados, 0)

    def preguntar_identificacion(self, eneatipos_ordenados, indice_actual):
        if indice_actual >= len(eneatipos_ordenados):
            messagebox.showinfo("Fin", "No te has identificado con ningún eneatipo.")
            self.root.quit()
            return

        # Eneatipo actual (el más alto según el índice)
        eneatipo_mayor = eneatipos_ordenados[indice_actual] + 1

        # Definir las palabras clave para cada eneatipo
        palabras_clave = {
            1: ["Perfeccionista", "Crítico", "Organizado"],
            2: ["Ayudador", "Empático", "Generoso"],
            3: ["Triunfador", "Competitivo", "Ambicioso"],
            4: ["Individualista", "Emocional", "Creativo"],
            5: ["Investigador", "Analítico", "Reservado"],
            6: ["Leal", "Cauteloso", "Confiable"],
            7: ["Entusiasta", "Optimista", "Espontáneo"],
            8: ["Desafiador", "Autoritario", "Protector"],
            9: ["Pacificador", "Tranquilo", "Adaptable"]
        }

        # Descripciones de cada eneatipo
        descripciones = {
            1: "Eneatipo 1 (El Perfeccionista): Personas organizadas, detallistas y disciplinadas, con un fuerte sentido del bien y del mal.",
            2: "Eneatipo 2 (El Ayudador): Personas empáticas que encuentran su felicidad ayudando a otros y siendo necesitadas.",
            3: "Eneatipo 3 (El Triunfador): Ambiciosos y orientados al éxito, buscan reconocimiento por sus logros.",
            4: "Eneatipo 4 (El Individualista): Personas emotivas que valoran la autenticidad y se ven a sí mismas como únicas.",
            5: "Eneatipo 5 (El Investigador): Reflexivos y analíticos, disfrutan de la soledad y el conocimiento.",
            6: "Eneatipo 6 (El Leal): Leales, responsables y cautelosos, a veces propensos a la ansiedad y la indecisión.",
            7: "Eneatipo 7 (El Entusiasta): Optimistas, espontáneos y enérgicos, disfrutan de las aventuras y la diversión.",
            8: "Eneatipo 8 (El Desafiador): Fuertes y protectores, no temen a la confrontación y buscan el control.",
            9: "Eneatipo 9 (El Pacificador): Tranquilos y amables, buscan la paz y evitan el conflicto."
        }

        # Mostrar las palabras clave y la descripción del eneatipo
        palabras = ", ".join(palabras_clave[eneatipo_mayor])
        descripcion = descripciones[eneatipo_mayor]
        identificacion = messagebox.askyesno(
            "Identificación",
            f"Tu eneatipo es el {eneatipo_mayor}.\nPalabras clave: {palabras}\n\n{descripcion}\n\n¿Te sientes identificado?"
        )

        if identificacion:
            # Si el usuario se identifica, finalizar el programa
            messagebox.showinfo("Identificación", f"Te has identificado con el eneatipo {eneatipo_mayor}.")
            self.root.quit()
        else:
            # Si no se identifica, pasar al siguiente eneatipo en la lista
            self.preguntar_identificacion(eneatipos_ordenados, indice_actual + 1)


if __name__ == "__main__":
    root = tk.Tk()
    app = CuestionarioEneagrama(root)
    root.mainloop()
