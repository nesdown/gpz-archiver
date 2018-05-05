import hexler
import numbers

hex_code = hexler.hexlify('7-zip32.dll', 'out.hex')

hex_string = str(hex_code)[2:]
print(hex_string)

hex_list = list(hex_string)
coded_list = []
counter = 0

for i in range(0, len(hex_list) - 2):
    if hex_list[i] == hex_list[i + 1]:
        counter += 1
        # i += 1
    else:
        if counter != 0:
            if str(hex_list[i]) in '0123456789':
                coded_list.append('#')
                coded_list.append(str(counter + 1))
                coded_list.append('#')
            else:
                coded_list.append(str(counter + 1))
            coded_list.append(hex_list[i])
            counter = 0
        else:
            coded_list.append(hex_list[i])

print(''.join(coded_list))
with open(input('Enter the archive name: ') + '.gpz', 'w') as f:
    f.write(''.join(coded_list))
