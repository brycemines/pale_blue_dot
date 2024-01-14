'''
Exploratory Data Analysis of CSV Files

This file contains a class that reads a csv file, cleans the data, selects the
wanted columns, shows the pygwalker interactive plotter, and returns a pandas dataframe.
'''

import pandas as pd
import numpy as np
from typing import List
import pygwalker as pyg


class CSVData:
    '''
    This class reads a csv file, cleans the data, selects the wanted columns,
    and returns a pandas dataframe.
    '''

    filename: str
    df: pd.DataFrame

    def __init__(self, filename: str):
        '''
        Constructor for ReadCSV class.
        '''
        self.filename = filename
        self.df = pd.DataFrame()
        self.read_csv()


    def read_csv(self) -> None:
        '''
        This function reads a csv file, cleans the data, selects the wanted
        columns, and returns a pandas dataframe.
        '''
        # Read csv file
        self.df = pd.read_csv(self.filename)


    def clean_data(self) -> None:
        '''
        This function cleans the data in the dataframe.
        '''
        # Remove rows with empty strings
        self.df = self.df.replace(r'^\s*$', np.nan, regex=True)
        self.df = self.df.dropna()


    def select_wanted_columns(self, wanted_columns: List[str]) -> None:
        '''
        This function selects the wanted columns from the dataframe.
        '''
        self.df = self.df[wanted_columns]


    def display_stats(self) -> None:
        '''
        This function prints the name of the csv file, the number of rows in the
        current dataframe, the number of columns, the column names, and the
        first 5 rows of the dataframe.
        '''
        print('Filename: ' + self.filename)
        print('Number of rows: ' + str(self.df.shape[0]))
        print('Number of columns: ' + str(self.df.shape[1]))
        print('Column names: ')
        print(self.df.columns)
        print('First 5 rows: ')
        print(self.df.head(5))


    def show(self) -> None:
        '''
        This function visualizes the data in the dataframe using PyGWalker.
        '''
        pyg.walk(self.df)


    def get_dataframe(self) -> pd.DataFrame:
        '''
        This function returns the dataframe.
        '''
        return self.df


    def save_dataframe(self, filename: str) -> None:
        '''
        This function saves the dataframe to a csv file.
        '''
        self.df.to_csv(filename, index=False)
    