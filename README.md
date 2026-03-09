# ai-book-writer

Ett Pythonprojekt för att använda OpenAI GPT-modeller till att iterativt och automatiserat skriva böcker med hög kvalitet.

## Struktur
- `data/`: Outline, regler, research och inputmaterial.
- `src/`: Pythonkod för att generera och bearbeta bokkapitel.
- `book/`: Genererade kapitel och nybokutkast.

## Installation

1. Skapa ett virtuellt Python-env:
   ```
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Installera paket:
   ```
   pip install -r requirements.txt
   ```

3. Sätt din OpenAI API-nyckel i `.env`:
   ```
   OPENAI_API_KEY=din_nyckel_här
   ```

## Användning

Exempel:
```
python src/generate_chapter.py
```

Läs mer i koden och anpassa prompts/regler efter behov!
