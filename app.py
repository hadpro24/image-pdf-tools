import argparse
import sys
import os

from utils import (
    image_to_pdf,
    pdf_merge
)

parser = argparse.ArgumentParser(description='Image and pdf tools')
parser.add_argument('-t','--type', type=str, choices=['pdf', 'image'],
        help='Image to pdf or Merge pdf', required=True)
parser.add_argument('-f', '--files', type=str, 
        help='Liste image or pdf', required=True, nargs='+')

args = vars(parser.parse_args())

def is_file_exist(path):
    if not os.path.isfile(path): 
        print(f'ERROR : The path specified does not exist')
        sys.exit()

def main():
    #image to pdf
    if args['type'].lower() == 'image':
        if len(args['type']) == 1:
            files = list(args['files'])
        else:
            files = args['files']
        for f in files:
            is_file_exist(f)
            #conver all image
            re = image_to_pdf(f)
            print(f'converted image, look at {re}')
    elif args['type'].lower() == 'pdf':
        for f in args['files']:
            is_file_exist(f)
        #merge pdf
        pdf_merge(args['files'])
        print("All pdf merged !!!, look at result folder")
    else:
        print('The specified type does not valid')
        sys.exit()

if __name__ == "__main__":
    main()
    print('Enjoy !!!')
