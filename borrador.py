import tkinter as tk
from tkinter import messagebox
from tkinter import font  # Importar el módulo font
from PIL import Image, ImageTk
from logica_eneagrama import LogicaEneagrama
import os

class CuestionarioEneagrama:
    def __init__(self, root):
        self.root = root
        
        # Cargar y configurar la imagen de fondo
        self.bg_image = Image.open(os.path.join(os.getcwd(),"eneagrama3.jpg"))
        self.bg_image = self.bg_image.resize((800, 600))  # Redimensionar la imagen a un tamaño adecuado
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        # Crear un label con la imagen de fondo
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Ajustar para que ocupe todo el espacio

        self.logica = LogicaEneagrama()
        self.root.title("Cuestionario Eneagrama")
        self.root.geometry("800x600")  # Establecer tamaño de la ventana
        self.current_question = 0
        self.score = [0] * 9  # Puntuación para los 9 eneatipos

        # Definir preguntas y relacionarlas con eneatipos (índices 0-8)
        self.preguntas = [
                    ("¿Te consideras una persona perfeccionista?", 0),
                    ("¿Tienes un fuerte sentido del bien y del mal?", 0),
                    ("¿Sueles fijarte en los errores que otros cometen?", 0),
                    ("¿Te resulta difícil relajarte si algo no está en orden?", 0),
                    ("¿Te consideras disciplinado y organizado?", 0),

                    ("¿Sueles ayudar a otros antes de pensar en ti mismo?", 1),
                    ("¿Es importante para ti sentirte apreciado por los demás?", 1),
                    ("¿Te cuesta decir que no cuando alguien te pide ayuda?", 1),
                    ("¿Te consideras una persona empática y comprensiva?", 1),
                    ("¿Sientes que los demás a veces no valoran lo suficiente tu ayuda?", 1),

                    ("¿Sientes la necesidad de destacarte en lo que haces?", 2),
                    ("¿Te preocupas mucho por la imagen que proyectas?", 2),
                    ("¿Te gusta recibir reconocimiento por tus logros?", 2),
                    ("¿Tienes una gran motivación por alcanzar tus metas?", 2),
                    ("¿Te resulta difícil aceptar tus fracasos?", 2),

                    ("¿Te consideras una persona reflexiva y analítica?", 3),
                    ("¿Prefieres mantener cierta distancia emocional en las relaciones?", 3),
                    ("¿Disfrutas de la soledad y el tiempo para pensar?", 3),
                    ("¿Tienes curiosidad por entender el mundo que te rodea?", 3),
                    ("¿Te resulta difícil compartir tus sentimientos con otros?", 3),

                    ("¿Sueles preocuparte por las opiniones de los demás?", 4),
                    ("¿Te cuesta tomar decisiones por miedo a equivocarte?", 4),
                    ("¿Te consideras una persona insegura en algunas situaciones?", 4),
                    ("¿Sientes la necesidad de asegurarte de que todo esté bien?", 4),
                    ("¿Te cuesta confiar en que todo saldrá bien sin tu intervención?", 4),

                    ("¿Te consideras una persona espontánea y alegre?", 5),
                    ("¿Te resulta fácil ver el lado positivo de las cosas?", 5),
                    ("¿Disfrutas de vivir nuevas experiencias constantemente?", 5),
                    ("¿Te cuesta estar en una rutina durante mucho tiempo?", 5),
                    ("¿Tienes miedo de perderte oportunidades interesantes?", 5),

                    ("¿Te consideras una persona decidida y con carácter?", 6),
                    ("¿Te gusta sentir que tienes el control de la situación?", 6),
                    ("¿Te resulta difícil aceptar la autoridad de otros?", 6),
                    ("¿Prefieres liderar antes que seguir?", 6),
                    ("¿Tienes miedo de que otros te perciban como débil?", 6),

                    ("¿Sientes la necesidad de proteger a los demás?", 7),
                    ("¿Te resulta importante sentirte necesario en las vidas de los demás?", 7),
                    ("¿Te preocupas por la seguridad y el bienestar de tus seres queridos?", 7),
                    ("¿Te consideras leal a tus amigos y familiares?", 7),
                    ("¿Te cuesta confiar en otras personas al principio?", 7),

                    ("¿Te consideras una persona tranquila y en paz?", 8),
                    ("¿Prefieres evitar los conflictos siempre que sea posible?", 8),
                    ("¿Te resulta difícil tomar partido en una discusión?", 8),
                    ("¿Te gusta mantener un ambiente armonioso en tus relaciones?", 8),
                    ("¿Te cuesta decir lo que realmente piensas para evitar discusiones?", 8)
                ]
        # Crear fuente personalizada
        self.custom_font = font.Font(size=14)  # Cambiar el tamaño a 14 o el que prefieras

        # Crear widgets
        self.question_label = tk.Label(self.root, text=self.preguntas[self.current_question][0], wraplength=400, font=self.custom_font, bg='white')  # Fondo blanco para la pregunta
        self.question_label.pack(pady=20)

        self.si_button = tk.Button(self.root, text="Sí", command=lambda: self.responder(1))
        self.si_button.pack(side="left", padx=20, pady=10)

        self.no_button = tk.Button(self.root, text="No", command=lambda: self.responder(0))
        self.no_button.pack(side="right", padx=20, pady=10)

    def responder(self, respuesta):
        eneatipo = self.preguntas[self.current_question][1]
        if respuesta == 1:  # Si elige 'Sí'
            self.score[eneatipo] += 1

        self.current_question += 1

        if self.current_question < len(self.preguntas):
            self.question_label.config(text=self.preguntas[self.current_question][0])
        else:
            self.mostrar_resultado()

    def mostrar_resultado(self):
        eneatipo_mayor = self.score.index(max(self.score)) + 1

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

        resultado = descripciones[eneatipo_mayor]
        messagebox.showinfo("Resultado", f"Tu eneatipo es el {eneatipo_mayor}\n{resultado}")
        self.root.quit()
        
    #def simular_respuestas(self):
        # Simula respuestas automáticas
        #if self.current_question < len(self.preguntas):
            # Alternar entre responder "Sí" y "No" para las pruebas
            #respuesta = 1 if self.current_question % 2 == 0 else 0
            #self.responder(respuesta)
            # Repite la simulación cada 500ms para cada pregunta
            #self.root.after(500, self.simular_respuestas)


if __name__ == "__main__":
    root = tk.Tk()
    app = CuestionarioEneagrama(root)
    root.mainloop()
