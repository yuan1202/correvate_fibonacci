import os, sys
import argparse
import itertools

from utils import load_input, write_output, get_fib


parser = argparse.ArgumentParser(description='fibonacci runner')
parser.add_argument('-i', '--input', help='input file full path', default='./input/example.csv')
parser.add_argument('-o', '--output', help='output file full path', default='./output.csv')
args = parser.parse_args()


if __name__ == '__main__':
    
    # check arguments
    assert os.path.exists(args.input), 'Input file cannot be found.'

    # load data
    header, indices = load_input(args.input)
    
    # get unique indices for single run
    unique = sorted(set(itertools.chain(*indices)))
    
    # run fibonacci calculation
    results = get_fib(unique)
    
    # make output
    output_array = []
    for r in indices:
        output_row = []
        for idx in r:
            output_row.append(results[idx])
        output_array.append(output_row)
    
    # write result
    write_output(args.output, header, output_array)