# Declarando una lista
try:
    materias = ["programacion", "matematicas", "filosofia", "ingles"]
    print(materias[0])
    materias.append("lengua y comunicacion")
    print(materias)
    materias[1]="biologia"
    print(materias)
    materias.remove("matematicas")
except IndexError:
        print("indice correcto") 