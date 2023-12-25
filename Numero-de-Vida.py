def digito_vida():
    fecha = input("Te voy a pedir tu fecha de nacimiento en el formato DD/MM/AAAA:")
    fecha_numeros = []
    for caracter in fecha:
        if caracter.isalnum():
            fecha_numeros.append(int(caracter))
    return fecha_numeros

def sumatoria_dv(lista_dv):
    while True:
        suma = sum(lista_dv)
        if suma <= 9:
            return suma
        else:
            lista_dv = [int(digito) for digito in str(suma)]

lista_dv = digito_vida()

resultado_final = sumatoria_dv(lista_dv)

print("El dígito de la vida es:", resultado_final)
