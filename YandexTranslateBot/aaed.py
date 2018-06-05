matrix = ''
def set_matrix(message):
    global matrix
    matrix = message
    matrix = matrix.split(';')
    print(type(matrix))
    buf = matrix
    matrix = list()
    for i in buf:
        i = i.replace('[','')
        i = i.replace(']', '')
        i = i.split(',')
        matrix.append(i)
    print(matrix)
a = '''[1,2,3];[3,2,1];[4,5,6]'''

set_matrix(a)
#print(matrix)