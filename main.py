import pandas as pd
import matplotlib as plt

new_dataframe = pd.read_csv('Data/cars_2010_2020.csv')
new_dataframe['Price (USD)'] = new_dataframe['Price (USD)'].astype(float)
new_dataframe['Price (AUD)'] = new_dataframe['Price (USD)'].multiply(1.5)
new_dataframe = new_dataframe.astype({'Engine Size (L)':'float','Price (AUD)':'float'})
print(new_dataframe)

