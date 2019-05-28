# Conver SVG to Page XML
With this tool you can convert svg coordinate files to page xml files

### Requirements
- conda

### Installation
```conda env create -f environment.yml```

### Usage
Activate the conda environment (```conda activate convert_svg_topage```)

And then you can start the method with the following command
```
python converter.py --input_folder /path/to/input/folder --output_folder /path/to/output/folder
```

The input folder is the folder containing the svg or svgs. The tool will just grep the svg files.
