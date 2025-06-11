import pytest
import requests

@pytest.fixture
def lista_simples():
    return [1,2,3,4]

def test_somar_lista_simples(lista_simples):
    assert sum(lista_simples) == 10
    
    
def test_tamano_da_lista_simples(lista_simples):
    assert len(lista_simples) == 4
    
    
def test_max_da_lista_simples(lista_simples):
    assert max(lista_simples) == 4
   
    
def test_min_lista_simples(lista_simples):
    assert min(lista_simples) == 1
    
