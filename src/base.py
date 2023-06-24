import pandas as pd 
import requests 

class Base: 
    def __init__(self):
        self.df = None
        self.csv_file = r'capstone002_Cleaned.csv'
        #self.api_url = 'C:\Users\xende\Downloads\CausesOfDeath_France_2001-2008.csv'
        #self.get_data()

    def return_string(self):
        return self.csv_file
    #def clean_data(self):
        # drop the columns that has not approprite data information

        # drop_columns = ['AGE', 'Flag and Footnotes']
        #  # I am dropping "Flag and Footnotes" becasue the entire columns has no data on it

        # df = df.drop(columns=drop_columns)





    

    def get_data(self):
        """ Scraping the data from the API and create dataframe object from it """
        response = requests.get(self.csv_file)
        r = response.json()
        response1 = requests.get(r)
        self.df = pd.DataFrame.from_dict(response1.json())
        return self.df
    

if __name__ == '__main__':
    c = Base()
    print(c.return_string())
    print(c.df())
    c.df.to_csv('capstone002_Cleaned.csv')