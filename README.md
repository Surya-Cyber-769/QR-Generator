# QR-Generator

A simple and fast QR Code Generator that creates QR codes for text, URLs, and data using an easy-to-use interface.

Features
- Generate PNG and SVG QR codes
- Configurable error-correction and size
- CLI and Python API examples
- Batch generation (CSV) and basic customization

Installation

```bash
# Install from PyPI (when published)
pip install qr-generator

# Or install editable from source
git clone https://github.com/Surya-Cyber-769/QR-Generator.git
cd QR-Generator
pip install -e .
```

Quick examples

Python API:
```python
from qr_generator import make_qr

# Create a PNG file
img_path = make_qr("https://example.com", output="example.png", scale=10)

# Create an SVG
svg_path = make_qr("Hello world", output="hello.svg", fmt="svg")
```

CLI:
```bash
# generate a PNG
python -m qr_generator.cli "https://example.com" --output qrcode.png --scale 8
```

Development
- Run tests: `pytest`
- Format: `black .`
- Lint: `ruff .`

Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md)

License
This project is available under the MIT License. See LICENSE for details.
