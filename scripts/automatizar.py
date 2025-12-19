import openai
import os
from pathlib import Path


openai.api_key = os.getenv("OPENAI_API_KEY")


# Capítulos a generar automáticamente
CAPITULOS = [1, 2]


# Cargar Biblia
with open("Biblia/Prompt_Maestro_Global.md", "r", encoding="utf-8") as f:
BIBLIA = f.read()


Path("Capitulos").mkdir(exist_ok=True)


for n in CAPITULOS:
print(f"Generando capítulo {n}...")


# ARQUITECTO
esquema = openai.ChatCompletion.create(
model="gpt-5-mini",
messages=[
{"role": "system", "content": BIBLIA},
{"role": "user", "content": f"Arquitecto Narrativo: diseña el Capítulo {n}"}
]
)["choices"][0]["message"]["content"]


# ESCRITOR
capitulo = openai.ChatCompletion.create(
model="gpt-5-mini",
messages=[
{"role": "system", "content": BIBLIA},
{"role": "user", "content": f"Escribe el Capítulo {n} usando este esquema:\n{esquema}"}
]
)["choices"][0]["message"]["content"]


ruta = f"Capitulos/Cap_{n:02d}.md"
with open(ruta, "w", encoding="utf-8") as f:
f.write(capitulo)


print("Proceso terminado. Capítulos creados.")
