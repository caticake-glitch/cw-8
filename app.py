import os
import anthropic
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

api_key = os.environ.get("ANTHROPIC_API_KEY")

if api_key is None:
    print("BŁĄD")

client = anthropic.Anthropic(api_key=api_key)

#to co widzisz przy wejsciu
history = []

print("\n" + "="*50)
print("CHATBOT CLAUDE - wersja terminalna")
print("-"*50)
print("Wpisz 'quit' lub 'exit' aby zakończyć rozmowę.")
print("-"*50 + "\n")

while True:
     
     #sprawdzanie czy koniec
    if user_input.lower() in ["quit", "exit", "Quit", "Exit", "q"]:
        print("\n Do widzenia! Miłego dnia.\n")
        break
    
    user_input = input("Ty: ").strip()
    
    #omijanie pustek
    if not user_input:
        print("Wpisz coś...\n")
        continue
    
    # Dodaj pytanie użytkownika do historii
    history.append({"role": "user", "content": user_input})
    
    try:
        # Wyślij całą historię do Claude
        print("Claude myśli...", end="", flush=True)
        
        response = client.messages.create(
            model="xyz",
            max_tokens=200,
            messages=history
        )
        
        print("\r" + " " * 20 + "\r", end="")  #czysci komunikat
        
        assistant_response = response.content[0].text
        
        print(f"Claude: {assistant_response}\n")

        #dodawanie do histori odpowiedzi
        history.append({"role": "assistant", "content": assistant_response})
        
    except anthropic.APIError as e:
        print(f"\n Błąd API: {e}\n")
    except Exception as e:
        print(f"\n Wystąpił nieoczekiwany błąd: {e}\n")


if __name__ == '__main__':
    main()
