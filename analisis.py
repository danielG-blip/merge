import pandas as pd

def analisis(df_ventas):
    if df_ventas is None:
        print("No hay datos para analizar. El mergeo falló.")
        return

    print("Traer a las personas por país")
    print("Colombia")
    mascara_Colombia = df_ventas["Pais"] == "Colombia"
    df_ventas_Colombia = df_ventas[mascara_Colombia]
    print(df_ventas_Colombia)

    print("Traer a las personas que tengan un salario mayor a 40.000")
    mascara_salario = df_ventas["Salario"] > 40000
    df_salario_mayor = df_ventas[mascara_salario]
    print(df_salario_mayor)
    
    print("Promedio de las ventas")
    print(df_ventas["total"].mean())
    
    print("Total de ventas")
    print(df_ventas["total"].sum())

    print("Total de las ventas por país")
    print(df_ventas.groupby("Pais")["total"].sum())