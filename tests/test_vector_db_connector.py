# tests/test_vector_db_connector.py

import unittest
import numpy as np
import os
from devtoolbox.vector_db_connector import VectorDBConnector

class TestVectorDBConnector(unittest.TestCase):
    def setUp(self):
        self.dim = 128
        self.db_path = "test_vector_db.index"
        self.meta_path = "test_vector_meta.pkl"
        self.vectors = np.random.rand(10, self.dim).astype('float32')
        self.metadata = [f"Item {i}" for i in range(10)]

        self.connector = VectorDBConnector(
            dim=self.dim,
            db_path=self.db_path,
            metadata_path=self.meta_path
        )
        self.connector.add_vectors(self.vectors, self.metadata)

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        if os.path.exists(self.meta_path):
            os.remove(self.meta_path)

    def test_search_returns_expected_results(self):
        query = self.vectors[0]
        results = self.connector.search(query, top_k=3)
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)
        self.assertIn("score", results[0])
        self.assertIn("meta", results[0])

    def test_vector_dimension_mismatch(self):
        bad_query = np.random.rand(64).astype('float32')  # wrong dimension
        with self.assertRaises(ValueError):
            self.connector.search(bad_query)

if __name__ == '__main__':
    unittest.main()
