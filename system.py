import pandas as pd
import matplotlib
import numpy as np

from abc import ABC, abstractmethod

class pre_process(ABC):
    def __init__(self, dataframe:str):
        self.dataframe = pd.read_csv(f'data/{dataframe}')

    @abstractmethod
    def clean_df(self, year:int):
        self.dataframe.drop_duplicates(inplace=True)
        df_recorte = self.dataframe[['Auction Title ', 'Department ', 'Close Date ','Winning Bid ','CC Fee', 'Auction Fee Total','Pay Status ','Expenses']].copy()
        df_recorte = df_recorte.convert_dtypes()
        df_recorte['Close Date '] = pd.to_datetime(df_recorte['Close Date '])
        df_recorte = df_recorte[df_recorte['Pay Status '] == 'Successful']
        df_recorte.Expenses.fillna(0,inplace=True)
        df_recorte['CC Fee'].fillna(0,inplace=True)
        df_year = df_recorte[df_recorte['Close Date '].dt.year == year]
        return df_year

class graphic_analysis():
    pass

class model_analysis():
    pass

