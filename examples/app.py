import argparse
import sys
import os

from ..image_pdf_tools import (
    image_to_pdf,
    pdf_merge
)

parser = argparse.ArgumentParser(description='Image and pdf tools')
parser.add_argument('-t','--type', type=str, choices=['pdf', 'image'],
        help='Image to pdf or Merge pdf', required=True)
parser.add_argument('-f', '--files', type=str, 
        help='Liste image or pdf', required=True, nargs='+')

args = vars(parser.parse_args())

def main():
    #image to pdf
    if args['type'].lower() == 'image':
        re = image_to_pdf(args['files'], './results')
        if not re:break
        print(f'converted image, look at {re}')
    elif args['type'].lower() == 'pdf':
        #merge pdf
        re = pdf_merge(args['files'], './results')
        if not re: return None
        print("All pdf merged !!!, look at result folder")
    else:
        print('The specified type does not valid')
        sys.exit()

if __name__ == "__main__":
    main()
    print('Enjoy !!!')
