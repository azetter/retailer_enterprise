path = '/home/hameed/Documents/Github/retailer_enterprise/Ham/datasets/Products/product_type.txt'
outpath = '/home/hameed/Documents/Github/retailer_enterprise/Ham/datasets/Products/NEW_product_type.txt'

_output = open(outpath,'w')
with open(path) as x:
    for line in x:
        newline = "'" + line[:-1] + "'\n"
        _output.write(newline)
        print(newline)
        if 'str' in line:
            break

_output.close()
