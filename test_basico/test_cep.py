import pytest
import requests


@pytest.fixture
def consulta_cep():
    res = requests.get("https://viacep.com.br/ws/0101101000/json/")
    if res.status_code != 200:
        return "CEP não encontrado!"
    else:
        res.status_code = 200
        res.json()
        return res
   
  
    
def test_cep_nao_encontrado(consulta_cep):
    res = consulta_cep
    
    assert not res == "CEP não encontrado!"
    
def test_verifica_se_tem_cep_de_logradouro(consulta_cep):
    
    res = consulta_cep
    assert res == "logradouro"
    
def test_verifica_se_tem_cep_de_bairro(consulta_cep):
    res = consulta_cep
    assert res == "bairro"
    
def test_verificar_para_encontrar_uma_rua():
    rua = res.json()
    assert rua['logradouro'] == "Travessa Hamburgo"