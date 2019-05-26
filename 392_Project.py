import pandas as pd
excel_file = r"C:\Users\Michael\Downloads\Records.csv"

df = pd.read_csv(excel_file)
print(df.head(10))

#Saves the max value in column total profit to variable max_profit_amount
max_profit_amount = (df['Total Profit'].max())

#Searches for the row im which Total Profit is equal to max_profit_amount
#Saves the index of the row df_make_profit_id as a value
df_max_profit_id = df.loc[df['Total Profit'] == max_profit_amount]
index_max_profit = (df_max_profit_id.index.values)

#Converts panda's datafram row to dict where keys are column names and values are lists of column data
#Assigns max_profit_id the value of the key Order ID
dict_max_profit_id = df_max_profit_id.to_dict('list')
max_profit_id = (dict_max_profit_id['Order ID'])

id_max_profit = df.loc[df['Total Profit'] == max_profit_amount, 'Order ID'].item()

print(f"The max profit is: ${max_profit_amount}")
print(f"Found in order #: {id_max_profit}")
print(f"At index value: {index_max_profit}")



#print(df.loc[1][1])
#print(df.loc[1]['Country'])