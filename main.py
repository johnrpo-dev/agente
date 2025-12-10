import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

print('----------------------')
print('🤖 Agente Iniciado...')
print('Escribe "exit" para salir.')
print('----------------------')

client = genai.Client(api_key=api_key)

# 1. Definimos la herramienta (Función de Python normal)
def list_files_in_dir(directory: str = "."):
    """Lista los archivos que existen en un directorio dado."""
    print(f"\n[🛠️ Agente usando herramienta: list_files_in_dir en '{directory}']")
    try:
        files = os.listdir(directory)
        return files
    except Exception as e:
        return str(e)

# 2. Creamos el Chat con la configuración automática
# Esto maneja la memoria y la ejecución de herramientas
chat = client.chats.create(
    model="gemini-2.0-flash",
    config=types.GenerateContentConfig(
        system_instruction="Eres un asistente útil. Si te piden hacer algo que requiere una herramienta, úsala.",
        tools=[list_files_in_dir], # Pasamos la función directamente
        automatic_function_calling=types.AutomaticFunctionCallingConfig(
            disable=False # Permite que el agente ejecute la función y obtenga el resultado solo
        )
    )
)

while True:
    user_input = input("\nTu: ").strip()

    if user_input.lower() in ["exit", "quit", "bye", "adios"]:
        break

    if not user_input:
        continue

    try:
        # 3. Enviamos el mensaje
        # El objeto 'chat' ya guarda el historial internamente
        response = chat.send_message(user_input)
        
        # 4. Imprimimos la respuesta final
        if response.text:
            print(f"Asistente: {response.text}")
        else:
            print("Asistente: (Tarea completada sin respuesta de texto)")
            
    except Exception as e:
        print(f"Error: {e}")