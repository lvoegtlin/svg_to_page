import argparse
import os
import sys
import xml.etree.ElementTree as ET
from tqdm import tqdm

from utils.XMLhandler import writePAGEfile


def convert(input_path, output_folder):
    if not os.path.exists(input_path):
        sys.exit(1)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    all_files = []
    # get all svg files
    for root, _, files in os.walk(input_path):
        all_files.extend(files)

    all_files = filter(lambda x: '.svg' in x, all_files)

    for file in tqdm(all_files):
        coords_string = parse_file_and_convert(input_path, file)
        file_name, _ = os.path.splitext(file)
        writePAGEfile(os.path.join(output_folder, file_name + '.xml'), coords_string)


def parse_file_and_convert(input_path, file_name):
    # parse tree
    with open(os.path.join(input_path, file_name), mode='r') as file:
        root = ET.fromstring(file.read())

    coordinates_string_list = []

    # viewbox 0,0 start check else add the offset
    for child in root:
        coordinates = child.attrib['d']
        coor_string = ''
        prev_number = False
        for elm in coordinates.split():
            if elm.isalpha():
                coor_string += ' '
            else:
                if prev_number:
                    coor_string += str(int(float(elm)))
                else:
                    coor_string += str(int(float(elm))) + ','

                prev_number = not prev_number

        coordinates_string_list.append(coor_string.strip())
    return coordinates_string_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--input_folder', type=str, required=True,
                        help='Input path to the svg folder')
    parser.add_argument('--output_folder', type=str, required=True,
                        help='Output path to the newly created xml files')

    args = parser.parse_args()
    convert(args.input_folder, args.output_folder)
