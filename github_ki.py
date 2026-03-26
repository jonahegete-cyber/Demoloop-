"""
Einfache KI-Abfrage in einer Datei.
- Funktioniert direkt
- Keine Ordnerstruktur nötig
- Antwort kommt mit kleiner Pause für „normales Schreiben“
"""

import openai
import time

# ========================
# 1️⃣ API-Key
# ========================
# Setze hier deinen OpenAI API Key ein:
openai.api_key = "DEIN_OPENAI_API_KEY_HIER"

# ========================
# 2️⃣ Funktion, die GPT-4 fragt
# ========================
def frage_ki(prompt):
    """
    prompt: Text, den du der KI gibst
    return: Antwort der KI
    """
    time.sleep(1)  # kleine Pause für normale Geschwindigkeit
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']

# ========================
# 3️⃣ Hauptprogramm
# ========================
if __name__ == "__main__":
    print("=== KI Abfrage ===")
    while True:
        user_input = input("Du: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Programm beendet.")
            break
        antwort = frage_ki(user_input)
        print("KI:", antwort)