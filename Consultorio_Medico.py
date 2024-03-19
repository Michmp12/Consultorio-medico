import os

odontologia = 0
ginecologia = 0
consulta_general = 0
maternidad = 0
infantes = 0
repetir = True

def fnt_limpiarpantalla():
    os.system('cls')

def fnt_opcion(op):
    global odontologia, ginecologia, consulta_general, maternidad, infantes
    if (op == 1):
        odontologia += 1
    if (op == 2):
        ginecologia += 1
    if (op == 3):
        consulta_general += 1
    if (op == 4):
        maternidad += 1
    if (op == 5):
        infantes += 1
    
    
def fnt_tabla():
    fnt_limpiarpantalla()
    global odontologia, ginecologia, consulta_general, maternidad, infantes
    print('Odontologia', odontologia)
    print('Ginecologia', ginecologia)
    print('Consulta general', consulta_general)
    print('Maternidad',maternidad)
    print('Infantes',infantes)

while repetir == True:
    fnt_limpiarpantalla()
    opcion = int(input('---- MENU DE OPCIONES ----\n1. Odontologia\n2. Ginecologia\n3. Consulta general \n4. Maternidad\n5. Infantes\n6. Salir\n7. Reporte\n\n-> '))
    fnt_opcion(opcion)
    if (opcion == 6):
        repetir = False
    else:
        if (opcion == 7):
            fnt_tabla()
            enter = input('\n<ENTER>')