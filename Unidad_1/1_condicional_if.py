promedio = float(input("ingresa tu promedio: "))

if promedio < 0 or promedio > 10:
    print("este promedio no existe")
elif promedio <= 5:
    print("tu promedio es muy bajo")
elif promedio <= 7:
    print("tu promedio es bajo")
elif promedio <= 9:
    print("tu promedio es bueno")
else:
    print("tu promedio es excelente")


