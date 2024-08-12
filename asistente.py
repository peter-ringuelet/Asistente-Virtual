import openai
import speech_recognition as sr
import pyttsx3
import requests
from datetime import datetime

# Configuración de OpenAI
openai.api_key = 'TU_API'

# Inicializar el motor de texto a voz
engine = pyttsx3.init()
engine.setProperty('rate', 100)  # Ajustar la velocidad del habla
engine.setProperty('volume', 1)  # Asegurar el máximo volumen

# Historial de la conversación
conversation_history = [
    {"role": "system", "content": "Eres un asistente formal y amigable que da respuestas breves, concisas y eficaces. Te llamas Mago. Puedes saber todo lo necesario sobre el usuario. El usuario está en Gonnet, La Plata."}
]

# Función para obtener la hora en Gonnet, La Plata sin segundos
def obtener_hora():
    now = datetime.now()
    return now.strftime("%H:%M")

# Función para obtener el clima en La Plata, AR usando OpenWeatherMap
def obtener_clima():
    api_key = "TU_API"  # Tu clave API gratuita del servicio de clima
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "La Plata, AR"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric&lang=es"
    
    try:
        response = requests.get(complete_url)
        response.raise_for_status()
        
        data = response.json()
        
        if data.get("cod") != 200:
            return f"No se pudo obtener el clima. Error: {data.get('message', 'Desconocido')}"
        
        main = data.get("main", {})
        weather = data.get("weather", [{}])[0]
        temperature = main.get("temp")
        description = weather.get("description")
        
        if temperature and description:
            return f"La temperatura en La Plata es de {temperature}°C con {description}"
        else:
            return "No se pudo obtener el clima"
    
    except requests.exceptions.HTTPError as http_err:
        return f"No se pudo obtener el clima. Error HTTP: {http_err}"
    except requests.exceptions.ConnectionError as conn_err:
        return f"No se pudo obtener el clima. Error de conexión: {conn_err}"
    except requests.exceptions.Timeout as timeout_err:
        return f"No se pudo obtener el clima. Tiempo de espera agotado: {timeout_err}"
    except requests.exceptions.RequestException as req_err:
        return f"No se pudo obtener el clima. Error: {req_err}"

def recognize_speech(prompt=""):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        if prompt:
            print(prompt)
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=15)
        except sr.WaitTimeoutError:
            print("Tiempo de espera agotado mientras se esperaba que comenzara la frase")
            return None

    try:
        text = recognizer.recognize_google(audio, language='es-ES')
        print(f"Reconocido: {text}")
        return text
    except sr.UnknownValueError:
        print("No pude entender el audio")
        return None
    except sr.RequestError:
        print("Error con la API de reconocimiento de voz")
        return None

def ask_gpt(question):
    global conversation_history
    conversation_history.append({"role": "user", "content": question})
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=conversation_history,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5
        )
        message = response.choices[0].message['content'].strip()
        conversation_history.append({"role": "assistant", "content": message})

        return message
    except openai.error.OpenAIError as e:
        print(f"Error de OpenAI: {e}")
        return "Lo siento, hubo un error con la API de OpenAI. Por favor, inténtalo de nuevo más tarde."

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def stop_speaking():
    engine.stop()

def listen_for_commands():
    while True:
        command = recognize_speech("Escuchando 'Mago' para activar...")
        if command and "mago" in command.lower():
            stop_speaking()
            question = command.lower().split("mago", 1)[-1].strip()
            if "hora" in question:
                response = obtener_hora()
            elif "clima" in question:
                response = obtener_clima()
            else:
                response = ask_gpt(question)
            print(f"Mago dice: {response}")
            speak_text(response)

if __name__ == "__main__":
    listen_for_commands()
