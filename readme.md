# Asistente de Voz "Mago" con OpenAI y Clima en La Plata

Este proyecto implementa un asistente de voz llamado "Mago" utilizando la API de OpenAI para generar respuestas y el servicio OpenWeatherMap para obtener el clima en La Plata, Argentina. "Mago" puede responder preguntas sobre la hora, el clima y cualquier otra consulta que el usuario pueda tener.

## Requisitos

- Python 3.x
- Paquetes de Python:
  - `openai`
  - `speech_recognition`
  - `pyttsx3`
  - `requests`
- Claves API:
  - Clave API de OpenAI
  - Clave API de OpenWeatherMap

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias utilizando pip:
```sh
   pip install openai speechrecognition pyttsx3 requests
```
3. Configura tus claves API:
   - Reemplaza `'TU_API'` en el código con tu clave API de OpenAI y tu clave API de OpenWeatherMap.

## Cómo Funciona

El asistente de voz "Mago" escucha comandos activados por la palabra clave "Mago". Puede realizar las siguientes funciones:

1. **Obtener la hora actual en Gonnet, La Plata:**
   - Al decir "Mago, ¿qué hora es?", el asistente devolverá la hora actual sin segundos.

2. **Obtener el clima en La Plata, Argentina:**
   - Al decir "Mago, ¿cómo está el clima?", el asistente devolverá la temperatura y una descripción del clima actual en La Plata.

3. **Responder preguntas generales:**
   - "Mago" utiliza la API de OpenAI para responder preguntas generales que el usuario pueda tener, proporcionando respuestas breves y concisas.

## Estructura del Código

- **`obtener_hora()`**: Devuelve la hora actual en Gonnet, La Plata, sin segundos.
- **`obtener_clima()`**: Consulta el clima actual en La Plata utilizando la API de OpenWeatherMap y devuelve una descripción con la temperatura.
- **`recognize_speech(prompt="")`**: Captura el audio del micrófono y lo convierte en texto utilizando la API de reconocimiento de voz de Google.
- **`ask_gpt(question)`**: Envía una pregunta a la API de OpenAI y devuelve una respuesta.
- **`speak_text(text)`**: Convierte el texto en habla utilizando `pyttsx3`.
- **`stop_speaking()`**: Detiene cualquier habla en curso.
- **`listen_for_commands()`**: Bucle principal que escucha continuamente comandos de voz y responde en consecuencia.

## Uso

1. Ejecuta el script en tu entorno de Python:
```sh
   python nombre_del_script.py
```
2. El asistente escuchará el comando "Mago" para activarse. Luego, puedes hacer preguntas como:
   - "Mago, ¿qué hora es?"
   - "Mago, ¿cómo está el clima?"
   - "Mago, [cualquier otra pregunta]"

3. El asistente responderá mediante texto y voz.

## Ejemplo de Salida
```
Escuchando 'Mago' para activar...
Reconocido: Mago, ¿cómo está el clima?
Mago dice: La temperatura en La Plata es de 22°C con cielo despejado
```

## Notas

- Asegúrate de tener una conexión a Internet activa para que las APIs de OpenAI y OpenWeatherMap funcionen correctamente.
- El reconocimiento de voz requiere un micrófono funcional y un entorno con poco ruido de fondo para obtener mejores resultados.

## Licencia

Este proyecto es de código abierto y está disponible bajo la [Licencia MIT](LICENSE).
