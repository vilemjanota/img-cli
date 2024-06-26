import os

def save(output_file):
    """
    Save an image from the clipboard to a file.

    Args:
        output_file (str): The name of the output file.

    Returns:
        None
    """
    print("saving to", output_file + "...")
    if(os.system(f"xclip -selection clipboard -target image/png -out > ./{output_file} 2>/dev/null")!=0):
        print("Clipboard does not contain an image")
        os.remove(output_file)