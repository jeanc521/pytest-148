import requests 

def buscar_cep(cep):
    res = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    if res.status_code != 200: 
        return 'CEP invalido'
    else: 
        cep_encontrado = res.json()
        return cep_encontrado

cep = input("Informe o cep: ")
resultado =  buscar_cep(cep)


print(f'Rua: {resultado['logradouro']}')
print(f'Complemento: {resultado['complemento']}')
print(f'Bairro: {resultado['bairro']}')
print(f'Localidade: {resultado['localidade']}')
print(f'Cidade: {resultado['uf']}')
print(f'Estado: {resultado['estado']}')
print(f'Região: {resultado['regiao']}')
print(f'DDD: {resultado['ddd']}')