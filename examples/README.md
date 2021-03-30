# pathus_script
Image to pdf and pdf merged python

# Setup local
```sh
	git clone https://github.com/hadpro24/pathus_script.git
   cd pathus_script
```

# Create env and Install dependencies
```sh
python3 -m venv env && source env/bin/activate
pip install -r requirements.txt
```

# How to use
```sh
python app.py -h
######
usage: app.py [-h] -t {pdf,image} -f FILES [FILES ...]

Image and pdf tools

optional arguments:
  -h, --help            show this help message and exit
  -t {pdf,image}, --type {pdf,image}
                        Image to pdf or Merge pdf
  -f FILES [FILES ...], --files FILES [FILES ...]
                        Liste image or pdf

```

# Convert image to pdf
```sh
python app.py -t image -f image_path.png
```

# Merge pdf
```sh
python app.py -t pdf -f pdf_path1.png pdf_path2.png pdf_path3.png
```

# You can convert many image
```sh
python app.py -t image -f image_path1.png image_path2.png
```


# Credit
Harouna Diallo