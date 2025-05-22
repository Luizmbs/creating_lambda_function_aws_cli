import json
from lambda_function import lambda_handler

def main():
    with open("teste_event.json") as f:
        event = json.load(f)
    context = None
    resultado = lambda_handler(event, context)
    print("Resultado do teste:", resultado)

if __name__ == "__main__":
    main()