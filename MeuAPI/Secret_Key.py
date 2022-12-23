import string
import secrets

alphabet = string.ascii_letters + string.digits
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(80)) # gera uma senha alfanumérica de 80 caracteres
    if (any(c.islower() for c in password) # verifica se pelo menos um dos caracteres é minúsculo
            and any(c.isupper() for c in password) # verifica se pelo menos um dos caracteres é maísculo
            and sum(c.isdigit() for c in password) >= 3): # verifica se existe no mínimo 3 dígitos
        break
print(password)



