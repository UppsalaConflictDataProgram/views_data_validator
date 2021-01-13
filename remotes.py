"""
Remotes, functions that are also accessible over httpimports
"""

from typing import Any
import numpy as np

def summarize(dataframe: Any):
    """
    Summarization function, that outputs Meta given a df
    No imports to simplify remote import over httpimports
    Function is generally available
    """
    meta = {}

    indexarray = np.array(dataframe.index.to_list())
    meta["ishape"] = indexarray

    return {
            "index":{"sp":[1,2,3]},
            "column_names":["foo","bar"]
        }
