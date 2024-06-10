# img-cli

`img-cli` is a command-line tool for saving images from the clipboard to a file.

## Installation

To install `img-cli`, you can run the following command:

```sh
pip3 install -e .
```

## Usage
To use img-cli, you can use the following command:
```sh
img-cli save <filename>
```
This will save an image from the clipboard to the specified file. If the clipboard does not contain an image, an error message will be printed.

## Testing

Tests for img-cli are located in the tests directory. You can run them using pytest:

```sh
pytest
```