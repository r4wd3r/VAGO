#!/usr/bin/env python

import sys
import argparse

'''Ejemplo del parser a implementar'''
def main():
    print "---------"
    print "Vago 1.0"
    print "----------\n"

    parser = argparse.ArgumentParser(
        description="Vamos a vagar...")
    parser.add_argument("input_file", help='File to process', type=str)
    parser.add_argument('-o', '--output', help='Prefix name for output files.', type=str, default="output")

    args = parser.parse_args()

    filename = args.input_file
    output = args.output

main()