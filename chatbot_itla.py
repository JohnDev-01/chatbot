
import re

qa_data = [
    {
        "questions": [
            "¿Qué es el ITLA?",
            "¿Qué significa ITLA?",
            "¿Qué institución es el ITLA?",
            "Explícame qué es el ITLA"
        ],
        "answer": "El ITLA es el Instituto Tecnológico de Las Américas, una institución especializada en tecnología y educación superior en la República Dominicana."
    },
    {
        "questions": [
            "¿Cuáles son las carreras que ofrece el ITLA?",
            "¿Qué carreras hay en el ITLA?",
            "Dime las carreras disponibles en el ITLA",
            "¿Qué programas académicos tiene el ITLA?"
        ],
        "answer": "El ITLA ofrece carreras en software, redes, multimedia, diseño, mecatrónica, manufactura automatizada y más áreas tecnológicas."
    },
    {
        "questions": [
            "¿Dónde está ubicado el ITLA?",
            "¿Cuál es la ubicación del ITLA?",
            "¿Dónde queda el ITLA?",
            "¿Dónde se encuentra el ITLA?"
        ],
        "answer": "El ITLA está ubicado en la avenida Las Américas, Santo Domingo Este, República Dominicana."
    },
    {
        "questions": [
            "¿El ITLA es público o privado?",
            "¿El ITLA pertenece al gobierno?",
            "¿Es el ITLA una institución estatal?",
            "¿El ITLA es una universidad pública?"
        ],
        "answer": "El ITLA es una institución pública descentralizada, enfocada en la educación tecnológica."
    },
    {
        "questions": [
            "¿Cómo puedo inscribirme en el ITLA?",
            "¿Qué debo hacer para estudiar en el ITLA?",
            "¿Cómo me inscribo en el ITLA?",
            "Dime el proceso de inscripción del ITLA"
        ],
        "answer": "Puedes inscribirte en el ITLA a través de su página web oficial, llenando el formulario de admisión y siguiendo las instrucciones para completar el proceso."
    },
    {
        "questions": [
            "¿Qué modalidades de estudio tiene el ITLA?",
            "¿Se puede estudiar online en el ITLA?",
            "¿Hay clases virtuales en el ITLA?",
            "¿El ITLA ofrece clases presenciales y online?"
        ],
        "answer": "El ITLA ofrece modalidades de estudio presenciales, virtuales y combinadas para adaptarse a las necesidades de los estudiantes."
    },
    {
        "questions": [
            "¿Qué es un tecnólogo en el ITLA?",
            "¿Qué significa ser tecnólogo en el ITLA?",
            "Explícame el concepto de tecnólogo en el ITLA",
            "¿Qué implica estudiar como tecnólogo en el ITLA?"
        ],
        "answer": "Un tecnólogo en el ITLA es un profesional capacitado en áreas tecnológicas específicas, con un enfoque práctico y aplicado en su formación."
    },
    {
        "questions": [
            "¿Cuál es la misión del ITLA?",
            "¿Qué busca el ITLA como institución?",
            "¿Cuál es el objetivo principal del ITLA?",
            "¿Qué persigue el ITLA?"
        ],
        "answer": "La misión del ITLA es desarrollar talento humano calificado en tecnología para contribuir al desarrollo sostenible y la competitividad del país."
    },
    {
        "questions": [
            "¿Qué beneficios tiene estudiar en el ITLA?",
            "¿Por qué debería estudiar en el ITLA?",
            "¿Qué ventajas ofrece el ITLA?",
            "¿Es bueno estudiar en el ITLA?"
        ],
        "answer": "Estudiar en el ITLA te permite acceder a educación tecnológica de calidad, equipos modernos, convenios internacionales y una alta tasa de empleabilidad."
    },
    {
        "questions": [
            "¿El ITLA tiene becas disponibles?",
            "¿Puedo estudiar en el ITLA con beca?",
            "¿Qué becas ofrece el ITLA?",
            "¿Cómo consigo una beca en el ITLA?"
        ],
        "answer": "Sí, el ITLA ofrece becas a estudiantes meritorios y aquellos que cumplen con los requisitos establecidos por la institución o programas gubernamentales."
    }
]

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def check_all_messages(message):
    for qa in qa_data:
        for question in qa["questions"]:
            if set(message) & set(question.lower().split()):
                return qa["answer"]
    return "Lo siento, no tengo información sobre eso. Pregúntame algo relacionado con el ITLA."

def chatbot():
    print("Chatbot ITLA: ¡Hola! Pregúntame cualquier cosa sobre el ITLA.")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() in ["salir", "adiós", "exit"]:
            print("Chatbot ITLA: ¡Hasta luego!")
            break
        print("Chatbot ITLA:", get_response(user_input))

if __name__ == "__main__":
    chatbot()
