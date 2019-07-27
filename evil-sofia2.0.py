#Evil SoFiA 
import re
import time 
from random import choice
import sys
vrs = ' 1.9.1'
time.sleep(0.5)
import os

hostname = "www.google.com"
response = os.system("ping -f " + hostname)
if response == 0:
    print "Hay conexion suficiente uwu"
else:
    print "No hay conexion suficiente unu"
    exit()
ax = os.system 
ax("cls")
ax("color 4 ")
ols = time.strftime("%H:%M:%S")
print time.strftime("                     %I:%M:%S") 
if ols > "23:30":
    print "EVIL SOFIA SE ESTA ACTUALIZANDO!..."
    exit()
else:
    print " "

print '''
    ___ _   _  _ _      __   __  ___ _  __   
   | __| \ / || | |   /' _/ /__\| __| |/  \  
   | _|`\ V /'| | |_  `._`.| \/ | _|| | /\ | 
   |___| \_/  |_|___| |___/ \__/|_| |_|_||_|  
'''
time.sleep(1.4)
ax("title EVIL SOFIA")
print "         Emmanuel Milos" + "|" + "Emilio Barroso"
print "         ~EXTRAPOLADOR Y GENERADOR SOFIA~" 
print '''
  
'''

while True:
    print("      .:MENU:.")
    print("   1.EXTRAPOLADOR")
    print("   2.GENERADOR DE DNI")
    print("   3.SALIR")
    print("")
    opc = input("  Digite el numero de la opcion: ")
    print("")


    if opc == 1:
        time.sleep(1.5)
        print("\tACCES GRANTED!")
        time.sleep(1.5)
        print("")
        Bin = (input("  Digite los primeros 8 digitos del Bin: "))
        lista = []
        Intro = lista.append(Bin)

        #Primer Bin
        bin11 = int(input("  Introduce el digito numero DIEZ del primer Bin: "))
        if bin11 >= 0 and bin11 <= 9:
            print("")
        else:
            print("Introduce un numero correcto :)")
            bin11 = int(input("Vuelve a introducir el digito: "))

        bin12 = int(input("  Introduce el digito numero ONCE del primer Bin: "))
        if bin12 >= 0 and bin12 <= 9:
            print("")
        else:
            print("Introduce un numero correcto :)")
            bin12 = int(input("Introduce el digito numero ONCE del primer Bin: "))

        #Segundo Bin

        bin21 = int(input("  Introduce el digito numero DIEZ del segundo Bin: "))
        if bin21 >= 0 and bin21 <=9:
            print("")
        else:
            print("Introduce un numero correcto :)")
            bin21 = int(input("Vuelve a introducir el digito: "))

        bin22 = str((input("  Introduce el digito numero ONCE del segundo Bin: ")))
        if bin22 >= 0 and bin22 <=9:
            print("")
        else:
            print("Introduce un numero correcto :)")
            bin22 = int(input("Introduce el digiro numero ONCE del segundo Bin: "))

        #Algoritmo

        A = int(bin11 + bin21 / 2) * 5
        B = int(bin12 + bin22 / 2) * 5
        C = A + B

        #Agregar los digitos

        Intro2 = lista.append(C)
        print("Tu extrapolacion es: ")
        time.sleep(0.8)
        print("".join(repr(e) for e in lista))
        print("")
        time.sleep(2)

    elif opc==2:
        #LAST DNI GEN
        import time
        
        from random import randint
        os.system("title LAST")
        os.system("cls")
        os.system("color 4")
        print time.strftime("               %I:%M:%S")
        print'''
    
$$\        $$$$$$\   $$$$$$\ $$$$$$$$\ 
$$ |      $$  __$$\ $$  __$$\\__$$  __|
$$ |      $$ /  $$ |$$ /  \__|  $$ |   
$$ |      $$$$$$$$ |\$$$$$$\    $$ |   
$$ |      $$  __$$ | \____$$\   $$ |   
$$ |      $$ |  $$ |$$\   $$ |  $$ |   
$$$$$$$$\ $$ |  $$ |\$$$$$$  |  $$ |   
\________|\__|  \__| \______/   \__|   
                                       
                                                                 
            '''
        dni=range(1,9)
        print("   Emmanuel Milos|Emilio Barroso")

        i=0

        while i<len(dni):
            for elento in dni:
               dni[i]=randint(1,9)
            i+=1


    
        dni2=x=''.join(map(str,dni))

        print ' '
        time.sleep(2)
        print ("          Generando DNI...")
        time.sleep(3)
        print '''

        '''
        def ra():
            numero = dni2

            intnumero = int(numero)

            letra1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

            resto = intnumero%23

            letra = letra1[resto]
            print '   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
            print '   %        ' + numero,  "-", letra + '       %'
            print'   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
            print " "

        ra()

        raw_input("Presiona Enter Para Salir De El Gen")
        os.system("color 0")
        print("")
    elif opc==3:
        print ("Gracias por Utlizar SoFiA")
        break;
        exit()
    elif opc==4:
        print "En Contruccion!"
        break;
        exit()