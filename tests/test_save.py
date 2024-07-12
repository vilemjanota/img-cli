import os
import pytest
from pycli.save import save


def save_file(): #image in clipboard test
    os.system("xclip -selection clipboard -t image/png < tests/img.png")
    output_file = "test_output.png"
    save(output_file, 'original', 'original')
    success = os.path.exists(output_file)
    if(success):
        os.remove(output_file)
    return success

def test_save():
    assert save_file()




