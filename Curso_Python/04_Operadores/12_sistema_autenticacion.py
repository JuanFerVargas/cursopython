# Sistema de Autenticaion
print("*** Sistema de Autenticaion ***")
usuario1="admin"
password1=123

usuario2=input("Cual es tu usuario? ")
password2=int(input("Cual es tu password? "))

is_correct=usuario1==usuario2 and password1==password2
print(f"Datos correctos? {is_correct}")

