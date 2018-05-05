import binascii


def hexlify(filename, out):
    with open(filename, 'rb') as f:
        content = f.read()
    with open(out, 'w') as o:
        o.write(str(content))

    print('Done!')
    # print(binascii.hexlify(content))

    return binascii.hexlify(content)
