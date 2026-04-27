import pandas as pd

def merge(df_clientes, df_ventas):
    df_clientes.columns = [c.strip().lower() for c in df_clientes.columns]
    df_ventas.columns = [c.strip().lower() for c in df_ventas.columns]
    
    columna_union = 'id'
    
    if columna_union not in df_clientes.columns or columna_union not in df_ventas.columns:
        print("Error: No se encontró la columna 'id' en los archivos.")
        return None

    df_unido = pd.merge(df_clientes, df_ventas, on=columna_union, how='inner')
    return df_unido