import pandas as pd

def limpiar_clientes (df_clientes):
        
    df_clientes['nombre'] = df_clientes['nombre'].str.strip().str.title()
    df_clientes['email'] = df_clientes['email'].str.strip().str.lower() 
    df_clientes['fecha_nacimiento'] = df_clientes['fecha_nacimiento'].str.strip()
    df_clientes['telefono'] = df_clientes['telefono'].str.strip()
    df_clientes['pais'] = df_clientes['pais'].str.strip().str.title()
    df_clientes['categoria'] = df_clientes['categoria'].str.strip().str.title()
    df_clientes['fecha_registro'] = df_clientes['fecha_registro'].str.strip()

    df_clientes = df_clientes.drop_duplicates()

    df_clientes['salario'] = pd.to_numeric(df_clientes['salario'], errors='coerce')
    df_clientes['salario'] = df_clientes['salario'].fillna(df_clientes['salario'].mean())
    df_clientes['telefono'] = df_clientes['telefono'].fillna('0000000')
    df_clientes['pais'] = df_clientes['pais'].fillna('Desconocido')
    df_clientes['nombre'] = df_clientes['nombre'].fillna('Desconocido')
    df_clientes['email'] = df_clientes['email'].fillna('No_email')
    df_clientes['fecha_nacimiento'] = df_clientes['fecha_nacimiento'].fillna('Desconocida')
    df_clientes['categoria'] = df_clientes['categoria'].fillna('No_categoria')

    df_clientes['salario'] = df_clientes['salario'].astype('int64')
    df_clientes['fecha_nacimiento'] = pd.to_datetime(df_clientes['fecha_nacimiento'], errors='coerce')
    df_clientes['fecha_registro'] = pd.to_datetime(df_clientes['fecha_registro'], errors='coerce')

    df_clientes.info()

    return df_clientes

def limpiar_ventas (df_ventas):

    df_ventas['producto'] = df_ventas['producto'].str.strip().str.title()
    df_ventas['cantidad_vendida'] = df_ventas['cantidad_vendida'].str.strip()
    df_ventas['precio_unitario'] = df_ventas['precio_unitario'].str.strip()
    df_ventas['total'] = df_ventas['total'].str.strip()
    df_ventas['fecha_venta'] = df_ventas['fecha_venta'].str.strip()

    df_ventas = df_ventas.drop_duplicates()
    
    df_ventas['cantidad_vendida'] = pd.to_numeric(df_ventas['cantidad_vendida'], errors='coerce').fillna(0).astype('int64')
    df_ventas['precio_unitario'] = pd.to_numeric(df_ventas['precio_unitario'], errors='coerce')
    df_ventas['precio_unitario'] = df_ventas['precio_unitario'].fillna(df_ventas['precio_unitario'].mean()).astype('int64')
    df_ventas['total'] = pd.to_numeric(df_ventas['total'], errors='coerce').fillna(0).astype('int64')
    df_ventas['fecha_venta'] = pd.to_datetime(df_ventas['fecha_venta'], errors='coerce')

    df_ventas.info()
    
    return df_ventas