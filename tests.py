"""
Tests for validation service
Tests validation functions, and exported summarization function
"""
import unittest
import pandas as pd

from remotes import summarize
from app import validate

class TestFunctions(unittest.TestCase):
    """
    Tests for functions...
    """

    def test_summarization(self):
        """
        Summarization test
        """
        data = pd.DataFrame([
                "a",1
            ])

        meta = summarize(data)
        print(meta)
        valid = validate(meta)
        print(valid)

        self.assertTrue(valid)
