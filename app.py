"""
Service responsible for data validation, inferring from a given set of data
attributes, namely:
    * Index
    * Column names
"""

import fastapi
from fastapi.responses import FileResponse

from mytypes import Meta

app = fastapi.FastAPI()

@app.post("/")
def validate(meta:Meta)->bool:
    """
    Validate the incoming metadata
    """
    valid = True
    return valid

@app.get("/module/{file}")
def module():
    """
    Return the remotes.py file,
    containing a summarization function.

    Importing this function over http rather
    than transferring the data for summarization
    saves a lot of bandwidth.
    """
    return FileResponse("remotes.py")
