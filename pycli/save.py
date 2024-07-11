import os

def save(output_file, height, width):
    """
    Save an image from the clipboard to a file.

    Args:
        output_file (str): The name of the output file.

    Returns:
        None
    """
    print("saving to", output_file + "...")
    os.system(f"xclip -selection clipboard -target image/png -out > ./{output_file} 2>error.txt")
    if (os.path.exists('error.txt') and os.path.getsize('error.txt') > 0):
        with open('error.txt', 'r') as file:
            error_message = file.read()
        print("Error occurred:", error_message)
        os.remove(output_file)
        #os.remove('error.txt')
        return
    if(height != 'original' and width != 'original'):
        os.system(f"convert {output_file} -resize {width}x{height} {output_file}")
    elif(height != 'original'):
        os.system(f"convert {output_file} -resize x{height} {output_file}")
    elif(width != 'original'):
        os.system(f"convert {output_file} -resize {width}x {output_file}")