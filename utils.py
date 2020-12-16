import csv


def load_input(path):

    data = []

    with open(path) as file:
        rows = csv.reader(file, delimiter=',')
        
        for i, r in enumerate(rows):
            if i == 0:
                if 'Col' not in r[0]: raise Exception('Please check input format.')
                header = r
            else:
                try:
                    data.append([max(int(s), 0) for s in r if len(s) > 0])
                except Exception as e:
                    print('Error reading input file:')
                    raise e
    
    # check input array format
    lengths = [len(r) for r in [header] + data]
    
    if not all([a == b for a, b in zip(lengths[:-1], lengths[1:])]): raise Exception('Please check input format.')
    return header, data


def write_output(path, header, result):
    with open(path, 'w') as outfile:
        for sublist in [header] + result:
            outfile.write('{}\n'.format(','.join([str(v) for v in sublist])))


def get_fib(indices): 

    v0, v1 = 0, 1
    outputs = {}
    i = 0

    cap = max(indices)
    if cap >= 10000:
        print('Warning: {}th number in Fibonacci number is huge and take long to calculate!'.format(cap))

    while i <= cap:
        if i > 1:
            v0, v1 = v1, v0 + v1
        
        if i in indices:
            if i == 0:
                outputs.update({i: v0})
            else:
                outputs.update({i: v1})

        i += 1
    
    return outputs