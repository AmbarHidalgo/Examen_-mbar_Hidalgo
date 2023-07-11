import Funciones as fu
platinum= 120000
gold= 80000
silver= 50000
contp= 0
contg= 0
conts= 0
cantp=0
cantg=0
cants=0

while True:
    fu.limpiarpantalla
    print("""
    ********************
        VENTA ENTRADAS
    ********************
    1) Comprar entradas
    2) Mostrar ubicaciones disponibles
    3) Ver listado de asistentes
    4) Mostrar ganancias totales
    0) Salir""")
    opcion=int(input("Seleccione una opcion : "))
    if opcion>=0 and opcion<=4:
        if opcion==0:
            print("Ha seleccionado salir, Adiós")
            break
        elif opcion==1:
            print("COMPRAR ENTRADAS")
            print(f"""
            *****************
            TIPO DE ENTRADAS:
            *****************
            1) Platinum ${platinum}
            2) Gold     ${gold}
            3) Silver   ${silver}""")
            opcion=int(input("Seleccione una entrada :"))
        
            if opcion==1:
                print("Ha seleccionado entrada Platinum")
                cantidad=int(input("Cuantas entradas desea llevar? (maximo 3 entradas) :"))
                if cantidad>=1 and cantidad<=3:
                    contp+=1
                    cantp+=1
                else:
                    print("Cantidad no válida")
                
            if opcion==2:
                print("Ha seleccionado entrad Gold")
                cantidad=int(input("Cuantas entradas desea llevar? (maximo 3 entradas) :"))
                if cantidad>=1 and cantidad<=3:
                    contg+=1
                    cantg+=1
            if opcion==3:
                print("Ha seleccionado entrada Silver")
                cantidad=int(input("Cuantas entradas desea llevar? (maximo 3 entradas) :"))
                if cantidad>=1 and cantidad<=3:
                    conts+=1
                    cants+=1

        elif opcion==2:
            print("UBICACIONES DISPONIBLES")
        
        elif opcion==3:
            print("LISTADO ASISTENTES")
        
        elif opcion==4:
            print("GANANCIAS TOTALES")
            print(f"""
            *********************
              GANANCIAS TOTALES
            *********************
            -------------------------------------------------
            TIPO ENTRADA        | CANTIDAD |   TOTAL
            ------------------------------------------------
            PLATINUM ${platinum}|{cantp}   | {cantp*platinum}        
            GOLD     ${gold}    |{cantg}   | {cantg*gold}       
            SILVER   ${silver}  |{cants}   | {cants*silver}""")
    else:
        print("Opción no valida")