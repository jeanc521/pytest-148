def verifica_email(email):
    if '@' in email and '.com' in email:
        return 'email valido'
    else: 
        return 'email incorreto'
    
def test_verificar_se_email_funciona():
    assert verifica_email("j@c.com") == 'email valido'
    assert verifica_email("jeanromoaldogmail")  == 'email incorreto'
    assert verifica_email("jeanromoaldogmail.com")  == 'email incorreto'
    assert verifica_email("jeanromoaldo@gmail")  == 'email incorreto'