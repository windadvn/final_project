#!/usr/bin/python3

from datetime import datetime
import os
import sqlparse
import pandas as pd
import connection
from pyspark.sql.functions import month

def query(file):
    path = open(os.getcwd()+'/query/'+file, 'r').read()
    query = sqlparse.format(path, strip_comments=True).strip()
    return query

if __name__ == '__main__':
    
    df = pd.read_sql(query('top_produk.sql'), connection.database())
    df.to_sql('top_produk', connection.warehouse(), if_exists='replace', index=False)
    
    
    df2 = pd.read_sql(query('transaksi_tiap_wilayah.sql'), connection.database())
    df2.to_sql('transaksi_tiap_wilayah', connection.warehouse(), if_exists='replace', index=False)

    filetime = datetime.now().strftime('%Y%m%d')

    path = os.getcwd()+'/local/'
    if not os.path.exists(path):
        os.makedirs(path)
    df.to_csv(f'{path}top_produk{filetime}.csv', index=False)
    df2.to_csv(f'{path}transaksi_tiap_wilayah{filetime}.csv', index=False)

    spark = connection.spark('spark')
    spark.createDataFrame(df).groupBy('produk').sum('amount').toPandas().to_csv(f'{os.getcwd()}/output/sum_produk.csv', index=False)
    spark.createDataFrame(df2).groupBy('country').sum('amount').toPandas().to_csv(f'{os.getcwd()}/output/sum_country.csv', index=False)