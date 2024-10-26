Cuestionario de Eneagrama
Este proyecto implementa un Cuestionario de Eneagrama en Python utilizando Tkinter para la interfaz gráfica. Permite a los usuarios responder preguntas que identifican su eneatipo, o tipo de personalidad, basado en el sistema de Eneagrama.

Estructura del Proyecto
1. logica_eneagrama.py
Este archivo define la clase LogicaEneagrama, la cual gestiona la lógica principal del cuestionario.

Funciones principales:
__init__(): Inicializa las preguntas y los eneatipos con puntuaciones en 0.
responder(respuesta): Recibe la respuesta del usuario y actualiza la puntuación de cada eneatipo según la respuesta.
mostrar_resultado(): Calcula el eneatipo con mayor puntuación y lo retorna.
Preguntas:
El cuestionario contiene preguntas para los 9 eneatipos del Eneagrama. Cada pregunta está vinculada a un eneatipo específico.

2. test_logica_eneagrama.py
Archivo que contiene pruebas unitarias para asegurar que el código funcione correctamente. Se emplea la librería unittest.

Pruebas:
test_eneatipo_mayor(): Verifica que al responder a las preguntas de manera uniforme, se identifique el eneatipo correcto.
test_responder_incrementa_puntuacion(): Confirma que la puntuación del eneatipo se incremente con una respuesta positiva.
test_terminar_cuestionario(): Prueba que el cuestionario finalice correctamente al responder todas las preguntas.
3. cuestionario_eneagrama.py
Este archivo define la clase CuestionarioEneagrama y la interfaz gráfica de usuario.

Características principales:
Interfaz gráfica (Tkinter): Se muestra cada pregunta con opciones "Sí" y "No".
Visualización de resultados: Al finalizar, el programa muestra el eneatipo identificado y permite al usuario confirmar si se siente identificado.
Imagen de fondo: Personaliza la ventana con una imagen de fondo usando la librería Pillow.
Requisitos
Para ejecutar este proyecto necesitas instalar las siguientes librerías de Python:

bash
Copy code
pip install tkinter pillow
Uso
Ejecuta el archivo cuestionario_eneagrama.py para iniciar la aplicación gráfica:

bash
Copy code
python cuestionario_eneagrama.py
Responde cada pregunta para obtener el eneatipo sugerido basado en tus respuestas.

Al finalizar el cuestionario, se mostrará el eneatipo con una descripción detallada y palabras clave.

Ejecutar Pruebas
Para ejecutar las pruebas unitarias, usa el siguiente comando en la terminal:

bash
Copy code
python test_logica_eneagrama.py
Notas
Personalización de imágenes: La imagen de fondo puede cambiarse actualizando la ruta en cuestionario_eneagrama.py.
Preguntas del cuestionario: Las preguntas están definidas para cada eneatipo; puedes ajustarlas en logica_eneagrama.py si es necesario.
Contribuciones
Si quieres contribuir a este proyecto, realiza un fork y envía un pull request con tus mejoras o sugerencias.