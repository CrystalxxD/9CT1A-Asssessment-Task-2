import pandas as pd
import matplotlib as plt
import numpy as np

new_dataframe = pd.read_csv('Data/cars_2010_2020.csv')
new_dataframe['Price (USD)'] = new_dataframe['Price (USD)'].astype(float)
new_dataframe['Price (AUD)'] = new_dataframe['Price (USD)'].multiply(1.5)
new_dataframe = new_dataframe.astype({'Engine Size (L)':'float','Price (AUD)':'float'})
print(new_dataframe)

# Word to search for
word_to_search = 'Toyota'

# Search for the word in the entire DataFrame
result = new_dataframe[new_dataframe.apply(lambda row: row.astype(str).str.contains(word_to_search).any(), axis=1)]

# Display the result
print(result)

new_dataframe.plot(
               kind='scatter',
               x='Brand',
               y='Model',
               color='blue',
               alpha=0.3,
               title='Test'
              )
