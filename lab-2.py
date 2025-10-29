import random
from csv import reader
from csv import DictReader
import xml.dom.minidom as minidom
#1 задание
# with open('books-en.csv') as f:
#     s = csv.reader(f, delimiter=';')
#     head = next(s)
#     s = list(s)
#
# answ = len(list(filter(lambda x: len(x[1]) > 30, s)))
# print(answ)

#4157

#2 задание

'''with open('books-en.csv', "r") as csvfile:
    table = list(DictReader(csvfile, delimiter=';'))

def find_string(name):
    books = []
    c = 0
    for row in table:
        try:
            money = int(row['Price'])
            author_name = row['Book-Author'].lower()

            if (name in author_name) and  money>=200:
                c += 1
                books.append(f"{row['Book-Title']}, {money}")

        except:
            pass
    if c == 0:
        print('Ничего не найдено')
    else:
        print('\n'.join(books))

while True:
    author = input('Введите имя автора: ')
    if author in ['', 0]:
        break
    else:
        find_string(author)
        '''
'задание 3'

# answ = []
# with open('books-en.csv') as f:
#     s = list(DictReader(f, delimiter=';'))
#     for _ in range(20):
#         row = random.choice(s)
#         answ.append(row)
# f = open('task3.txt', 'w', encoding='utf-8')
# for index, el in enumerate(answ, start=1):
#     f.write(f"{index}{el['Book-Author']}. {el['Book-Title']} - {el['Year-Of-Publication']}")
#     f.write('\n')
# f.close()

'4 задание'

# xml_file=open('currency.xml', 'r')
# xml_data=xml_file.read()
#
# dom=minidom.parseString(xml_data)
# dom.normalize()
#
# elements1=dom.getElementsByTagName('NumCode')
# elements2=dom.getElementsByTagName('CharCode')
# numcode=[]
# CharCode=[]
#
# def beg(elements,massive):
#     for node in elements:
#
#         for child in node.childNodes:
#             if child.nodeType==3:
#                 massive.append(child.data)
#
#             if node.getAttribute('ID')=='R01010':
#                 print(node.getElementsByTagName('NumCode')[0].firstchild.data)
#     return massive
#
# print(beg(elements1,numcode))
# print(beg(elements2,CharCode))
#
# xml_file.close()

#допзадание
with open('books-en.csv') as f:
    table = list(DictReader(f, delimiter=';'))
publishers=set()
popular=[]
for row in table:
    popular.append([int(row['Downloads']),row['Book-Title']])
    publishers.add(row['Publisher'])
popular=sorted(popular,key=lambda x: -x[0])
for num,book in enumerate(popular[:20],start=1):
    print(num,*book)

#print(publishers)