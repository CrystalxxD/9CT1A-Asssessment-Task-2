import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
while True:
    User_Want = input("[1] - Original dataframe [2] - All data from data frame | [3] - Choose what data you want | [4] - Graph of all the data | [5] - Quit Program | Pick a number between 1 and 5:  ")
    if User_Want == '1':
        new_dataframe = pd.read_csv('Data/cars_2010_2020.csv')
        print(new_dataframe)
        
    elif User_Want == '2':
        new_dataframe = pd.read_csv('Data/cars_2010_2020.csv')
        new_dataframe['Price (USD)'].astype(float)
        new_dataframe['Price (AUD)'] = new_dataframe['Price (USD)'].multiply(1.5)
        new_dataframe = new_dataframe.astype({'Engine Size (L)':'float','Price (AUD)':'float'})
        print(new_dataframe)


    elif User_Want == '3':
        new_dataframe = pd.read_csv('Data/cars_2010_2020.csv')
        new_dataframe['Price (USD)'].astype(float)
        new_dataframe['Price (AUD)'] = new_dataframe['Price (USD)'].multiply(1.5)
        new_dataframe = new_dataframe.astype({'Engine Size (L)':'float','Price (AUD)':'float'})
        word_to_search = str(input("What word do you want to find in the data frame e.g Toyota, Corolla, 2020, Hybrid: "))

        new_word_to_search = str(input("Is there any more words or number you want to find. If not enter same word the question before: "))

        new_new_word_to_search = str(input("Is there any more words or number you want to find. If not enter same word the question before: "))

        # Search for the word in the entire DataFrame
        result = new_dataframe[new_dataframe.apply(lambda row: row.astype(str).str.contains(word_to_search).any(), axis=1)]

        new_result = result[result.apply(lambda row: row.astype(str).str.contains(new_word_to_search).any(), axis=1)]

        new_new_result = new_result[new_result.apply(lambda row: row.astype(str).str.contains(new_new_word_to_search).any(), axis=1)]

        # Display the result
        print(new_new_result)

        graph = str(input("What type of graph do you want. Options are scatter, bar, pie : "))
        x_value = str(input("What do you want on the x axis e.g Brand, Model, Year, Engine Size (L), Fuel Type, Price (USD), Price (AUD): ")) 
        y_value = str(input("What do you want on the y axis e.g Brand, Model, Year, Engine Size (L), Fuel Type, Price (USD), Price (AUD) | If you choose pie type the same input as above: "))
        title_name = str(input("What name do you want for a title:  "))
        if graph == 'scatter' or 'bar':
            new_dataframe.plot(
                                kind = graph,
                                x = x_value,
                                y = y_value,
                                color='blue',
                                alpha=0.3,
                                title= title_name
                                )
            plt.show()
        elif graph == 'pie':
            category_counts = new_dataframe[x_value ].value_counts()

            # Create pie chart
            plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)

            # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.axis('equal')

            # Display the pie chart
            plt.show()

    elif User_Want == '4':
        new_dataframe = pd.read_csv('Data/cars_2010_2020.csv')
        new_dataframe['Price (USD)'].astype(float)
        new_dataframe['Price (AUD)'] = new_dataframe['Price (USD)'].multiply(1.5)
        new_dataframe = new_dataframe.astype({'Engine Size (L)':'float','Price (AUD)':'float'})    
        graph = str(input("What type of graph do you want. Options are scatter, bar, pie : "))
        x_value = str(input("What do you want on the x axis e.g Brand, Model, Year, Engine Size (L), Fuel Type, Price (USD), Price (AUD): ")) 
        y_value = str(input("What do you want on the y axis e.g Brand, Model, Year, Engine Size (L), Fuel Type, Price (USD), Price (AUD) | If you choose pie type the same input as above: "))
        title_name = str(input("What name do you want for a title:  "))
        if graph == 'scatter' or 'bar':
            new_dataframe.plot(
                                kind = graph,
                                x = x_value,
                                y = y_value,
                                color='blue',
                                alpha=0.3,
                                title= title_name
                                )
            plt.show()
        elif graph == 'pie':
            category_counts = new_dataframe[x_value ].value_counts()

            # Create pie chart
            plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)

            # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.axis('equal')

            # Display the pie chart
            plt.show()

        else:
            print("Not a valid option")
    elif User_Want == '5':
        print('Thank you for using the program. The dataframe was sourced from https://www.kaggle.com/datasets/waqi786/cars-dataset-2010-2020')
        break
    else:
        print("Not a valid option") 