# tests/test_dataset_cleaner.py

import unittest
import pandas as pd
from devtoolbox.data.dataset_cleaner import DatasetCleaner

class TestDatasetCleaner(unittest.TestCase):
    def setUp(self):
        data = {
            'Name ': ['Alice', 'Bob', 'Charlie', 'Alice'],
            'Age': [25, None, 30, 25],
            'Income': [50000, 60000, None, 50000],
            'City': ['NY', 'LA', 'NY', 'NY']
        }
        self.df = pd.DataFrame(data)

    def test_clean_column_names(self):
        cleaner = DatasetCleaner(self.df)
        cleaner.clean_column_names()
        self.assertIn('name', cleaner.df.columns)
        self.assertIn('age', cleaner.df.columns)

    def test_drop_missing(self):
        cleaner = DatasetCleaner(self.df)
        cleaned_df = cleaner.drop_missing(threshold=0.4).df
        self.assertNotIn('income', cleaned_df.columns)

    def test_fill_missing_mean(self):
        cleaner = DatasetCleaner(self.df)
        cleaner.fill_missing(strategy='mean')
        self.assertFalse(cleaner.df['age'].isnull().any())

    def test_remove_duplicates(self):
        cleaner = DatasetCleaner(self.df)
        before = len(cleaner.df)
        cleaner.remove_duplicates()
        after = len(cleaner.df)
        self.assertLess(after, before)

    def test_get_cleaned(self):
        cleaner = DatasetCleaner(self.df)
        result = cleaner.clean_column_names().remove_duplicates().get_cleaned()
        self.assertIsInstance(result, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()
