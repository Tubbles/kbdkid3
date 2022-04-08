#!/bin/env python3

import argparse
import copy
import ezdxf
from shutil import copy as file_copy
import os


def main():
    parser = argparse.ArgumentParser(description='Separate the layers from a DXF file into new DXF files')
    parser.add_argument(
        '--output-dir', help='The output directory to place the output files. Defaults to the same directory as the input file')
    parser.add_argument('dxf_file', help='The DXF file to read')

    args = parser.parse_args()

    original = ezdxf.readfile(args.dxf_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Separate the layers from a DXF file into new DXF files')
    parser.add_argument(
        '--output-dir', help='The output directory to place the output files. Defaults to the same directory as the input file')
    parser.add_argument('dxf_file', help='The DXF file to read')

    args = parser.parse_args()
    dxf_file = args.dxf_file
    dxf_file_name = os.path.basename(args.dxf_file)

    output_dir = os.path.dirname(os.path.realpath(args.dxf_file))
    if args.output_dir:
        output_dir = os.path.realpath(args.output_dir)

    original = ezdxf.readfile(dxf_file)
    layer_names = [l.dxf.name.lower() for l in list(original.layers)]
    del original

    for layer in layer_names:
        new_file = os.path.join(output_dir, f'{os.path.basename(os.path.splitext(args.dxf_file)[0])}_{layer}.dxf')
        file_copy(dxf_file, new_file)

        doc = ezdxf.readfile(new_file)
        doc.audit()

        keep_layers = ['0', layer]
        msp = doc.modelspace()
        delete_entities = [entity for entity in msp if entity.dxf.layer.lower() not in keep_layers]

        for entity in delete_entities:
            msp.unlink_entity(entity)

        doc.save()
        print(f'Generated: {new_file}')
