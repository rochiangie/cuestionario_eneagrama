# Archivo: logica_eneagrama.py

class LogicaEneagrama:
    def __init__(self):
        self.current_question = 0
        self.score = [0] * 9  # Puntuación para los 9 eneatipos

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

    def responder(self, respuesta):
        eneatipo = self.preguntas[self.current_question][1]
        if respuesta == 1:  # Si elige 'Sí'
            self.score[eneatipo] += 1

        self.current_question += 1
        if self.current_question >= len(self.preguntas):
            return self.mostrar_resultado()

    def mostrar_resultado(self):
        eneatipo_mayor = self.score.index(max(self.score)) + 1
        return eneatipo_mayor
