import requests

base_url = "https://viacep.com.br/ws/"

def get_endereco(cep: str) -> dict:
    response = requests.get(f"{base_url}{cep}/json/", timeout=60)

    if response.status_code == 200:
        return response.json()
    return {}

def exibir_endereco(endereco: dict) -> None:
    if endereco:
        print(f"CEP: {endereco.get('cep', 'Não informado')}")
        print(f"Logradouro: {endereco.get('logradouro', 'Não informado')}")
        print(f"Complemento: {endereco.get('complemento', 'Não informado')}")
        print(f"Bairro: {endereco.get('bairro', 'Não informado')}")
        print(f"Localidade: {endereco.get('localidade', 'Não informado')}")
        print(f"UF: {endereco.get('uf', 'Não informado')}")
        print(f"Estado: {endereco.get('estado', 'Não informado')}")
        print(f"Região: {endereco.get('regiao', 'Não informado')}")
    else:
        print("Endereço não encontrado.")

if __name__ == "__main__":
    cep_usuario = input("Digite o seu CEP: ")  # Solicita o CEP do usuário
    endereco = get_endereco(cep_usuario)
    exibir_endereco(endereco)
