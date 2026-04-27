import carga
import limpieza
import merge 
import analisis

limpieza_realizada = False
carga_realizada = False
mergeo_realizado = False

df_cliente_carga = None
df_ventas_carga = None
df_cliente_limpieza = None
df_ventas_limpieza = None
df_clientes_ventas = None

while True:
    print("""
1. Cargar DataFrame.
2. Ejecutar Limpieza.
3. Ejecutar Mergeo (Unión).
4. Cargar Análisis.
5. Salir.
    """)
    
    opcion = input("Selecciona la opcion de tu interes: ")

    match opcion:
        case "1":
            print('Proceso de carga clientes en ejecucion')
            df_cliente_carga = carga.carga_cliente()
            print('Proceso de Carga clientes, finalizando correctamente')
            
            print('Proceso de carga ventas en ejecucion')
            df_ventas_carga = carga.carga_ventas()
            print('Proceso de Carga ventas, finalizando correctamente')
            
            carga_realizada = True

        case "2":
            if not carga_realizada:
                print("Se debe cargar datos previamente")
            else:
                print('Proceso de limpieza clientes, en ejecucion...')
                df_cliente_limpieza = limpieza.limpiar_clientes(df_cliente_carga)
                
                print('Proceso de limpieza ventas, en ejecucion...')
                df_ventas_limpieza = limpieza.limpiar_ventas(df_ventas_carga)
                
                limpieza_realizada = True
                print('Limpieza finalizada correctamente')

        case "3":
            if not carga_realizada:
                print("Debes realizar la carga primero")
            elif not limpieza_realizada:
                print("Debes realizar la carga y la limpieza primero")
            else:
                print("Ejecutando mergeo de datos...")
                df_clientes_ventas = merge.merge(df_cliente_limpieza, df_ventas_limpieza)
                mergeo_realizado = True
                print("Mergeo finalizado con éxito.")

        case "4":
            if not mergeo_realizado:
                print("Debes realizar el mergeo primero")
            else:
                print("Proceso de analisis, en ejecucion...")
                analisis.analisis(df_clientes_ventas)

        case "5":
            print("Saliendo del programa...")
            break

        case _:
            print("Seleccione una opcion valida")