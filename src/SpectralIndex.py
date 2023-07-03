import re
import orjson

from py_expression_eval import Parser, Expression
from pydantic import BaseModel, validator
from src.utils import Bands, IndexType
from datetime import date
from typing import Optional, List


def orjson_dumps(value, *, default):
    """
    orjson.dumps returns bytes, to match standard json.dumps we need to decode
    """
    return orjson.dumps(value, default=default).decode()


class SpectralIndex(BaseModel):
    """
    Python dataclass for Spectral Indices
    """
    contributor: str
    short_name: str
    reference: str
    long_name: str
    formula: str
    bands: Optional[List] = None
    platforms: Optional[List] = None
    application_domain: str
    date_of_addition: date
    
    
    class Config:
        extra = "forbid"
        json_loads = orjson.loads
        json_dumps = orjson_dumps
        
    @validator("short_name")
    def check_short_name(cls, value):
        if re.search(r"\s+", value):
            raise ValueError("short_name must not contain spaces.")
        return value
    
    @validator('formula')
    def check_formula(cls, value):
        parser = Parser()
        expression = parser.parse(value)
        variables = expression.variables()  # obtain band names (e.g. ["R", "G"])

        # check Expression
        if not isinstance(expression, Expression):
            raise ValueError("Invalid formula.")
        
        # check if the variables are in "Bands".
        if not all(elem in Bands._value2member_map_ for elem in variables):
            band_names = ", ".join(Bands._value2member_map_.keys())
            raise ValueError(
                "Invalid variables in formula. SpectralIndex only supports the following variables: " +
                band_names
            )
        
        return value
                
    @validator('contributor')
    def check_contributor(cls, value):
        # regex to detect emails or github profiles.
        email_regex = r"^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"
        github_regex = r"(?:https?://)?(?:www[.])?github[.]com/[\w-]+/?"
        full_regex = "%s|%s" % (email_regex, github_regex)
        # Check if it is a correct email address or GitHub profile.
        if not  re.match(full_regex, value):
            raise ValueError("contributor is neither a GitHub profile nor an email.")
        return value
    
    @validator('application_domain')
    def check_type(cls, value):
        # Obtain names of IndexType enum.
        IndexTypeNames = ", ".join(IndexType._value2member_map_.keys())
        
        # Check if IndexTtpe is supported.
        if not value in IndexType._value2member_map_:
            raise ValueError(
                "Invalid IndexType. SpectralIndex only supports the following IndexType: " +
                IndexTypeNames
            )        
        return value