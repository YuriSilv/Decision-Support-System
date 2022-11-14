import pandas as pd
import matplotlib
import numpy as np

from abc import ABC, abstractmethod

class pre_process(ABC):
    def __init__(self, dataframe):
        self.dataframe = dataframe

    @abstractmethod
    def clean_df():
        pass

class graphic_analysis():
    pass

class model_analysis():
    pass

