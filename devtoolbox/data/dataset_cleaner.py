# devtoolbox/data/dataset_cleaner.py

import pandas as pd
import numpy as np

class DatasetCleaner:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def clean_column_names(self):
        """Standardize column names: lowercase and replace spaces with underscores"""
        self.df.columns = (
            self.df.columns.str.strip().str.lower().str.replace(" ", "_")
        )
        return self

    def drop_missing(self, threshold=0.5):
        """Drop columns with missing value ratio above threshold"""
        missing_ratio = self.df.isnull().mean()
        to_drop = missing_ratio[missing_ratio > threshold].index
        self.df.drop(columns=to_drop, inplace=True)
        return self

    def fill_missing(self, strategy="mean", fill_value=None):
        """Fill missing values using a strategy or fixed value"""
        for col in self.df.select_dtypes(include=[np.number]).columns:
            if self.df[col].isnull().any():
                if strategy == "mean":
                    self.df[col] = self.df[col].fillna(self.df[col].mean())
                elif strategy == "median":
                    self.df[col] = self.df[col].fillna(self.df[col].median())
                elif strategy == "zero":
                    self.df[col] = self.df[col].fillna(0)
                elif strategy == "value" and fill_value is not None:
                    self.df[col] = self.df[col].fillna(fill_value)
        return self

    def remove_duplicates(self):
        """Remove duplicate rows"""
        self.df.drop_duplicates(inplace=True)
        return self

    def get_cleaned(self):
        """Return cleaned DataFrame"""
        return self.df
