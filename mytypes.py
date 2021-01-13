"""
Types related to dataset validation
"""
from typing import List,Dict
from pydantic import BaseModel

class Meta(BaseModel):
    """
    Metadata, gleamed from a Pandas data frame, essentially a sufficient
    representation for validation of a pandas.DataFrame
    """
    index: Dict[str,List[int]]
    column_names: List[str]
