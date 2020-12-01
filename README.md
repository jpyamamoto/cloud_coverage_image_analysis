# Cloud Coverage Detection

Detect the index of cloud coverage from an image, given by the total amount of pixels in the image divided by the number of cloud pixels.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the package.

```bash
pip install -r requirements.txt
```

## Tests

The project runs with Python 3. If the default version is Python 2, use the command `python3` instead.

```bash
python -m pytest
```

## Usage

```bash
./main.py <image_path> [s|S]

# Examples
./main.py ../images/image1.JPG
./main.py ../images/image1.JPG S
```

## Generate Documentation

After having the requirements installed, execute the following command:

```bash
cd docs/

# To generate the documentation in HTML format
make html

# To generate the documentation in LaTeX format
make html
```

Generated docs will be located in `docs/build/`.

## License
[MIT](LICENSE)
