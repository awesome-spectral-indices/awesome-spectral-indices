from datetime import date
from typing import List, Optional, Union
from pydantic import BaseModel, HttpUrl, validator
from py_expression_eval import Parser, Expression

class SpectralIndex(BaseModel):
    short_name: str
    long_name: str
    formula: str
    reference: HttpUrl
    type: str
    date_of_addition: date
    contributor: HttpUrl
        
    @validator('short_name')
    def check_short_name(cls, v):
        assert ' ' not in v, 'short_name must not contain spaces.'
        return v
    
    @validator('formula')
    def check_formula(cls, v):
        parser = Parser()
        expression = parser.parse(v)
        variables = expression.variables()
        bands = ['A','B','G','R','N','RE1','RE2','RE3','RE4','S1','S2','T1','T2','g','L','C1','C2','kNN','kNR','kNB','kNL','kGG','kGR','kGB']
        assert isinstance(expression,Expression), 'Invalid formula.'
        assert all(elem in bands for elem in variables), 'Invalid variables for formula, please check the supported variables.'
        return v
    
    @validator('contributor')
    def check_contributor(cls, v):        
        assert v.host == 'github.com', 'contributor is not a GitHub url.'
        return v
    
    @validator('type')
    def check_type(cls, v):        
        assert v in ["vegetation","water","burn","snow","drought","kernel"], 'type must be one of ["vegetation","water","burn","snow","drought","kernel"].'
        return v