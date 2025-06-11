import requests
from unittest.mock import MagicMock
import pytest

@pytest.fixture
def buscar_resposta_com_mock():
    mock = MagicMock(spec=requests.Response)
    mock.status_code = 200 
    mock.json.return_value = {"menssagem":"Acesso com sucesso"}
    return mock

def test_conferencia_resposta_com_mock(buscar_resposta_com_mock):
    res = buscar_resposta_com_mock 
    assert res.status_code == 200
    assert res.json() == {"menssagem":"Acesso com sucesso"}