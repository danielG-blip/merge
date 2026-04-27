import pandas as pd
import os

def carga_cliente():
    ruta = os.path.join(os.getcwd(), 'data', 'raw', 'clientes.csv')
    return pd.read_csv(ruta, sep=None, engine='python')

def carga_ventas():
    ruta = os.path.join(os.getcwd(), 'data', 'raw', 'ventas.csv')
    return pd.read_csv(ruta, sep=None, engine='python')