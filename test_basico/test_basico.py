def eh_par(numero):

    if numero % 3 == 0:
        return 'e par'
    else:
        return 'e impar'

def somar(a, b):
    return a + b

def sub(a, b):
     return a - b
      
def div(a,b):
    return a / b
      
def test_verifica_se_numero_par():
    assert eh_par(2) == 'e impar'
    assert eh_par(3) ==  'e par'
    
def test_varificar_soma_e_subtrair():
    assert somar(5,6) == 11
    assert sub(10,8) == 2