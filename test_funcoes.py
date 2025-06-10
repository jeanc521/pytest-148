from funcoes import *

def test_validando_senha():
    assert validar_senha("Brunindupla4y$") == 'Senha cadrastada'
    assert validar_senha("Brunindupla4y@") == 'Senha cadrastada'
    assert validar_senha("Brunindupla4y#") == 'Senha cadrastada'
    assert validar_senha("Brunindupla4y%") == 'Senha cadrastada'
    assert validar_senha("Brunindupla4y*") == 'Senha cadrastada' 
    assert validar_senha("Brunindupla4y&") == 'Senha cadrastada'   
    assert validar_senha("Jp") == 'Senha nao contem elementos obrigatorios'
    assert validar_senha("jp@#&*%") == 'Senha nao contem elementos obrigatorios'
    assert validar_senha("jp@#&*") == 'Senha nao contem elementos obrigatorios'
    
def test_tamanho_da_string():
    assert tamanho_string("joazinho") == 8
    
    
def test_validando_calcular_media():
    assert calcular_media({}) == 0
    assert calcular_media({3}) == 3
    
    
def test_verificar_maior_idade():
    assert verificar_maior_idade(20) == True
    assert verificar_maior_idade(17) == False
    
    
def test_vefiricar_numero_positivo():
    assert eh_positivo(2) == 'positivo'
    assert eh_positivo(-2) == 'negativo'
    
def test_status_de_notas_de_alunos():
    assert status_aluno(2) == 'reprovado'
    assert status_aluno(6) == 'recuperação'
    assert status_aluno(8) == 'aprovado'
    

    