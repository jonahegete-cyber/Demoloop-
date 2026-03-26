"""
Einfache GitHub KI-App in einer Datei.
- Fragt OpenAI GPT-4 ab
- Gibt Antwort zurück
- Läuft ohne mehrere Ordner
"""

import os
import time
import openai
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# OpenAI API-Key aus der Umgebung
# Auf iOS kannst du: os.environ["OPENAI_API_KEY"] = "DEIN_KEY" setzen
openai.api_key = os.getenv("OPENAI_API_KEY", "DEIN_OPENAI_API_KEY_HIER_EINFÜGEN")

app = FastAPI(title="Einfaches GitHub KI Backend")

# Datenmodell für die Anfrage
class Query(BaseModel):
    prompt: str

@app.post("/chat")
async def chat(query: Query):
    """Nimmt einen Text-Prompt entgegen, wartet 1 Sekunde und gibt GPT-Antwort zurück"""
    time.sleep(1)  # normale Schreibgeschwindigkeit
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": query.prompt}],
        temperature=0.7
    )
    return {"answer": response['choices'][0]['message']['content']}

if __name__ == "__main__":
    # Starte den Server auf Port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)