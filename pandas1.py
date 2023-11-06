from pathlib import Path

import pandas

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / 'data'

# creating a dataframe with python dictionary

product_dict = {
    'date': ['15/02/2021', '16/02/2021'],
    'value': [500, 300],
    'produto': ['rice', 'potato'],
    'quantity': [50, 70],
}

product_dataframe = pandas.DataFrame(product_dict)

# print(product_dataframe)


# DATAFRAME WITH EXCEL

vendas_dataframe = pandas.read_excel(DATA_DIR / 'Vendas.xlsx')

''' print(vendas_dataframe) '''


# HEAD - SHOWS N ROWS OF THE DATAFRAME

''' print(vendas_dataframe.head()) '''


# SHAPE - SHOWS THE NUMBER OF COLUMNS AND ROWS

''' print(vendas_dataframe.shape) '''


# DESCRIBE - WILL GENERATE SOME STATISTICS OF THE DATA

''' print(vendas_dataframe.describe()) '''


# GETTING A SINGLE COLUMN OF THE TABLE - pandas.Series = column

''' products = vendas_dataframe.get('Produto', 'NO RESULTS FOUND')
print(products) '''


# GETTING TWO OR MORE COLUMNS - table

''' products = vendas_dataframe.get(['Produto', 'ID Loja'], 'NO RESULTS FOUND')
print(products) '''


# .loc METHOD - GETTING ROWS BY INDEX - Series

''' print(vendas_dataframe.loc[1:5]) '''


# GETTING ROWS WITH A CONDITION

condition = vendas_dataframe['ID Loja'] == 'Norte Shopping'
''' print(vendas_dataframe.loc[condition]) '''


# CONDITION WITH SELECTED COLUMNS

''' print(vendas_dataframe.loc[condition].get(['Data', 'Produto', 'Quantidade'])) '''


# LOC [ROW, COLUMN]

''' print(vendas_dataframe.loc[1, 'Produto']) '''


# ADD A NEW COLUMN BY A EXISTING COLUMN

# IT WILL CREATE A COLUMN IF THE VALUE DOES NOT EXIST
vendas_dataframe['Comissao'] = vendas_dataframe['Valor Final'] * 0.05
''' print(vendas_dataframe) '''

# COLUMN WITH A DEFAULT VALUE
vendas_dataframe.loc[:, 'Imposto'] = 0
''' print(vendas_dataframe) '''


# CONCAT TWO DATAFRAMES WITH IDENTICAL COLUMNS

# NEW DATAFRAME
vendas_dez_dataframe = pandas.read_excel(DATA_DIR / 'Vendas - Dez.xlsx')

# CONCAT
vendas_concat = pandas.concat([vendas_dataframe, vendas_dez_dataframe])
''' print(vendas_concat) '''


# DELETE ROWS AND COLUMNS THAT ARE Null - DROPNA

# delete where rows and cols are null
vendas_concat = vendas_concat.dropna(how='all')

# delete where rows are null - axis = 0 = rows
vendas_concat = vendas_concat.dropna(how='all', axis=0)

# delete where cols are null - axis = 1 = columns
vendas_concat = vendas_concat.dropna(how='all', axis=1)

# delete rows that have at least one null value
vendas_concat = vendas_concat.dropna()


# FILL NULL VALUES - FILLNA

# fill with average of the column - mean
''' vendas_concat['Comissao'].fillna(vendas_concat['Comissao'].mean())
print(vendas_concat['Comissao']) '''

# fill with the last value - ffill
''' vendas_concat = vendas_concat.ffill() '''


# GROUP BY & VALUE COUNTS

# count values
transactions_count = vendas_concat['ID Loja'].value_counts()
''' print(transactions_count) '''

# group by
product_bill = vendas_concat[['Produto', 'Valor Final']].groupby('Produto')
''' print(product_bill.sum(numeric_only=True)) '''


# MERGING TWO DATAFRAMES - merge

gerentes_dataframe = pandas.read_excel(DATA_DIR / 'Gerentes.xlsx')

data_merge = vendas_concat.merge(gerentes_dataframe)
print(data_merge)
