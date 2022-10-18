#!/usr/bin/python3

from multiprocessing.connection import Connection
import os
import json
import sqlparse

import pandas as pd
import numpy as np

import connection
import conn_warehouse

if __name__ == '__main__':
    print(f"[INFO] Service ETL Memulai .....")
    conn_dwh, engine_dwh  = conn_warehouse.conn()
    cursor_dwh = conn_dwh.cursor()

    conf = connection.config('postgresql')
    conn, engine = connection.psql_conn(conf)
    cursor = conn.cursor()

    path_query = os.getcwd()+'/query/'
    query = sqlparse.format(
        open(
            path_query+'query.sql','r'
            ).read(), strip_comments=True).strip()

    querydimuser = sqlparse.format(
        open(
            path_query+'query_transaction.sql','r'
            ).read(), strip_comments=True).strip()

    queryfactorders = sqlparse.format(
        open(
            path_query+'query_barang.sql','r'
            ).read(), strip_comments=True).strip()
            
            
    query_dwh = sqlparse.format(
        open(
            path_query+'dwh_pelanggan.sql','r'
            ).read(), strip_comments=True).strip()

    querydwhdimuser = sqlparse.format(
        open(
            path_query+'dwh_transaction.sql','r'
            ).read(), strip_comments=True).strip()

    querydwhfactorders = sqlparse.format(
        open(
            path_query+'dwh_barang.sql','r'
            ).read(), strip_comments=True).strip()

    try:
        print(f"[INFO] Service ETL Sedang Berjalan .....")
        df = pd.read_sql(query, engine)
        dfusers = pd.read_sql(querydimuser, engine)
        dffact = pd.read_sql(queryfactorders, engine)
        
        cursor_dwh.execute(query_dwh)
        cursor_dwh.execute(querydwhdimuser)
        cursor_dwh.execute(querydwhfactorders)
        conn_dwh.commit()

        dfusers.to_sql('dwh_transaksi', engine_dwh, if_exists='append', index=False)
        print(f"[INFO] Service ETL dim users sukses .....")
        dffact.to_sql('dwh_barang', engine_dwh, if_exists='append', index=False)
        print(f"[INFO] Service ETL fact orders sukses .....")
        df.to_sql('dwh_pelanggan', engine_dwh, if_exists='append', index=False)
        print(f"[INFO] Service ETL dim orders sukses .....")
    except:
        print(f"[INFO] Service ETL is Gagal .....")

    

    