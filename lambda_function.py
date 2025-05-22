import requests

def lambda_handler(event, context):
    valor_reais = float(event.get("valor", 0))

    # Chamada à API Frankfurter (sem key)
    resp = requests.get(
        "https://api.frankfurter.dev/v1/latest",
        params={"base": "BRL", "symbols": "USD"},
        timeout=5
    )
    resp.raise_for_status()
    data = resp.json()

    # Extrai a taxa e calcula
    rate = data["rates"]["USD"]
    return {"valor_BRL": valor_reais * rate}
