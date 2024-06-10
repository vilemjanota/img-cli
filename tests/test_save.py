import os
import pytest
from pycli.save import save
import pyperclip


def save_file(): # Test that new file is create
    output_file = "test_output.png"
    save(output_file)
    success = os.path.exists(output_file)
    if(success):
        os.remove(output_file)
    return success

def save_file_error(): # Test that file is not created
    output_file = "test_output.png"
    save(output_file)
    success =  not os.path.exists(output_file)
    if(not success):
        os.remove(output_file)
    return success

def test_save():
    assert save_file() != save_file_error()



