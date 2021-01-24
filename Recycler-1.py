#Universidad del Valle de Guatemala
#Algoritmos y Programación Básica
#Sección 50
#Joshua Padilla 19347
#Yoo Ji Kim 19561
#Martha Gómez 19501
#Gabriel Quiroz 19255
#José Ponce 19092
#Prototipo programado
#Re-cycler v0.0
import moduloprototiporecycler as mp
import numpy as np 
import matplotlib.pyplot as plt

with open('Datosx.txt', encoding='utf-8') as archivo:
    texto = archivo.read()
archivo.close()
lineas = texto.split('\n')
datosusuario = lineas[0].split (' ,')
#Contadores para grafica
coperacion = 0
cbolsas= 0
#Contadores para validacion
opcion = 0
contadorerror= 0
idioma = ""
#Lista para almacenar nombre
nombre = [datosusuario [4]]
#Lista para almacenar direccion
direccion = [datosusuario[3]]
#Lista para almacenar correo
correo = [datosusuario[0]]
#Lista para almacenar contraseña
contraseña = [datosusuario [1]]
#Lista para almacenar telefono
telefono = [datosusuario[2]]
#Lista para almacenar fechas disponibles
voluntario=["21 de Abril", "24 de Abril", "26 de Abril", "29 de Abril" ]
#Lista para almacenar horas disponibles
horasvoluntario=["8:00", "11:00", "14:00", "15:00"]
#Lista para almacenar materiales disponibles
materiales=["Metal","Plástico","Papel/Cartón","Vidrio"]
#Lista para almacenar la informacion de voluntario que es la 2
x=[]
#Lista para guardar informacion de opcion 1 de Reciclar
y=[]
#lista para almacenar toda la informacion de cuando sera la proxima colecta que es la opcion 4
z=[]
u = ''
c = ''
lineas[1] = lineas[1].split(',')
lineas[2] = lineas[2].split(',')
lineas[3] = lineas[3].split(',')

for rec in lineas[1]:
    recin = rec.split('  ')
    y.append(recin)
    
for vol in lineas[2]:
    volin = vol.split('  ')
    x.append(volin)
    
for vot in lineas[3]:
    votin = vot.split('  ')
    z.append(votin)
    
#Mundo que esta definido como funcion en el modulo
mp.mundo()
#Validacion para que ingrese el numero que esta disponible
while idioma != "1":
    print('\nEscoje tu idioma')
    print('1. Español')
    idioma = input()
#Validacion para que ingrese correo y contraseña correcta       
if idioma == '1':
        while u != correo[0] or c!= contraseña[0] and contadorerror != 5:
            contadorerror+=1
            print("\n\n                       INICIA SESIÓN con GOOGLE")
            print("=========================================================================")
            print("\n                          Usuario o correo")
            u = '\ufeff' + input("                          ")
            print("\n                            Contraseña")
            c = input("                          ")     
            if u != correo or c!= contraseña:
                print("\n\t\tCorreo o contraseña incorrecta")
    
   
        
    #Ciclo para que continue el programa si elige una opcion incorrecta o la opcion 10 que es para finalizarlo
        while opcion != '10' and contadorerror !=5:
            coperacion += 1
            
            
            print("\n\n                  ¿CÓMO AYUDARÁS AL PLANETA?\n")
            print("==========================================================")
            print('Ahorita QUIERO\n')
            print("1. Reciclar")
            print("2. Ser voluntario")
            print("3. Monitorear el recolector")
            print("4. Decidir cuándo será la próxima colecta")
            print("5. Saber más")
            print("6. Ver mi perfil")
            print("7. Editar mi perfil")
            print("8. Historia de la empresa")
            print("9. Mostrar toda mi actividad")
            print('10. Salir')
            opcion = input("\n")
                

            if opcion == "1":
                #Lista para almacenar toda la info de reciclar
                reciclar = []
                 #Menu que se le muestra al usuario
                print("\n\n                            RECICLAR")
                print("------------------------------------------------------------------")
                print("\n¿Qué quieres reciclar?")
                print("1.",materiales[0] )
                print("2.",materiales[1] )
                print("3.",materiales[2] )
                print("4.",materiales[3])
                #Validacion si elige una opcion diferente a 1 2 3 o 4
                pepino = "0"
                
                while pepino != "1" and pepino != "2" and pepino != "3" and pepino != "4" :
                    #Input y dependiendo de que valor tome el input se almacenara un dato distinto de la lista de materiales en la lista de reciclar
                    pepino = (input("Ingrese una opcion:\n"))
                if pepino == "1":
                    reciclar.append (materiales[0])
                elif pepino == "2":
                    reciclar.append (materiales[1])                    
                elif pepino == "3":
                    reciclar.append (materiales[2])
                elif pepino == "4":
                    reciclar.append (materiales[3])
                        #Validacion para cantidad de bolsas de que solo puede ser un numero sino vuelve a pedirle al usuario que ingrese otra vez el numero
                print('\n¿Cuántas bolsas del material vas a reciclar?')
                validacionlopez = True
                #Input para que ingrese la cantidad de bolsas que reciclara
                lopez= input( "Ingrese la cantidad de bolsas que reciclara:\n")
                
                while validacionlopez != False:
                    try:
                        lopez = int(lopez)
                        cbolsas += lopez
                        validacionlopez = False
                    except:
                        print("Ingrese un dato valido")
                        lopez = input( "Ingrese la cantidad de bolsas que reciclara:\n")
                        #Que se agregue a la lista para almacenar informacion la cantidad de bolsas que reciclara
                reciclar.append(lopez)
                #Menu que se le muestra al usuario
                
                print("\nElije la fecha para la colecta en la que quieres participar.")
                print("1.", voluntario[0])
                print("2.", voluntario[1])
                print("3.", voluntario[2])
                print("4.", voluntario[3])
                amigo = "0"
                #Validacion por si ingresa un dato diferente de 1 2 3 4 o 5 en el input llamado amigo, si lo hace se le volvera a pedir que ingrese una opcion
                while amigo != "1" and amigo != "2" and amigo != "3" and amigo != "4":
                    amigo = (input("Ingrese una opcion:\n"))
                
                if amigo == "1":
                    reciclar.append(voluntario[0])
                    
                elif amigo == "2":
                    reciclar.append(voluntario[1])                    
                    
                elif amigo == "3":
                    reciclar.append(voluntario[2])                    
                elif amigo == "4":
                    reciclar.append(voluntario[3])                   
                #Menu que se le muestra al usuario                   
                print('\nEscoje la hora de recolecta que más te parezca')
                print('1.', horasvoluntario[0])
                print('2.', horasvoluntario[1])
                print('3.', horasvoluntario[2])
                print('4.', horasvoluntario[3])
                 #Validacion para que ingrese una opcion valida entre 1 a 4 de lo contrario se le volvera a pedir que ingrese una opcion
                horita = "0"
                
                while horita != "1" and horita != "2" and horita != "3" and horita != "4":
                    horita = (input("Ingrese una opcion:\n"))
                    
                if horita == "1":
                    reciclar.append(horasvoluntario[0])
                        
                elif horita == "2":
                    reciclar.append(horasvoluntario[1])                        
                        
                elif horita == "3":
                    reciclar.append(horasvoluntario[2])
                        
                elif horita == "4":
                    reciclar.append(horasvoluntario[3])
                #Agregar la lista que esta al inicio de la opcion a la lista que esta definida al inicio del programa    
                y.append(reciclar)
                #Mostrar mensaje de gracias que esta definido como funcion en los modulos 
                    
                print(mp.gracias())
                input()
                
            if opcion == "2":
                #Variable en la que se almacenara toda la informacion  que vaya elijiendo
                    informacionalmacenar=[]
                    
                    print("\nElije la fecha para la que quieres voluntariar")
                    print("1.", voluntario[0])
                    print("2.", voluntario[1])
                    print("3.", voluntario[2])
                    print("4.", voluntario[3])
                    #Validacion de si ingresa un dato diferente de 1 2 3 o 4 se le volvera a pedir que ingrese de nuevo una opcion
                    voluntariod = "0"
                
                    while voluntariod != "1" and voluntariod != "2" and voluntariod != "3" and voluntariod != "4":
                        voluntariod= input ("Ingrese la fecha que desea participar:\n")
                         #Si la opcion esta entre 1 a 4 dependiendo de lo que eliga se agregara a la lista definida al inicio de la opcion 2 como informacionalmacenar
                    
                    if voluntariod == "1":
                        informacionalmacenar.append(voluntario[0])
                    
                    elif voluntariod == "2":
                        informacionalmacenar.append(voluntario[1])                    
                        
                    elif voluntariod == "3":
                        informacionalmacenar.append(voluntario[2])                    
                        
                    elif voluntariod == "4":
                        informacionalmacenar.append(voluntario[3])
                    else:
                        print ("No ingreso un dato valido")
                        
                    #Menu que se le muestra al usuario
                    print('\nEscoje la hora en la que quieras voluntariar')
                    print("1.", horasvoluntario[0])
                    print("2.", horasvoluntario[1])
                    print("3.", horasvoluntario[2])
                    print("4.", horasvoluntario[3])
                    voluntariohorad = "0"
                
                    while voluntariohorad != "1" and voluntariohorad != "2" and voluntariohorad != "3" and voluntariohorad != "4":
                        voluntariohorad = input ("Ingrese la hora a la que desea participar:\n")
                        #Dependiendo de lo que eliga se agregara agregara el indice de la variable horasdevoluntario que esta al inicio del programa a la lista que esta definida al inicio de la opcion
                    
                    if voluntariohorad == "1":
                        informacionalmacenar.append(horasvoluntario[0])
                        
                    elif voluntariohorad == "2":
                        informacionalmacenar.append(horasvoluntario[1])                        
                        
                    elif voluntariohorad == "3":
                        informacionalmacenar.append(horasvoluntario[2])                        
                        
                    elif voluntariohorad == "4":
                        informacionalmacenar.append(horasvoluntario[3])
                    #Toda la informacion que se almaceno en la lista definida al inicio de la opcion 2, que se agregue a la que esta al inicio del programa   
                    x.append(informacionalmacenar)
                        
                    #Mensaje de agradecimiento que esta definido como funcion en un modulo      
                    print(mp.gracias())
                    input("\nPresione enter para regresar al menú principal.\n")
                
            if opcion == "3":
                #Mensaje que se le mostrara si elige la opcion 3 del menu
                de = "hoy"
                he = "11:30 p.m."
                teh = "2"
                tem = "30"
                print("\n\n                     MONITOREO DE CAMIÓN")
                print("------------------------------------------------------------------")
                #Mapa que esta definido como funcion en el modulo
                mp.guate()
                print("\nEl camión llegará a la ubicación seleccionada",de,"a las",he+".")
                print("\nFaltan", teh, "horas y", tem, "minutos para su llegada.")
                #Enter para regresar al menu
                input("\nPresione enter para regresar al menú principal.\n")
                
            if opcion == "4":
                #Lista donde se almacenara todas las opciones que vaya eligiendo aqui
                voto = []
                #Menu que se le mostrara al usuario
                print("\n\n                     DECISIÓN PARA COLECTAS")
                print("------------------------------------------------------------------")
                print("\nElije un material, mes, día y hora aprox. para la colecta")
                #Validacion para que escriba el nombre de los materiales que se encuentran en la lista
                validacionvoto1 = ["Metal","Plastico","Papel","Carton","Vidrio"]
                #Que se muestre la validacion al usuario para que pueda ver como es que tiene que escribir cada material, de lo contrario se le pedira que ingrese de nuevo el material
                print(validacionvoto1)
                #Validacion para que al ingresar el material solo sean letras y no numeros o que lo deje en blanco
                voto1 = input("Material:\n ")
                while voto1 not in validacionvoto1:
                        print("Ingrese un dato valido")
                        voto1 = input("Material:\n ")
                         #VAppend para que se agregue a la lista definida a l inicio de la opcion
                voto.append(voto1)
                 #Validacion para que ingrese solo los meses que estan disponibles 
                validacionvoto2 = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
                #Mostrarle la validacion la usuario para que sepa como ingresar el mes
                print("Elija un mes", validacionvoto2)
                #Input para que ingrese el mes y la validacion
                voto2 = input("Mes:\n ")
                while voto2 not in validacionvoto2:
                    print("Ingrese un dato valido")
                    voto2 = input("Mes:\n ")
                    #Que se agregue el mes que escribio a la lista definida al inicio de la opcion 4
                voto.append(voto2)
                #Validacion para que ingrese un numero valido
                validacionvoto3 = True
                voto3 = input("Ingrese el numero de día:\n ")
                while validacionvoto3 != False:
                    try:
                        voto3 = int(voto3)
                        #Que se agregue el dia que eligio a la lista que esta definida al inicio de la opcion
                        validacionvoto3 = False
                    except:
                        print("Ingrese un dato valido")
                        voto3 = input("Ingrese el numero de día:\n ")
                voto.append(voto3)
                #Input para quue ingrese la hora
                voto4 = input('Hora aproximada:\n ')
                #Que se agregue el input anterior a la lista definida al inicio de la opcion
                voto.append(voto4)
                #La lista definida al inicio de la opcion que se agregue a la lista definida al inicio del programa
                z.append(voto)
                
                
                
                #Mensaje de gracias e input para regresar al menu
                print("\n¡Gracias por tu aporte!")
                input("\nPresione enter para regresar al menú de principal. ")               
                #Mensaje que se le mostrara al usuario si elige la opcion 5
            if opcion == "5":
                print("\n\n                         INFORMACIÓN")
                print("------------------------------------------------------------------")
                print("\n¿Cómo podemos ayudarte?")
                print("1. Chat 1:1")
                print("2. Preguntas frecuentes")
                print("3. Fichas informativas de empresas")
                print("4. Regresar al menú principal")
                e = "0"
                #Validacion para que eliga solo las opciones disponibles en la lista
                while e != "1" and e != "2" and e != "3" and e != "4":
                    e = (input("Ingrese una opcion:\n"))
                if e == "1":
                    #Mensaje que se le mostrara si elige la opcion 1
                    print("\n======CHAT 1:1======")
                    print("Hola, ¿cómo podemos ayudarte?")
                    input()
                    print("Tu mensaje a sido recibido, un operador de servicio al cliente te contactará en breve.")
                    input("\n Presione enter para regresar al menú principal.")
                if e == "2":
                    #Mensaje que se le mostrara si elige la opcion 2
                    print("\n======PREGUNTAS FRECUENTES======")
                    print("\nPregunta: ¿Hay otros idiomas disponibles?")
                    print("Respuesta: No por el momento, ya que en el país el idioma más popular es el español,",
                          "no consideramos necesario agregar otro idioma mientras que no nos expandamos a otro país.")
                    print("\nPregunta: ¿Porqué debería reciclar?")
                    print("Respuesta: Porque el la contaminación mata al planeta y reciclando puedes reducirla.")
                    print("\nPregunta: ¿Cómo puedo ayudar más?")
                    print("Respuesta: Trata de usar productos biodegradables.")
                    input("\n Presione enter para regresar al menú principal.")
                if e == "3":
                    #Mensaje que se le mostrara si elige la opcion 3
                    print("\n======EMPRESAS======")
                    print("\nNombre de empresa: Geotec")
                    print("Teléfono: 23233445")
                    print("Dirección: 1 av zona 10")
                    print("Materiales: Metal, vidrio")
                    print("Correo electrónico: mat.v@gmail.com")
                    print("\nNombre de empresa: Biofriends")
                    print("Teléfono: 21905699")
                    print("Dirección: 2-22 calle 24 zona 11")
                    print("Materiales: Plástico")
                    print("Correo electrónico: bio@gmail.com")
                    print("\nNombre de empresa: Recipro")
                    print("Teléfono: 43434546")
                    print("Dirección: 12 avenida zona 2")
                    print("Materiales: cartón, papel")
                    print("Correo electrónico: recic@gmail.com")
                    input("\n Presione enter para regresar al menú principal.")
                
            if opcion == "6":
#aqui es donde muestra su nombre, direccion, correo, telefono y contraseña si elige la opcion 6
                print("\n\n                           USUARIO")
                print("------------------------------------------------------------------")
                print("\nNombre:", nombre)
                print("\nDirección:", direccion)
                print("\nCorreo electrónico:", correo)
                print("\nContraseña:", contraseña)
                print("\nTeléfono:", telefono)
                input("\nPresione enter para regresar al menú principal.")
            
            if opcion =="7":
                #Menu que se le mostrara al usuario
                print ("¿ Que desea editar ?")
                print ("1. Nombre")
                print ("2. Direccion")
                print ("3. Correo")
                print ("4. Contraseña")
                print ("5. Telefono")
                print("")
                 #Validacion para que el input solo este entre el rango de 1 2 3 4 o 5 
                juan = "0"
                while juan != "1" and juan != "2" and juan != "3" and juan != "4" and juan != "5":
                    juan = (input("Ingrese una opcion:\n"))
                    #Que ingrese el nuevo nombre que desea tener si la opcion es esta y validacion para que no pueda dejar el nombre en blanco
                if juan =="1":
                    nuevonombre = input ("Ingrese el nombre que desea tener\n")
                     #Pop para eliminar de la lista el nombre que tenia anteriormente
                    while nuevonombre == "":
                        print("Ingrese un dato valido")
                        nuevonombre = input ("Ingrese el nombre que desea tener\n")   
                    nombre.pop(0)
                    #Append para agregar el nuevo nombre
                    nombre.append(nuevonombre)
                    #Mensaje de agradecimiento y enter para regresar al menu
                    print ("El nombre ha sido modificado exitosamente")
                    input ("Presione enter para regresar al menu\n")
                    #Si juan es igual a 2 que ingrese una nueva direccion y validacion para que no deje en blanco la direccion
                if juan =="2":
                    nuevadireccion = input ("Ingrese una direccion\n")
                    while nuevadireccion == "":
                        print("Ingrese un dato valido")
                        nuevadireccion = input ("Ingrese una direccion\n")
                        #Que se elimine la direccion que anteriormente poseia 
                    direccion.pop(0)
                    #Append para agregar la nueva direccion que acaba de elegir
                    direccion.append(nuevadireccion)
                    #Mensaje de agradecimiento
                    print ("La direccion a sido modificadada exitosamente")
                    #Enter para regresar al menu
                    input ("Presione enter para regresar al menu\n")
                    #Si juan es igual a 3 que ingrese su nuevo correo y validacion para que no lo deje en blanco
                if juan =="3":
                    nuevocorreo = input ("Ingrese su nueva direccion de correo electronico\n")
                    while nuevocorreo == "":
                        print("Ingrese un dato valido")
                        #Input por si lo deja en blanco
                        nuevocorreo = input ("Ingrese su nueva direccion de correo electronico\n")
                    correo.pop(0)
                    #Append para agregar el nuevo correo
                    correo.append(nuevocorreo)
                    #Mensaje de agradecimiento
                    print ("El correo ha sido modificado exitosamente")
                    #Enter para regresar al menu
                    input ("Presione enter para regresar al menu\n")
                #Si juan es igual a 4 que ingrese la contraseña actual y validacion para que no la pueda dejar en blanco
                if juan =="4":
                    contra =input ("Ingrese su contraseña actual:\n")
                    while contra == "":
                        print("Ingrese un dato valido")
                        contra = input ("Ingrese su contraseña actual:\n\n")
                        #Validacion de que si ingresa su contraseña correctamente podra ingresar la nueva contraseña y validacion para que no la pueda dejar en blanco
                    if contra == contraseña[0]:
                        nuevacontraseña = input ("Ingrese una nueva contraseña:\n")
                        while nuevacontraseña == "":
                            #Input para que ingrese de nuevo la nueva contraseña y si no es igual las dos veces no se guardara
                            print("Ingrese un dato valido")
                            nuevacontraseña = input ("Ingrese una nueva contraseña:\n\n")
                        nuevacontraseña2= input ("Ingrese nueva contraseña otra vez\n")
                        while nuevacontraseña2 == "":
                            print("Ingrese un dato valido")
                            nuevacontraseña2 = input ("Ingrese nueva contraseña otra vez:\n\n")
                            #Pop para elminar la antigua contraseña y agregar la nueva si en los dos ingresos son identicos
                        if nuevacontraseña == nuevacontraseña2:
                            contraseña.pop(0)
                            contraseña.append (nuevacontraseña)
                            #Mensaje de agradecimiento y mensaje de que las contraseñas no coinciden y enter para regresar al menu
                            print ("La contraseña a sido modificadada exitosamente")
                            input ("Presione enter para regresar al menu\n")                        
                        else:
                            print ("Las contraseñas no coinciden")
                            input ("Presione enter para regresar al menu\n")
                    
                    else:
                        print("La contraseña es incorrecta")
                        print("")
                        input ("Presione enter para regresar al menu\n")
                 #Si juan es igual a 5 que ingrese su nuevo numero de telefono y validacion para que no pueda dejar el espacio en blanco o que ingrese un dato valido
                if juan =="5":
                    nuevotelefono = input("Ingrese su nuevo telefono\n")
                    validaciontelefono = True
                    while validaciontelefono != False:
                        try:
                            nuevotelefono = int(nuevotelefono)
                            validaciontelefono = False
                        except:
                            print("Ingrese un dato valido")
                            nuevotelefono = input( "Ingrese su nuevo telefono\n")
                            #pop para eliminar el antiguo numero y append para agregar el nuevo numero de telefono
                    telefono.pop(0)
                    telefono.append(nuevotelefono)
                    #Print para mostrar mensaje de agradecimiento y enter para regresar al menu
                    print ("El telefono ha sido modificado exitosamente")
                    input ("Presione enter para regresar al menu\n")
               #Si elige la opcion 8 se le mostra la historia de los creadores al usuario     
            if opcion == "8":
                print("Somos alumnos de la Universidad del valle que trabajamos \nen un proyecto para asi poder resolver alguna problematica del pais,\nal analizar que es lo que afectaba mas al país determinamos que\nnadie reciclaba, por lo tanto decidimos realizar este programa\npara incentivar a los demas a reciclar")
                print("")
                print("Los responsables somos:")
                print("")
                print("Gabriel Quiroz\nJose Pablo Ponce \nJoshua Padilla \nYoo Ji Kim \nMartha Gomez")
                print("")
                input("Presione enter para regresar al menu\n")
                
            #Si elige la opcion 9 se le mostrara toda la informacion de lo que realizara a futuro el usuario
            if opcion =="9":
                #Datos para la realizacion de la grafica
                plt.plot([0,coperacion],[0,cbolsas], label = 'Bolsas recicladas', color = '#1C2833') 
                plt.legend(loc='upper left')
                plt.title('Cantidad de bolsas recicladas') 
                plt.xlabel('Cantidad de operaciones') #Configurar los ejes de la gráfica
                plt.ylabel('Cantidad de bolsas') 
                plt.grid() 
                plt.show() 
                opcion = 0 
                #Ingresar la fecha del voluntariado
                print("¿ Cuando seras voluntario?\n", x)
                #FECHA DE RECICLAJE
                print("Cuando reciclaras\n", y)
                #pROXIMA COLECTA FECHA
                print("Cuando sera la proxima colecta\n", z)
                print("")
                input("Presione enter para regresar al menu\n")
                
             
# iNFORMACION SOBRE ARCHIVO.TXT            
with open('Datosx.txt','w', encoding='utf-8') as archivo:
    #Datos
    
    archivo.write(u+" ,")
    archivo.write(c+" ,")
    archivo.write(telefono[0]+" ,")
    archivo.write(direccion[0]+" ,")
    archivo.write(nombre[0])
    archivo.write('\n')
    for elemento in y:
        archivo.write(',')
        for item in elemento:
            archivo.write(str(item)+"  ")
    archivo.write('\n')
    for elemento in x:
        archivo.write(',')
        for item in elemento:
            archivo.write(str(item)+"  ")
    archivo.write('\n')
    for elemento in z:
        archivo.write(',')
        for item in elemento:
            archivo.write(str(item)+"  ")   
    archivo.close()
#Lee el documento txt
with open('Datosx.txt', encoding='utf-8') as archivo:
    texto = archivo.read()
archivo.close()
lineas = texto.split('\n')





