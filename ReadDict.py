
# read 'dict/test', return a list
def readList():
    list = []
    with open('dict/test', 'r') as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            list.append(line)
    return list

# print the list
def printList(list):
    for i in list:
        #print(i)
        print(i + '.' + 'xyz')


if __name__ == '__main__':
    list = readList()
    printList(list)

