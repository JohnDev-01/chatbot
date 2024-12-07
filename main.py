
import re
import random
from itla_questions import qa_data

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
