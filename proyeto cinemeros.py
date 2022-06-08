import sys
import os
import random
#funcion entradas
def desc_edades():
    print('   EDAD O DISCAPACIDAD                   DESCUENTOS POR EDAD O DISCAPACIDAD')
    print("""          
8. MENORES DE EDAD                                      10%
9. PERSONAS DISCAPACITADAS                              20%
10. TERCERA EDAD                                        15%""")
def entradas_cine():
    print('--------------------------------------')
    print('               ENTRADAS               ')
    print('--------------------------------------')
    print("_"*70)
    print('   DIA        PRECIOS             DESCUENTOS CON TARJETA CINEMEROS')
    print("""          
1. LUNES = $8100                      10%
2. MARTES = $7000                     NO APLICA
3. MIERCOLES = $9000                  5%
4. JUEVES = $5000                     7%
5. VIERNES = $6800                    4%
6. SABADO = $7400                     3%
7. DOMINGO = $5000                    NO APLICA""")

    while True:
        try:
            dia=int(input('ESCOJA UN NUMERO SEGUN EL DIA DE LA SEMANA PARA IR AL CINEMEROS: '))#dato de entrada
            num_entrada=int(input('CUANTAS ENTRADAS DESEA COMPRAR: '))#dato de entrada
            break
        except ValueError:
            print("Intentelo de nuevo, ingrese valores correctos.")
        
    if dia==1:
        tarjeta_cine=0
        while tarjeta_cine<1 or tarjeta_cine>2 and True:
            try:
                tarjeta_cine=int(input('¿CUENTA CON TARJETA CINEMEROS? 1: SI 2:NO '))#dato de entrada
                
            except ValueError:
                print("Intentalo de nuevo, ingresa un valor correcto.")
        
                          
        if tarjeta_cine==1:
            desc_entrada=(8100*10*num_entrada)/100
            desc_edad_num=0
            while True:
                try:
                    
                 
                    desc_x_edad=int(input('QUIERE APLICAR DESCUENTO POR EDAD O DISCAPACIDAD: 1= SI 2= NO : '))
                        
                        
                    if desc_x_edad==1:
                        desc_edades()
                        desc_edad_num=int(input('ESCOJA EL NUMERO SEGUN SU EDAD O DISCAPACIDA: '))
                        if desc_edad_num==8:
                            valor_entrada=(8100*num_entrada-desc_entrada)
                            valor_entrada_edad=(valor_entrada*10)/100
                            valor_final=valor_entrada-valor_entrada_edad
                            print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_final)
                            break
                        elif desc_edad_num==9:
                            valor_entrada=(8100*num_entrada-desc_entrada)
                            valor_entrada_edad=(valor_entrada*20)/100
                            valor_final=valor_entrada-valor_entrada_edad
                            print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_final)
                            break
                        elif desc_edad_num==10:
                            valor_entrada=(8100*num_entrada-desc_entrada)
                            valor_entrada_edad=(valor_entrada*15)/100
                            valor_final=valor_entrada-valor_entrada_edad
                            break
                        else:
                            print('Valores que puedes digitar: 8, 9 o 10')
                    elif(desc_x_edad==2):
                        valor_entrada=(8100*num_entrada-desc_entrada)
                        print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_entrada)#dato de salida
                        break
                    else:
                        print('Digita valor 1 o 2')
                   
                except ValueError:
                    print("Ingresa un valor correcto.")
        else:
             #proceso 
            valor_entrada=8100*num_entrada
            print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_entrada)#dato de salida
    elif dia==2:
        while True:
            try:
                
                    desc_x_edad=int(input('QUIERE APLICAR DESCUENTO POR EDAD O DISCAPACIDAD: 1= SI 2= NO : '))
                    if desc_x_edad==1:
                        desc_edades()
                        valor_entrada=7000*num_entrada
                        desc_edad_num=int(input('ESCOJA EL NUMERO SEGUN SU EDAD O DISCAPACIDA: '))
                        if desc_edad_num==8:
                            valor_entrada_edad=(valor_entrada*10)/100
                            valor_final=valor_entrada-valor_entrada_edad
                            print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_final)
                            break
                        elif desc_edad_num==9:
                            valor_entrada_edad=(valor_entrada*20)/100
                            valor_final=valor_entrada-valor_entrada_edad
                            print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_final)
                            break
                        elif desc_edad_num==10:
                            valor_entrada_edad=(valor_entrada*15)/100
                            valor_final=valor_entrada-valor_entrada_edad
                            print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_final)
                            break
                        else:
                             print('Valores que puedes digitar: 8, 9 o 10')
                    elif desc_x_edad==2:
                        valor_entrada=7000*num_entrada
                        print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_entrada)#dato de salida
                        break
                    else:
                        print('Digita valor 1 o 2')

            except ValueError:
                print("Ingresa un valor correcto.")
    else:
        if dia==3:
            while True:
                try:
                    tarjeta_cine=int(input('¿CUENTA CON TARJETA CINEMEROS? 1: SI 2:NO '))#dato de entrada
                    if tarjeta_cine==1:
                        desc_entrada=(9000*5*num_entrada)/100
                        desc_x_edad=int(input('QUIERE APLICAR DESCUENTO POR EDAD O DISCAPACIDAD: 1= SI 2= NO : '))
                        if desc_x_edad==1:
                            desc_edades()
                            desc_edad_num=int(input('ESCOJA EL NUMERO SEGUN SU EDAD O DISCAPACIDA: '))
                            if desc_edad_num==8:
                                valor_entrada=(9000*num_entrada-desc_entrada)
                                valor_entrada_edad=(valor_entrada*10)/100
                                valor_final=valor_entrada-valor_entrada_edad
                                print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_final)
                                break
                            elif desc_edad_num==9:
                                valor_entrada=(9000*num_entrada-desc_entrada)
                                valor_entrada_edad=(valor_entrada*20)/100
                                valor_final=valor_entrada-valor_entrada_edad
                                print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_final)
                                break
                            elif desc_edad_num==10: 
                                valor_entrada=(9000*num_entrada-desc_entrada)
                                valor_entrada_edad=(valor_entrada*15)/100
                                valor_final=valor_entrada-valor_entrada_edad
                                break
                            else:
                                 print('Valores que puedes digitar: 8, 9 o 10')
                   
                        elif desc_x_edad==2:
                            valor_entrada=(9000*num_entrada-desc_entrada)
                            print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_entrada)#dato de salida
                            break
                        else:
                             print('Digita valor 1 o 2')
                    elif tarjeta_cine==2:
                        #proceso 
                        valor_entrada=9000*num_entrada
                        print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_entrada)#dato de salida
                        break
                    else:
                        print('Digita valor 1 o 2')
                except ValueError:
                    print("Ingresa un valor correcto.")

        elif dia==4:
            while True:
                try:
                    tarjeta_cine=int(input('¿CUENTA CON TARJETA CINEMEROS? 1: SI 2:NO '))#dato de entrada
                    if tarjeta_cine==1:
                        desc_entrada=(5000*7*num_entrada)/100
                        desc_x_edad=int(input('QUIERE APLICAR DESCUENTO POR EDAD O DISCAPACIDAD: 1= SI 2= NO : '))
                        if desc_x_edad==1:
                            desc_edades()
                            desc_edad_num=int(input('ESCOJA EL NUMERO SEGUN SU EDAD O DISCAPACIDA: '))
                            if desc_edad_num==8:
                                valor_entrada=(5000*num_entrada-desc_entrada)
                                valor_entrada_edad=(valor_entrada*10)/100
                                valor_final=valor_entrada-valor_entrada_edad
                                print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_final)
                                break
                            elif desc_edad_num==9:
                                valor_entrada=(5000*num_entrada-desc_entrada)
                                valor_entrada_edad=(valor_entrada*20)/100
                                valor_final=valor_entrada-valor_entrada_edad
                                print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_final)
                                break
                            elif desc_edad_num==10: 
                                valor_entrada=(5000*num_entrada-desc_entrada)
                                valor_entrada_edad=(valor_entrada*15)/100
                                valor_final=valor_entrada-valor_entrada_edad
                                break
                            else: 
                                print('Valores que puedes digitar: 8, 9 o 10')
                        elif desc_x_edad==2:
                            valor_entrada=(5000*num_entrada-desc_entrada)
                            print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_entrada)#dato de salida
                            break
                        else:
                            print('Digita valor 1 o 2')
                    elif tarjeta_cine==2:
                        #proceso 
                        valor_entrada=5000*num_entrada
                        print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_entrada)#dato de salida
                        break
                    else: 
                        print('Digita valor 1 o 2')
                except:
                    print("Ingresa un valor correcto.")
        else:
            if dia==5:
                while True:
                    try:
                        tarjeta_cine=int(input('¿CUENTA CON TARJETA CINEMEROS? 1: SI 2:NO '))#dato de entrada
                        if tarjeta_cine==1:
                            desc_entrada=(6800*4*num_entrada)/100
                            desc_x_edad=int(input('QUIERE APLICAR DESCUENTO POR EDAD O DISCAPACIDAD: 1= SI 2= NO : '))
                            if desc_x_edad==1:
                                desc_edades()
                                desc_edad_num=int(input('ESCOJA EL NUMERO SEGUN SU EDAD O DISCAPACIDA: '))
                                if desc_edad_num==8:
                                    valor_entrada=(6800*num_entrada-desc_entrada)
                                    valor_entrada_edad=(valor_entrada*10)/100
                                    valor_final=valor_entrada-valor_entrada_edad
                                    print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_final)
                                    break
                                elif desc_edad_num==9:
                                    valor_entrada=(6800*num_entrada-desc_entrada)
                                    valor_entrada_edad=(valor_entrada*20)/100
                                    valor_final=valor_entrada-valor_entrada_edad
                                    print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_final)
                                    break
                                elif desc_edad_num==10: 
                                    valor_entrada=(6800*num_entrada-desc_entrada)
                                    valor_entrada_edad=(valor_entrada*15)/100
                                    valor_final=valor_entrada-valor_entrada_edad
                                    break
                                else:
                                    print('Valores que puedes digitar: 8, 9 o 10')
                            elif desc_x_edad==2:
                                valor_entrada=(6800*num_entrada-desc_entrada)
                                print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_entrada)#dato de salida
                                break
                            else:
                                print('Digita valor 1 o 2')
                        elif tarjeta_cine==2:
                            #proceso 
                            valor_entrada=6800*num_entrada
                            print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_entrada)#dato de salida
                            break
                        else: 
                            print('Digita valor 1 o 2')
                    except:
                        print("Ingresa un valor correcto.")

            else:
                if dia==6:
                    while True:
                        try:
                            tarjeta_cine=int(input('¿CUENTA CON TARJETA CINEMEROS? 1: SI 2:NO '))#dato de entrada
                            if tarjeta_cine==1:
                                desc_entrada=(7400*3*num_entrada)/100
                                desc_x_edad=int(input('QUIERE APLICAR DESCUENTO POR EDAD O DISCAPACIDAD: 1= SI 2= NO : '))
                                if desc_x_edad==1:
                                    desc_edades()
                                    desc_edad_num=int(input('ESCOJA EL NUMERO SEGUN SU EDAD O DISCAPACIDA: '))
                                    if desc_edad_num==8:
                                        valor_entrada=(7400*num_entrada-desc_entrada)
                                        valor_entrada_edad=(valor_entrada*10)/100
                                        valor_final=valor_entrada-valor_entrada_edad
                                        print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_final)
                                        break
                                    elif desc_edad_num==9:
                                        valor_entrada=(7400*num_entrada-desc_entrada)
                                        valor_entrada_edad=(valor_entrada*20)/100
                                        valor_final=valor_entrada-valor_entrada_edad
                                        print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_final)
                                        break
                                    elif desc_edad_num==10: 
                                        valor_entrada=(7400*num_entrada-desc_entrada)
                                        valor_entrada_edad=(valor_entrada*15)/100
                                        valor_final=valor_entrada-valor_entrada_edad
                                        break
                                    else:
                                        print('Valores que puedes digitar: 8, 9 o 10')
                                else:
                                    valor_entrada=(7400*num_entrada-desc_entrada)
                                    print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_entrada)#dato de salida
                                    break
                            elif desc_x_edad==2:
                                #proceso 
                                valor_entrada=7400*num_entrada
                                print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_entrada)#dato de salida
                                break
                                
                            else: 
                                print('Digita valor 1 o 2')
                        except:
                            print("Ingresa un valor correcto.")
                            
                else:
                    if dia==7:
                        while True:
                            try:
                                desc_x_edad=int(input('QUIERE APLICAR DESCUENTO POR EDAD O DISCAPACIDAD: 1= SI 2= NO : '))
                                if desc_x_edad==1:
                                    desc_edades()
                                    valor_entrada=5000*num_entrada
                                    desc_edad_num=int(input('ESCOJA EL NUMERO SEGUN SU EDAD O DISCAPACIDA: '))
                                    if desc_edad_num==8:
                                        valor_entrada_edad=(valor_entrada*10)/100
                                        valor_final=valor_entrada-valor_entrada_edad
                                        print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_final)
                                        break
                                    elif desc_edad_num==9:
                                        valor_entrada_edad=(valor_entrada*20)/100
                                        valor_final=valor_entrada-valor_entrada_edad
                                        print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_final)
                                        break
                                    elif desc_edad_num==10:
                                        valor_entrada_edad=(valor_entrada*15)/100
                                        valor_final=valor_entrada-valor_entrada_edad
                                        print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_final)
                                        break
                                    else:
                                        print('Valores que puedes digitar: 8, 9 o 10')
                                elif desc_x_edad==2:
                                    valor_entrada=5000*num_entrada
                                    print('EL VALOR DE SU(S) ENTRADA(S) ES: $',valor_entrada)#dato de salida
                                    break
                                else:
                                    print('Digita valor 1 o 2')
                            except:
                                print("Ingresa un valor correcto.")


#funcion combos
def combos_comida():
    print(' ')
    print('--------------------------------------')
    print('               COMBOS                 ')
    print('--------------------------------------')
    tarjeta_cine=0
    print("_"*130)
    print('COMBOS                                                                          PRECIO NORMAL          PRECIO CON TARJETA CINEMEROS        ')
    print("""
1. DOS GASEOSAS GRANDES +1 CRISPETA GRANDE                                      $20900                        $18900
2. DOS GASEOSAS MEDIANAS +1 CRISPETA MEDIANA                                    $18300                        $16500
3. DOS GASEOSAS MEDIANAS +1 CRISPETA MEDIANAS +2 PERROS CALIENTES O SANDWICH    $29400                        $26500
4. UNA GASEOSA MEDIANA +1 CRISPETA PEQUEÑA +1 PERRO CALIENTES O SANDWICH        $18200                        $16400 """)   
    while True:
        try:
            numero_combo=int(input('ESCOJA UN COMBO SEGUN EL NUMERO: '))
            num_combos=int(input('CUANTAS COMBOS DESEA COMPRAR: '))  
            break
        except ValueError:
            print("Intentelo de nuevo, ingrese valores correctos.")


    if numero_combo==1:
        while True:
            try:
                tarjeta_cine=int(input('¿CUENTA CON TARJETA CINEMEROS? 1: SI 2:NO '))#dato de entrada
                if tarjeta_cine==1:
                    #proceso 
                    valor_combo=18900*num_combos
                    print('EL VALOR DEL COMBO ES: ',valor_combo)#dato de salida
                    break
                    
                elif tarjeta_cine==2:
                    #proceso 
                    valor_combo=20900*num_combos
                    print('EL VALOR DEL COMBO ES: ',valor_combo)#dato de salida
                    break
                else:
                    print('Digita valor 1 o 2')
            except ValueError:
                print("Intentelo de nuevo, ingrese valores correctos.")

    else: 
        if numero_combo==2:
            while True:
                try:
                    #proceso 
                    tarjeta_cine=int(input('¿CUENTA CON TARJETA CINEMEROS? 1: SI 2:NO '))
                    if tarjeta_cine==1:
                        valor_combo=16500*num_combos
                        print('EL VALOR DEL COMBO ES: ',valor_combo)#dato de salida
                        break
                    elif tarjeta_cine==2:
                        #proceso 
                        valor_combo=18300*num_combos
                        print('EL VALOR DEL COMBO ES: ',valor_combo)#dato de salida
                        break
                    else:
                        print('Digita valor 1 o 2')
                except ValueError:
                    print("Intentelo de nuevo, ingrese valores correctos.")
        else:
            if numero_combo==3:
                while True:
                    try:
                        #proceso 
                        tarjeta_cine=int(input('¿CUENTA CON TARJETA CINEMEROS? 1: SI 2:NO '))
                        if tarjeta_cine==1:
                            #proceso 
                            valor_combo=26500*num_combos
                            print('EL VALOR DEL COMBO ES: ',valor_combo)#dato de salida
                            break
                        elif tarjeta_cine==2:
                            #proceso 
                            valor_combo=29400*num_combos
                            print('EL VALOR DEL COMBO ES: ',valor_combo)#dato de salida
                            break
                        else:
                            print('Digita valor 1 o 2')
                    except ValueError:
                        print("Intentelo de nuevo, ingrese valores correctos.")
            else:
                if numero_combo==4:
                    while True:
                        try:
                            #proceso 
                            tarjeta_cine=int(input('¿CUENTA CON TARJETA CINEMEROS? 1: SI 2:NO '))
                            if tarjeta_cine==1:
                                #proceso 
                                valor_combo=16400*num_combos
                                print('EL VALOR DEL COMBO ES: ',valor_combo)#dato de salida
                                break
                            elif tarjeta_cine==2:
                                #proceso 
                                valor_combo=18200*num_combos
                                print('EL VALOR DEL COMBO ES: ',valor_combo) #dato de salida
                                break
                            else:
                                print('Digita valor 1 o 2')
                        except ValueError:
                            print("Intentelo de nuevo, ingrese valores correctos.")
                else:
                    print('Digite valor de 1-4')
                    combos_comida()

#funcion asientos
def asientos_cine():
    
    print('--------------------------------------')
    print('               ASIENTOS               ')
    print('--------------------------------------')
    #Funciones
    def generarMatriz(filas,columnas):
       
            matriz = []
            for f in range(filas):
                fila = []
                for c in range (columnas):
                    fila.append(0)
                matriz.append(fila)
            return matriz      
           

    def numerarAsientos(asientos):

            asientosNumero = [] 
            numero = 1
            for i in range (asientos):
                asientosNumero.append(numero)
                numero = numero + 1
            return asientosNumero
    
         

    def mostrarButacas(numeracion):
        print("NÚMERO DE ASIENTO")
        print(numeracion)
        print("BUTACAS")
        print("0 = Libres, 1 = ocupada")
    
                    
    def validarAsiento(asientosNumeros):
        while True:
            try:
                asiento = int(input("Seleccione el asiento que desea: "))
                cantidadDeAsientos = len(asientosNumeros)
                while ((asiento > cantidadDeAsientos) or (asiento < 1))and (asiento != -1):
                    asiento = int(input("El asiento seleccionado no existe. Seleccione nuevamente el asiento que desea"))     
                return asiento
            except ValueError:
                print("Intentelo de nuevo, ingrese valores correctos.")
        



    def generarFilasConLetras(matriz,filas,letras):
        letra = -1
        largoLetras = len(letras)
        contador = 0
        for f in range (filas): 
            letra = letras[f]
            indiceLetra = f 
            print("Fila",letra, matriz[f])
            contador = contador + 1
            letra = indiceLetra + 1
        return contador,letra
    

                    
    def obtenerIndiceDeFila(letras,fila):
        indiceFila = -1
        for i in range (len(letras)):
            if (fila == letras[i]):
                indiceFila = i
        return indiceFila
                       
                    
    def obtenerIndiceDeAsiento(columna):
        indiceDeAsiento = columna - 1
        return indiceDeAsiento
           

    def reservarAsientos(matriz,indiceFila,indiceColumna):
        asiento = matriz[indiceFila][indiceColumna]
        if asiento == 0:
            matriz[indiceFila][indiceColumna] = 1
            return True
        else:
            return False
          
        
    def cargarSala(matriz,columnas,filas):
        for i in range (filas): 
            for c in range (columnas):
                matriz[i][c] = random.randint(0,1)
               
                
    def calcularButacasLibres(matriz,filas,columnas):
        contador = 0
        for i in range (filas):
            for c in range (columnas):     
                if matriz[i][c] == 0:
                    contador = contador + 1
        return contador
       
            
    def mostrarButacasLibres(contador):
        print("La cantidad de butacas libres (0) es de",contador)
        

    def generarListaDeButacasDisponiblesPorFila(matriz,filas,columnas):
        butacasDisponiblesPorFila = []
        for f in range (filas): 
            contadorDeButacasLibresPorFila = 0
            for c in range (columnas):
                if matriz[f][c] == 0: 
                    contadorDeButacasLibresPorFila = contadorDeButacasLibresPorFila + 1  
            butacasDisponiblesPorFila.append(contadorDeButacasLibresPorFila)
        return butacasDisponiblesPorFila



    def calcularFilaConMasButacasContiguas(indiceDeFila,matriz,filas,columnas):
        mayorContinuidad = 0 #TOTALFILA
        filaConMayorContinuidad = -1 #Fila especifica
        for i in range (filas):
            contador = 0 
            continuidad = False #Inicio bandera en False, por default
            mayorContinuidadDeFila = 0 #Mayor continuidad de esa fila especifica
            for c in range (columnas):
                if matriz[i][c] == 0: #Si la columna de esa fila = 0, cambio valor de bandera y sumo 1
                    continuidad = True
                    contador = contador + 1        
                else:
                    if contador > mayorContinuidadDeFila: #Si la columna de esa fila es 1, me fijo si lo que sumé en el contador es
                                                            #mayor que lo que ya guardé en la mayor continuidadDeFila, si lo es, la mayor continuidad de la fila
                                                            #pasa a valer lo que el contador. E inicio nuevamente el contador en 0
                        mayorContinuidadDeFila = contador
                    contador = 0
            if mayorContinuidadDeFila > mayorContinuidad: #Si la mayor continuidad de esa fila es mayor a la continuidad ya guardada, la mayor continuidad pasa a valor
                                                        #la mayor continuidad de esa fila y por ultimo guardamos el indice de la fila con mayor COntinuidad para devolver
                mayorContinuidad = mayorContinuidadDeFila
                filaConMayorContinuidad = i
        return filaConMayorContinuidad
       
            
    def mostrarListaDeButacasDisponiblesPorFila (listaDeButacasDisponiblesPorFila,matriz,filas,letras):
        for i in range (filas): 
            print("La fila",letras[i],"posee",listaDeButacasDisponiblesPorFila[i],"asientos disponibles")
           

    def mostrarFilaConMasButacasContiguasVacias(butacasContiguas,letras):
        print("La fila con más butacas contiguas es la ",letras[butacasContiguas])
               

    #Main
    letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","W","X","Y","Z"]
    filas = random.randint(15,20)
    asientos = random.randint(15,20)
    numeracion = numerarAsientos(asientos)
    matriz = generarMatriz(filas,asientos)
    mostrarButacas(numeracion)
    cantidadDeFilas,letra = generarFilasConLetras(matriz,filas,letras)
    asiento = validarAsiento(numeracion)
    while asiento != -1:
        while True:
            try:
                indiceAsiento = obtenerIndiceDeAsiento(asiento)
                fila = (input("Ingrese la fila que desea: "))
                indiceDeFila = obtenerIndiceDeFila(letras,fila)
                while (indiceDeFila == -1) or (indiceDeFila >= filas):
                    fila = (input("ERROR. Fila inexistente.Ingrese la fila que desea: "))
                    indiceDeFila = obtenerIndiceDeFila(letras,fila)  
                    
                resultadoDeReserva = reservarAsientos(matriz,indiceDeFila,indiceAsiento)
                if resultadoDeReserva == True:
                    print("La reserva se ha generado con éxito")
                    salir_silla=int(input('escriba 1 si desea salir al menu: '))
                    if salir_silla==1:
                        break
                    
                else:
                    print("El asiento se encuentra reservado. Intentelo nuevamente")
            except ValueError:
                print("Intentelo de nuevo, ingrese valores correctos.")
        mostrarButacas(numeracion)
        cantidadDeFilas,letra = generarFilasConLetras(matriz,filas,letras)
        asiento = validarAsiento(numeracion)

       
    print("Ocupación de sala")   
    cargarSala(matriz,asientos,filas)
    cantidadDeFilas,letra = generarFilasConLetras(matriz,filas,letras)   
    butacasLibres = calcularButacasLibres(matriz,filas,asientos)
    mostrarButacasLibres(butacasLibres)
    listaDeButacasDisponiblesPorFila = generarListaDeButacasDisponiblesPorFila(matriz,filas,asientos)
    mostrarListaDeButacasDisponiblesPorFila(listaDeButacasDisponiblesPorFila,matriz,filas,letras)
    butacasContiguas = calcularFilaConMasButacasContiguas(indiceDeFila,matriz,filas,asientos)
    mostrarFilaConMasButacasContiguasVacias(butacasContiguas,letras)
    
    
#funcion salir
def salida():
    print('--------------------------------------')
    print('         ADIOS,VUELVA PRONTO          ')
    print('--------------------------------------')
    sys.exit() 


os.system("cls")
while True:
    
    def menu():
        print('--------------------------------------')
        print(' ¡BIENVENIDO AL SISTEMA DE CINEMEROS! ')
        print('--------------------------------------')
        print('--------------------------------------')
        print('            MENU CINEMEROS            ')
        print('--------------------------------------')
        print ("""     
        1. VALOR ENTRADA
        2. COMBOS DE COMIDA
        3. ASIENTOS
        4. SALIR""")
    menu()
    while True:
        try:
            opcion=int(input('¿QUE DESEA REALIZAR? '))
            break
        except ValueError:
            print ("Digita un valor valido, intentadolo de nuevo.")

    if opcion==1:
        entradas_cine() #llamamos la fncion entrada1  
    elif opcion==2:#llamamos la funcion combos_comida
        combos_comida()
    else:
        if opcion==3:#llamamos la funcion asientos_cine
            asientos_cine()
        elif opcion==4:
            salida()#llamamos la funcion salida
        else:
            print("Digite un valor del 1-4")
