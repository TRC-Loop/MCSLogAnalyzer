"""
 * author: AK
 * created on 09-06-2024-15h-02m
 * github: https://github.com/TRC-Loop
 * email: ak@stellar-code.com
 * copyright 2024
"""
from enum import Enum
from halo import Halo

class FileType(Enum):
    JSON = "json"
    MCS = "mcs"
    TEXT = "text"
    
LoadLog_spinner = Halo(text='Processing...', spinner='dots12')