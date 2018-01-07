import time
def getdict():
    dict1 = {}
    dict2 = {}
    key = 0
    for letters in 'abcdefghijklmnopqrstuvwxyz':
        dict1[letters] = key
        dict2[key] = letters
        key+=1
    return dict1,dict2

z,y = getdict()
def easycrypto(string, z,y):
    newstr = ""
    for letters in string:
        if z[letters] % 2 == 0:
            i = z[letters] + 1
            letters = y[i]
        else:
            i = z[letters] - 1
            letters = y[i]
        newstr += letters
    return newstr



def acronym(string):
    agencies = {}
    z = string.split(" ")
    acr = ""
    for strings in range(len(z)):
        if z[strings][0] == z[strings][0].upper():
            acr+=z[strings][0]
    agencies[acr] = string
    return agencies


def reversephonebook(dictionary):
    newdict = {}
    for keys in dictionary:
        value = dictionary[keys]
        newdict[value] = keys
    return newdict

def somedumbassshit():
    list = ["first", "second", "third"]
    str = []
    for string in list:
        z = input("What is the " + string + " word: ")
        str += z[0]
    if str == sorted(str[0]+str[1]+str[2]):
        return True

def somemoredumbassshit():
    list  = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    z = int(input("What month as an int pussy: "))
    print(list[z-1])
    time.sleep(1)
    print(" you stupid cunt")

def average():
    z = input("Type a sentence you big fat bitch: ")
    y = len(z)
    b = len(z.split(" "))
    return (y-b+1)/b



def fcopy(file1,file2):
    z = open(file1, 'r')
    y = open(file2, 'w')
    a = z.read()
    i =0
    y.write("I love andrea times 100 million\n")
    while i < 100000000:
        y.write("I love andrea " + str(i)+"\n")
        i+=1
    z.close()
    y.close()



def links(file):
    file = open(file, 'r')
    counter = 0
    for lines in file:
        if "</a>" in lines:
            counter +=1
    return counter

def stats(file):
    file = open(file, "r")
    line,word,character = 0,0,0
    for lines in file:
        line+=1
        list = lines.split(" ")
        str = ""
        for items in list:
            str += items
        word += len(list)
        character += len(str)
    print("line count {}".format(line))
    print("word count {}".format(word))
    print("character count {}".format(character))



def grades(files):
    file = open(files,"r")
    list = []
    for lines in file:
        list += lines.split(" ")
    list = sorted(list)
    list1,i, = [],0,
    for item in range(0,len(list)-1):
        if list[i] != list[item+1]:
            list1 += [list[i:item+1]]
            i =item+1
        if item == len(list)-2:
            list1 +=[list[i:len(list)]]
    for items in range(len(list1)):

        print(str(len(list1[items]))+ ' got a(n) ' + list1[items][0])

def ticker(file):
    z = open(file, 'r')
    dict = {}
    list =[]
    x=0
    for lines in z:
        list+=[lines]
    for items in range(len(list)-1):
        if x%2==0:
            dict[list[items]] = list[items+1]
        x+=1
    while(True):
        y = input('Enter Company Name: ')
        print(dict[y+'\n'])
#print(ticker('/Users/nicholaskreissler/Desktop/newfile.txt'))

def mirror(string):
    # abcdefghijklmnopqrstuvwxyz
    dict = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p', 'z': 's', 's': 'z'}
    str = ''
    for letters in string:
        if letters in dict:
            str += dict[letters]
        else:
            str += letters
    z = str[::-1]
    for letters in z:
        if letters in "acefghjkry":
            return "Invalid"
    return z

def scarydict(file,newfile):
    z = open(file,'r')
    str = ""
    for lines in z:
        for characters in lines:
            if characters not in '".,-!:;/][1234567890?\')(':
                if characters == '\n':
                    str += ' '
                else:
                    str += characters
    l = str.split(' ')
    l = sorted(l)
    newl = []
    prev = l[0]
    for index in range(1,len(l)):
        if l[index] != prev:
            newl += [l[index]]
            prev = l[index]
    newfile = open(newfile, 'w')
    for word in newl:
        if len(word) > 3:
            print(word)
            newfile.write(word + "\n")

def names():
    ret,list = True,[]
    while(ret):
        var = input("Enter name here: ")
        if var == '':
            ret = False
        else:
            list +=[var]
    dict = {}
    for items in list:
        if items in dict:
            dict[items]+=1
        else:
            dict[items] = 1
    for items in dict:
        if dict[items] == 1:
            x,y = 'student','is'
        else:
            x,y = 'students', 'are'
        print("There " + y + ' ' + str(dict[items]) + ' ' + x + ' named ' + items )


def different(list):
    dict = {}
    for lists in list:
        for items in lists:
            dict[items] = 'test'
    print(len(dict))
different([[1,0,3,4,5,6,1],[0,1,0]])

def abbreviation():
    list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    dict = {}
    for item in list:
        dict[item[0:2]] = item
    while(True):
        z = input("Enter day abbreviation: ")
        print(dict[z])



def index(filename,list):
    dict = {}
    for item in list:
        dict[item] = []
    for item in dict:
        x=0
        text = open(filename, 'r')
        for line in text:
            x+=1
            if item in line:
                dict[item] += [x]
    for item in dict:
        l = ''
        x = 0
        for numbers in dict[item]:
            x+=1
            if len(dict[item]) == x:
                l += str(numbers)
            else:
                l += str(numbers) + ', '
        print(item + '     ' + l)
#2. Problem 4.29 [stats()]
#3. Problem 4.27 [fcopy()]
#4. Problem 4.31 [duplicate()]
#5. Problem 4.30 [distribution()]
#6. Problem 4.32[ censor()]
def stats(file):
    file = open(file, 'r')
    lines, words, characters = 0,0,0
    for line in file:
        lines+=1
        for character in line:
            if character == " " or character == '\n':
                characters+=1
                if len(line) > 1:
                    words+=1
            else:
                characters+=1


    return lines, words, characters

print(stats('/Users/nicholaskreissler/Desktop/homework/example.txt'))

def fcopy(file,newfile):
    file = open(file, 'r')
    newfile = open(newfile, 'w')
    x = file.read()
    newfile.write(x)
    file.close()
    newfile.close()
fcopy('/Users/nicholaskreissler/Desktop/frankenstein.txt','/Users/nicholaskreissler/Desktop/newfile.txt')

def duplicate(file):
    file = open(file,'r')
    list = []
    for lines in file:
        list+= lines.split(' ')
    list = sorted(list)
    newl = []
    for items in list:
        if items in newl:
            file.close()
            return False
        else:
            newl += items
    file.close()
    return True
print(duplicate('/Users/nicholaskreissler/Desktop/homework/Duplicates.txt'))
print(duplicate('/Users/nicholaskreissler/Desktop/homework/noDuplicates.txt'))


# I couldnt think of a good way to sort them i have a loop im still working on but ran out of time
def distribution(file):
    file = open(file, 'r')
    l = []
    stri = ''
    for lines in file:
        for character in lines:
            if character != '\n':
                stri += character
        l += stri.split(' ')
    d = {}
    l = sorted(l)
    for items in l:
        if items not in d:
            d[items] = 1
        else:
            d[items] += 1
    if "A+" in d:
        print(str(d['A+']) + " students got an A+")
    if "A" in d:
        print(str(d['A']) + " students got an A")
    if "A-" in d:
        print(str(d['A-']) + " students got an A-")
    if "B+" in d:
        print(str(d['B+']) + " students got an B+")
    if "B" in d:
        print(str(d['B']) + " students got an B")
    if "B-" in d:
        print(str(d['B-']) + " students got an B-")
    if "C+" in d:
        print(str(d['C+']) + " students got an C+")
    if "C" in d:
        print(str(d['C']) + " students got an C")
    if "C-" in d:
        print(str(d['C-']) + " students got an C-")
    if "D+" in d:
        print(str(d['D+']) + " students got an D+")
    if "D" in d:
        print(str(d['D']) + " students got an D")
    if "D-" in d:
        print(str(d['D-']) + " students got an D-")
    if "F" in d:
        print(str(d['F']) + " students got an F")

distribution('/Users/nicholaskreissler/Desktop/homework/grades.txt')



def censored(file):
    file = open(file,'r')
    z = file.read()
    z = z.split(' ',)
    l = []
    for items in z:
        l += items.split('.')
    newtext = ''
    for item in l:
        if len(item) == 4:
            newtext += 'xxxx '
        elif item == '\n':
            newtext  = newtext[:-1]
            newtext+='.\n'
        else:
            newtext += item + ' '
    print(newtext)

censored('/Users/nicholaskreissler/Desktop/homework/example.txt')

def distanvebetweenMinandMax(list):
    """

    :param list: list
    :return: int
    """
    x,y,z,a = -1,-1,-1,-1
    for items in range(len(list)):
        if list[items] < x:
            x=y
            y+=1
        else:
            y+=1
        if list[items] > x:
            z=a
            a+=1
        else:
            a+=1
    return z-x
print(distanvebetweenMinandMax([1, -4, -7, 7, 8, 11]))

def numunique(list):
    """

    :param list: list
    :return: int
    """
    lists = []
    for items in list:
        if items not in lists:
            lists += [items]
    return len(lists)

print(numunique([11, 11, 11, 11, 22, 33, 44, 44, 44, 44, 44, 55, 55, 66, 77, 88, 88]))

def removeduplicates(list):
    """

    :param list: list
    :return: list
    """
    list1 = []
    for items in list:
        if items not in list1:
            list1 += [items]
    return list1

print(removeduplicates([11, 11, 11, 11, 22, 33, 44, 44, 44, 44,
44, 55, 55, 66, 77, 88, 88]))

def create2D(x,y):
    """

    :param x: int
    :param y: int
    :return: list(list)
    """
    list =[]
    for item in range(x):
        columns = []
        for items in range(y):
            z= item*items
            columns +=[z]
        list+=[columns]
    return list
print(c)
def index(s):
    return s[2:5], s[7:9], s[1:8], s[0:4], s[7:10]
print(index('0123456789'))

def string(s):
    return s.count('day'), s.find('sunny'), s.replace('sunny','cloudy')
print(string('it will be a sunny day today'))

def name(last,first,middle):
    return last+"\t"+first+'\t'+middle+'\t'
print(name('Smith','John','Paul'))

def even(int):
    x = ''
    for i in range(1,int+1):
        if i % 2 == 0 or i % 3 ==0:
            x += str(i)+', '
    return x
print(even(17))

def postcard(first,last,street,number,city,state,zipcode):
    print('{} {}'.format(first,last))
    print('{} {}'.format(number, street))
    print('{}, {} {}'.format(city,state,zipcode))
postcard('John','Doe','Main Street','123','Anycity','AS','09876')

def roster(students):
    print("Last    First    Class   Average Grade")
    for student in students:
        print('{:10}{:10}{:10}{:8.2f}'.format(student[0],
                                              student[1],student[2],student[3]))

def stringcount(file, string):
    file = open(file, 'r')
    s = 0
    for line in file:
        s += line.count(string)
    return s
print(stringcount('/Users/nicholaskreissler/Desktop/homework/example.txt', 'line'))

def words(file):
    file = open(file, 'r')
    x = []
    for line in file:
        x += line.split(' ')
    newl = []
    for item in x:
        news = ''
        for character in item:
            if character not in '\n,.?!':
                news += character.lower()
        if len(news) >= 1:
            newl+=[news]
    return newl
print(words('/Users/nicholaskreissler/Desktop/homework/example.txt'))

def mygrep(file,string):
    file = open(file,"r")
    l = ''
    for line in file:
        if string in line:
            l +=line
    return l
print(mygrep('/Users/nicholaskreissler/Desktop/homework/example.txt', 'line'))


def sumall():
    number = 0
    while(True):
        y = float(input("Type numbers to add them:"))
        if y != 0:
            number += y
        else:
            return number

def inboth(list1,list2):
    list,x,y = [],0,-1
    while(True):
        if x < len(list1):
            x+=1
            y+=1
            if list1[y] in list2:
                list+=[list1[y]]
        else:
            break
    return list

def concat(list1,list2):
    list3,x,y = [],0,-1
    while(True):
        x+=1
        y+=1
        list3+=[list1[y]]
        if x == len(list1):
            x,y = 0,-1
            while(True):
                x+=1
                y+=1
                list3 +=[list2[y]]
                if x == len(list2):
                    return list3

def geometric(list):
    x,ret = -1,True
    while(x+1 <len(list)):
        x+=1
        if x < len(list)-1:
            if list[x]*2 == list[x+1]:
                ret = True
            else:
                ret = False
                break



    return ret

def fib(integer):
    x,list = 1,[1,1,2]
    while(True):
        x+=1
        if integer > len(list)-1:
            list += [list[x] + list[x-1]]
            if integer == len(list)-1:
                return list[integer]
        else:
            return list[integer]

def mystery(integer):
    x,y = integer,-1
    while(x >= 1):
        y+=1
        x/=2
    return(y)

def exclamation(string):
    x,string1 = -1,''
    while(True):
        x+=1
        string1 += string[x]
        if string[x] in 'aeiou':
            string1 += string[x]*3
        if len(string) == x+1:
            string1 += string[x]
            return string1

def factorial(n):
    res= 1
    for i in range(2,n+1):
        res*=i
    return res

def approxe(integer):
    e1,e2,i,error = [1/factorial(0)],[1/factorial(0)+1/factorial(1)],0, integer
    while(sum(e2) - sum(e1) > error):
        i+= 1
        e1 = e2
        e2 = e2 + [1/factorial(i)]
    return sum(e2)

def approxPi(err):
    'err:float, return:float'
    pi = 4
    prev = 0
    cnt = 1
    while True:
        if abs(pi-prev) < err:
            break
        prev = pi
        if cnt %2 == 1:
            pi -= 4/(1+(2*cnt))
        else:
            pi += 4/(1+(2*cnt))
        cnt+=1
    return pi

def heron(n,error):
    'n: int, error:float, return:float'
    prev= 1
    while True:
        curr = 0.5 * (prev+n/prev)
        if abs(curr-prev) <= error:
            return curr
        prev = curr

def cipher(enc, s):
    'enc:string, s: string, return:string'
    acc = ''
    for i in s:
        acc+=enc[int(i)]
    return acc

import string
#6.1
def birthstate(string):
    dictionary = {'Barrack Hussein Obama II':'Hawaii'}
    return dictionary[string]
#print(birthstate('Barrack Hussein Obama II'))

#6.2
def rlookup(rphonebook):
    while(True):
        z = input("Enter phone number in the format (xxx)xxx-xx-xx: ")
        if z in rphonebook:
            print(tuple(rphonebook[z]))
        else:
            print("The number you entered is not in use")

#rlookup({'(123)456-78-90': ['Anna','Karenina']})

#6.5

def lookup(phonebook):
    while(True):
        z = input('Enter the first name:')
        y = input('Enter the last name:')
        new = tuple([z]) + tuple([y])
        if new in phonebook:
            print(phonebook[new])

#lookup({('Anna','Kerenina'): '(123)456-78-90'})

#6.6
def sync(phonebook):
    lis = []
    for items in phonebook:
        lis += list(items)
    s = set(lis)
phonebook1 = {'123-45-67-89','890-12-34-56'}
phonebook2 = {'123-45-67-89','45-453453453'}
phonebook3 = {'45-453453453','12345123412'}
phonebook4 = [phonebook1,phonebook2,phonebook3]
sync(phonebook4)

#6.11

def getdict():
    dict1 = {}
    dict2 = {}
    key = 0
    for letters in 'abcdefghijklmnopqrstuvwxyz':
        dict1[letters] = key
        dict2[key] = letters
        key+=1
    return dict1,dict2


z,y = getdict()
def easycrypto(string, z,y):
    newstr = ""
    for letters in string:
        if z[letters] % 2 == 0:
            i = z[letters] + 1
            letters = y[i]
        else:
            i = z[letters] - 1
            letters = y[i]
        newstr += letters
    return newstr

#6.12

def letter2number(string):
    x= 4.0
    dic ={}
    for letter in 'ABCDF':
        dic[letter+'+'] = x + .3
        dic[letter] = x
        dic[letter+'-'] = x - .3
        x += -1
    return dic[string]
print(letter2number('A+'))

#6.13

agencies = {'CCC':'Civilian Conservarion Corps', 'FCC':'Federal Communications Commission', 'FDIC':'Federal Deposit Insurande Corporation',

                                                                                               'SSB':'Social Security Board','WPA':'Works Progress Administration'}
acronyms = agencies.keys()
agencies['SEC'] = 'Sevurities and Exchange Comission'
agencies['SSB'] = 'Social Security Administration'
agencies.pop('CCC')
agencies.pop('WPA')
print(agencies)
print(acronyms)

#6.14
# in 6.13


#6.15
def newlookup(phonebook):
    while(True):
        z = input('Enter the first name:')
        y = input('Enter the last name:')
        new = (z, y)
        if new in phonebook:
            print(phonebook[new])
#newlookup({('Anna','Kerenina'): ['(123)456-78-90','1235452345']})

# 6.20

def reversephonebook(dictionary):
    newdict = {}
    for keys in dictionary:
        value = dictionary[keys]
        newdict[value] = keys
    return newdict
print(reversephonebook({'anna':'4234'}))
#6.21

def ticker(file):
    z = open(file, 'r')
    dict = {}
    x=0
    line = z.readlines()
    for i in range(len(line)-1):
        if x % 2 == 0:
            dict[line[i].strip()]= line[i+1].strip()
        x+=1
    while(True):
        z = input('Enter company name: ')
        print(dict[z]+'\n')

#ticker('/Users/nicholaskreissler/Desktop/nasdaq.txt')
#6.22
def mirror(string):
    # abcdefghijklmnopqrstuvwxyz
    dict = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p', 'z': 's', 's': 'z'}
    str = ''
    for letters in string:
        if letters in dict:
            str += dict[letters]
        else:
            str += letters
    z = str[::-1]
    for letters in z:
        if letters in "acefghjkry":
            return "Invalid"
    return z
print(mirror('bed'))
print(mirror('wood'))
#6.23

def scaryDict(file_name, file):
    file_obj = open(file_name)
    lines = file_obj.readlines()
    file_obj.close()
    punctuation = string.punctuation
    new_content = ''
    for line in lines:
        for ch in line:
            if ch in punctuation or ch in '\n' or ch in '1234567890':
                new_content += ' '
            else:
                new_content += ch
    output_file_obj = open(file, 'w')
    for word in sorted(list(set(new_content.split(' ')))):
        if len(word) > 2:
            output_file_obj.write(word + '\n')
    output_file_obj.close()


scaryDict('/Users/nicholaskreissler/Desktop/frankenstein.txt', '/Users/nicholaskreissler/Desktop/test.txt')

#6.36
def dictalphabet():
    dic1 ={}
    dic2 = {}
    x= 0
    for item in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        dic1[item] = x
        dic2[x] = item

        x +=1
    return dic1,dic2


def caeser(int, file,file1):
    z = open(file, 'r')

    news = ""
    for lines in z:
        news += encrypt(int, lines)
    a = open(file1, 'w')
    a.write(news)
    z.close()
    a.close()


def encrypt(int, lines):
    dic1,dic2 = dictalphabet()
    s = ""
    for character in lines:
        if character.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            z = dic1[character.upper()] + int
            if z > 25:
                z = z- 26
            if character.lower() == character:
                s += dic2[z].lower()
            else:
                s += dic2[z]
        else:
            s+= character
    return s

def removeacross(list):
    for item in list[2]:
        if item in list[1]:
            list[2].remove(item)
    return list

removeacross([[1,2],[1,3],[1,4]])

def index(s):
    return s[2:5], s[7:9], s[1:8], s[0:4], s[7:10]
print(index('0123456789'))

def string(s):
    return s.count('day'), s.find('sunny'), s.replace('sunny','cloudy')
print(string('it will be a sunny day today'))

def name(last,first,middle):
    return last+"\t"+first+'\t'+middle+'\t'
print(name('Smith','John','Paul'))

def even(int):
    x = ''
    for i in range(1,int+1):
        if i % 2 == 0 or i % 3 ==0:
            x += str(i)+', '
    return x
print(even(17))

def postcard(first,last,street,number,city,state,zipcode):
    print('{} {}'.format(first,last))
    print('{} {}'.format(number, street))
    print('{}, {} {}'.format(city,state,zipcode))
postcard('John','Doe','Main Street','123','Anycity','AS','09876')

def roster(students):
    print("Last    First    Class   Average Grade")
    for student in students:
        print('{:10}{:10}{:10}{:8.2f}'.format(student[0],
                                              student[1],student[2],student[3]))

def stringcount(file, string):
    file = open(file, 'r')
    s = 0
    for line in file:
        s += line.count(string)
    return s

def words(file):
    file = open(file, 'r')
    x = []
    for line in file:
        x += line.split(' ')
    newl = []
    for item in x:
        news = ''
        for character in item:
            if character not in '\n,.?!':
                news += character.lower()
        if len(news) >= 1:
            newl+=[news]
    return newl

def mygrep(file,string):
    file = open(file,"r")
    l = ''
    for line in file:
        if string in line:
            l +=line
    return l

def string():
    z = input('Enter a sentence: ')
    d = {}
    z = z.lower()
    for item in z:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1

    for items in sorted(d):
        print(items + str(d[items]))
    return d


try:
   f = open("my_file.tt", "w")
   try:
      f.write("Writing some data to the file")
   finally:
      f.close()
except IOError:
   print("Error: my_file.txt does not exist or it can't be opened for output.")

def func(set):
    s = ''
    for items in set:
        s += str(items) + ', '
    return s

def networks(int, list1):
    d = {}
    for i in list1:
        d[i] = list(i)
    l = []
    for items in d:
        l+=[d[items]]
    newl = []
    x=0
    for items in range(len(l)-1):
        for things in l[items]:
            if things in l[items+1]:
                newl += [l[items]+l[items+1]]
            elif things not in l[items+1] and x%2 != 0:
                newl +=[l[items+1]]
            x+=1
    for items in range(len(newl)):
        print('Social Network ' +  str(items) + ' is ' + func(set(newl[items])))

networks(10,[(0,1),(1,2),(3,4),(4,5)])


import time
def network(i,j):
    x = (makedic(i,j))
    l = engine(x)
    for i in range(len(l)):
        print('Network ' + str(i) + " is " + str(l[i]))
def engine(x):
    res =[]
    while True:
        l = []
        i = 0
        if i > len(x)-1:
            return res
        y = list(x.keys())[i]
        l+=x[y] + [y]
        while i != len(x.keys())-1:
            if x[y] in l or y in l:
                l+= x[y]
                i+=1
                y = list(x.keys())[i]
            else:
                i+=1
                y = list(x.keys())[i]
        for d in l:
            if d in x:
                del x[d]
        if len(l) > 1:
            res += [set(l)]
def makedic(i,j):
    dictionary = {}
    for integer in range(i):
        dictionary[integer]= []
        for lists in j:
            if integer in lists:
                for items in lists:
                    if items != integer:
                        dictionary[integer] += [items]
    return dictionary

network(500,[(0,1),(2,1,4,56),(3,4),(4,5),(5,6),(7,8),(8,9),(10,11)])

import string
#6.1
def birthstate(string):
    dictionary = {'Barrack Hussein Obama II':'Hawaii'}
    return dictionary[string]
#print(birthstate('Barrack Hussein Obama II'))

#6.2
def rlookup(rphonebook):
    while(True):
        z = input("Enter phone number in the format (xxx)xxx-xx-xx: ")
        if z in rphonebook:
            print(tuple(rphonebook[z]))
        else:
            print("The number you entered is not in use")

#rlookup({'(123)456-78-90': ['Anna','Karenina']})

#6.5

def lookup(phonebook):
    while(True):
        z = input('Enter the first name:')
        y = input('Enter the last name:')
        new = tuple([z]) + tuple([y])
        if new in phonebook:
            print(phonebook[new])

#lookup({('Anna','Kerenina'): '(123)456-78-90'})

#6.6
def sync(phonebook):
    lis = []
    for items in phonebook:
        lis += list(items)
    s = set(lis)
phonebook1 = {'123-45-67-89','890-12-34-56'}
phonebook2 = {'123-45-67-89','45-453453453'}
phonebook3 = {'45-453453453','12345123412'}
phonebook4 = [phonebook1,phonebook2,phonebook3]
sync(phonebook4)

#6.11

def getdict():
    dict1 = {}
    dict2 = {}
    key = 0
    for letters in 'abcdefghijklmnopqrstuvwxyz':
        dict1[letters] = key
        dict2[key] = letters
        key+=1
    return dict1,dict2


z,y = getdict()
def easycrypto(string, z,y):
    newstr = ""
    for letters in string:
        if z[letters] % 2 == 0:
            i = z[letters] + 1
            letters = y[i]
        else:
            i = z[letters] - 1
            letters = y[i]
        newstr += letters
    return newstr

#6.12

def letter2number(string):
    x= 4.0
    dic ={}
    for letter in 'ABCDF':
        dic[letter+'+'] = x + .3
        dic[letter] = x
        dic[letter+'-'] = x - .3
        x += -1
    return dic[string]
print(letter2number('A+'))

#6.13

agencies = {'CCC':'Civilian Conservarion Corps', 'FCC':'Federal Communications Commission', 'FDIC':'Federal Deposit Insurande Corporation',

                                                                                               'SSB':'Social Security Board','WPA':'Works Progress Administration'}
acronyms = agencies.keys()
agencies['SEC'] = 'Sevurities and Exchange Comission'
agencies['SSB'] = 'Social Security Administration'
agencies.pop('CCC')
agencies.pop('WPA')
print(agencies)
print(acronyms)

#6.14
# in 6.13


#6.15
def newlookup(phonebook):
    while(True):
        z = input('Enter the first name:')
        y = input('Enter the last name:')
        new = (z, y)
        if new in phonebook:
            print(phonebook[new])
#newlookup({('Anna','Kerenina'): ['(123)456-78-90','1235452345']})

# 6.20

def reversephonebook(dictionary):
    newdict = {}
    for keys in dictionary:
        value = dictionary[keys]
        newdict[value] = keys
    return newdict
print(reversephonebook({'anna':'4234'}))
#6.21

def ticker(file):
    z = open(file, 'r')
    dict = {}
    x=0
    line = z.readlines()
    for i in range(len(line)-1):
        if x % 2 == 0:
            dict[line[i].strip()]= line[i+1].strip()
        x+=1
    while(True):
        z = input('Enter company name: ')
        print(dict[z]+'\n')

#ticker('/Users/nicholaskreissler/Desktop/nasdaq.txt')
#6.22
def mirror(string):
    # abcdefghijklmnopqrstuvwxyz
    dict = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p', 'z': 's', 's': 'z'}
    str = ''
    for letters in string:
        if letters in dict:
            str += dict[letters]
        else:
            str += letters
    z = str[::-1]
    for letters in z:
        if letters in "acefghjkry":
            return "Invalid"
    return z
print(mirror('bed'))
print(mirror('wood'))
#6.23

def scaryDict(file_name, file):
    file_obj = open(file_name)
    lines = file_obj.readlines()
    file_obj.close()
    punctuation = string.punctuation
    new_content = ''
    for line in lines:
        for ch in line:
            if ch in punctuation or ch in '\n' or ch in '1234567890':
                new_content += ' '
            else:
                new_content += ch
    output_file_obj = open(file, 'w')
    for word in sorted(list(set(new_content.split(' ')))):
        if len(word) > 2:
            output_file_obj.write(word + '\n')
    output_file_obj.close()


scaryDict('/Users/nicholaskreissler/Desktop/frankenstein.txt', '/Users/nicholaskreissler/Desktop/test.txt')

#6.36
def dictalphabet():
    dic1 ={}
    dic2 = {}
    x= 0
    for item in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        dic1[item] = x
        dic2[x] = item

        x +=1
    return dic1,dic2


def caeser(int, file,file1):
    z = open(file, 'r')

    news = ""
    for lines in z:
        news += encrypt(int, lines)
    a = open(file1, 'w')
    a.write(news)
    z.close()
    a.close()


def encrypt(int, lines):
    dic1,dic2 = dictalphabet()
    s = ""
    for character in lines:
        if character.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            z = dic1[character.upper()] + int
            if z > 25:
                z = z- 26
            if character.lower() == character:
                s += dic2[z].lower()
            else:
                s += dic2[z]
        else:
            s+= character
    return s

import random
import time

import string
from itertools import chain


def craps(int):
    d = {0: [2, 3, 12], 1: [7, 11]}
    res = {0: 0, 1: 0}
    while (sum(res.values()) != int):
        y = random.randrange(1, 7)
        z = random.randrange(1, 7)
        initial = y+z
        if initial in d[0]:
            res[0] += 1
        elif initial in d[1]:
            res[1] += 1
        else:
            while (True):
                x = 0
                y = random.randrange(1,7)
                z = random.randrange(1,7)
                x = y+z
                if x == 7:
                    res[0]+=1
                    break
                elif x == initial:
                    res[1]+=1
    print(res)
    return (res[1]/int)


def manhatten(int,inte):
    l = getgrid(int,inte)

    x=0
    y_position = 0
    x_position = 0
    l1 = ['y_position', 'x_position']
    l2= [1,-1]
    while(x < 10000):
        x+=1
        y = random.choice(l1)
        z = random.choice(l2)
        if y == 'y_position':
            if y_position == 0 and z == -1:
                y_position = int-1
                l[y_position][x_position]+=1
            elif y_position == int-1 and z == 1:
                y_position = 0
                l[y_position][x_position] = 1
            else:
                y_position += z
                l[y_position][x_position] = 1
        if y == 'x_position':
            if x_position == 0 and z == -1:
                x_position = inte - 1
                l[y_position][x_position]=1
            elif x_position == inte - 1 and z == 1:
                x_position = 0
                l[y_position][x_position] = 1
            else:
                x_position += z
                l[y_position][x_position] = 1
    for i in l:
        print('{}'.format(l[i]))
    print('\n')



def getgrid(x,y):
    l = {}
    for i in range(x):
        l[i] = []
        for z in range(y):
            l[i] += [0]

    return l

manhatten(200,500)

def diceprob(int):
    l = 0
    z = 0
    while l != 200:
        x = random.randrange(1,7)
        y = random.randrange(1,7)
        if x+y==int:
            l+=1
            z+=1
        else:
            z+=1
    print('It took {0} rolls to get {1} rolls of {2}'.format(z,l,int))

def war(p):
    k=0
    n=0
    while k != p:
        k+=1
        ld = getcards()
        dict = makedict(ld)
        player1, player2,  = getcardsforplayers(ld)
        n = engine(player1,player2,dict,k,n)

def makedict(listod):
    dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: []}
    for i in listod:
        for key in i:
            dict[key] += [i[key]]
    return dict

def engine(player1,player2,dict,k,n):
    l = list(chain.from_iterable(player1.values()))
    l1 = list(chain.from_iterable(player2.values()))
    while(len(l) != 0 and len(l1) != 0):
        card = random.choice(l)
        card1 = random.choice(l1)
        key = getkeys(card, dict)
        key1 = getkeys1(card1, dict)
        if key > key1:
            l.append(card1)
            l1.remove(card1)
        elif key1 > key:
            l1.append(card)
            l.remove(card)
        elif key == key1:
            l.remove(card)
            l1.remove(card1)
            newl = [card,card1]
            while (True):
                i,g = getlength(l,l1)
                sample = random.sample(l,i)
                sample1 = random.sample(l1,g)
                if len(sample) != 0:
                    c = random.choice(sample)
                else:
                    for i in newl:
                        l1.append(i)
                    loop = 0
                    break

                if len(sample1) != 0:
                    c1 = random.choice(sample1)
                else:
                    for i in newl:
                        l.append(i)
                    loop = 0
                    break
                key = getkeys(c, dict)
                key1 = getkeys1(c1,dict)
                if key > key1:
                    for i in sample1:
                        l.append(i)
                    for i in newl:
                        l.append(i)
                    if len(l1) == 0 or len(l) == 0:
                        loop = 0
                        break
                    l1 = remove1(l1,sample1)

                    break
                if key < key1:
                    for i in sample:
                        l1.append(i)
                    for i in newl:
                        l1.append(i)
                    if len(l) == 0 or len(l1) == 0:
                        loop = 0
                        break
                    l = remove1(l,sample)
                    break

    t,n = getwinner(l,l1,n)
    #print("Player 1 has {} cards and player2 has {}, {} wins".format(len(l),len(l1),t))
    print("Player 1 has won {}% of the games".format((n/k)*100))
    return n
def remove1(list,list1):
    for items in list1:
        list.remove(items)
    return list


def getwinner(l,l1,n):
    if len(l) == 52:
        n += 1
        return 'Player 1',n
    else:

        return 'Player 2',n

def getlength(l,l1):
    if len(l) > 3:
        i = 3
    else:
        i = len(l)
    if len(l1) > 3:
        g = 3
    else:
        g = len(l1)
    return i,g


def getkeys(card,fulldictionary):
    key = -1
    for keys in fulldictionary:
        for items in fulldictionary[keys]:
            if items == card:
                key = keys
    return key


def getkeys1(card1,fulldictionary):
    key1 = -1
    for keys in fulldictionary:
        for items in fulldictionary[keys]:
            if items == card1:
                key1 = keys
    return key1



def getcards():
    l1 =[]
    l = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    x=0
    while(x!=4):
        d = {}
        for i in range(len(l)):
            if x == 0:
                d[i]=str(l[i])+' of Diamonds'
            if x == 1:
                d[i]=str(l[i])+' of Clubs'
            if x == 2:
                d[i]=str(l[i])+' of Hearts'
            if x == 3:
                d[i]=str(l[i])+' of Spades'
        x+=1
        l1+=[d]
    return l1


def getcardsforplayers(x):
    player1 = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: []}
    player2 = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: []}
    while len(list(chain.from_iterable(player1.values()))) != 26:
        b = random.choice(range(len(x)))
        z = random.choice(list(x[b].keys()))
        player1[z] += [x[b][z]]
        del x[b][z]
        if len(x[b])==0:
            del x[b]
    while len(list(chain.from_iterable(player2.values()))) != 26:
        b = random.choice(range(len(x)))
        z = random.choice(list(x[b].keys()))
        player2[z] += [x[b][z]]
        del x[b][z]
        if len(x[b])==0:
            del x[b]
    return player1,player2,
#war(20000)

def game(i):
    b=0
    x=0
    while(x != i):
        x+=1
        z = random.randrange(1,10)
        y = random.randrange(1,10)
        print('{} + {} = '.format(z,y))
        a = int(input('Enter Answer: '))
        if y+z==a:
            print('Correct')
            b+=1
        else:
            print('Incorrect')
    print('You got {} out of {} answers correct!'.format(b,i))

#game(5)


def zipf(file):
    file = open(file,'r')
    punctuation = string.punctuation
    s =''
    for lines in file:
        for characters in lines:
            if characters not in punctuation and characters not in '\n':
                s += characters.lower()
            else:
                s += ' '
    new = s.split(' ')
    print(new)
    new = list(filter(None, new))
    print(new)

    newset = list(set(new))
    #l = []
    #for items in newset:
      #  l += [(new.count(items), items)]
    #print(sorted(l))
    d={}
    for items in new:
        if items in d:
            d[items] += 1
        else:
            d[items] = 0
    new = []
    length = 0
    for keys in d:
        new += [(d[keys],keys)]
        length += d[keys]
    g = (sorted(new, reverse = True))
    for i in range(0,10):
        print(str(((g[i][0]/length ) *(i+1)) )+ " "+(g[i][1]))




zipf('/Users/nicholaskreissler/Desktop/frankenstein.txt')








def reverse(d):
    s = {}
    for keys in d:
        if d[keys] in s:
            s[d[keys]] += [keys]
        else:
            s[d[keys]] = [keys]
    print(s)


d = {0:1,1:1,2:3,3:4}
reverse(d)

def dic2lis(lis):
    for i in range(len(lis)):

def inboth(list1, list2):
    "list1:list(int),list2:list(int),return:list3:list(int)"
    list3 = []
    for i in list1:
        if i in list2:
            list3.append(i)
    return list3

def inboth1(list1, list2):
    "list1:list(int),list2:list(int),return:list3:list(int)"
    list3 = []
    for index in range(len(list1)):
        if list1[index] in list2:
            list3.append(list1[index])

def concat(list1, list2):
    "list1:list(int),list2:list(int),return:list3:list(int)"
    list3 = []
    for i in list1:
        list3.append(i)
    for l in list2:
        list3.append(l)
    return list3

def concat1(list1, list2):
    "list1:list(int),list2:list(int),return:list3:list(int)"
    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i])
    for l in range(len(list2)):
        list3.append(list2[l])

concat1([3, 4], [4, 5])

def reverse(list):
    "list:list(int),return:list1:list(int)"
    list1 = []
    for item in list:
        list1[0:0] += [item]
    return list1

def reverse1(list):
    list1 = []
    for i in range(len(list)):
        x = len(list) - i - 1
        list1.append(list[x])
    return list1

reverse1([3, 5])

def reverse2d(list):
    x = 3
    list1 = [[], [], []]
    for lists in list:
        x -= 1
        for number in lists:
            list1[x][0:0] += [number]
    print(list1)

reverse2d([[1, 2], [3], [4, 5, 6]])

def multlist(l1, l2):
    c = 0
    x = -1
    for a in l1:
        x += 1
        c += a * l2[x]

    print(c)

def multlist1(l1, l2):
    c = 0
    for a in range(len(l1)):
        c += l1[a] * l2[a]
    print(c)

multlist1([1, 2, 3], [4, 5, 6])

def reverse2d1(list):
    list2 = [[],[],[]]
    x=3
    for i in range(len(list)):
        x-=1
        for j in range(len(list[i])):
            list2[x][0:0] += [list[i][j]]
    if len(list2[0]) == 0:
        del list2[0]
    print(list2)
reverse2d1([[1,2],[4,5,6]])

import turtle as g
colors = (['black','orange','red','blue','green','yellow'])

for i in range(45):

    g.color(colors[i%6])
    g.fd(2*i*5)
    g.right(45)
    g.pensize(i)
def fl(file):
    x =0
    file = open(file, 'w+')
    s = ''
    while x < 1000000:
        if x % 2 == 0:
            s+='f'
        else:
            s+='j'
        x+=1
    file.write(s)
    file.close()
fl('/Users/nicholaskreissler/Desktop/fjj.txt')
elevatorposition = 32

def buttonup(elevatorposition):
    call = [[],[[],[],[],[]]]
    call[1][0] = input("What floors are the elevator being called by:")
    call = listol(call)
    print(call)
    elevengine(call)
def listol(call):
    if "," in call[1][0]:
        call = [[],[sorted(list(map(int, call[1][0].split(",")))), [], [], []]]

    else:
        call = [[],[list(map(int, call.split[1][0](" "))), [], [], []]]
    return call



def elevengine(call):
    i,j=0,0
    while(j < len(call[1][0])):
        if i < len(call[1][2])-1 and call[1][2][i] < call[1][0][j]:
            #do some function
            i+=1
        else:
            #do some function
            j+=1
    print(j)
    print(i)

def concatenate(arg1, arg2):
    """ concatenates 2 dimenssional list of length4 with 2 dimensional
    list of length 4

    :param arg1: list(list)
    :param arg2: list(list)
    :return: List(list)
    """
    for item in arg2[1][0]:
        arg1[1][0] += [item]
    for item in arg2[1][1]:
        arg1[1][1] += [item]
    for item in arg2[1][2]:
        arg1[1][2] += [item]
    for item in arg2[1][3]:
        arg1[1][3] += [item]
    return arg1
#list = [[number],[[initialcalls],[callsbelowbottomup],[callsinbetweeninitials],[callsafterinitials]]]
buttonup(elevatorposition)

def sumall():
    number = 0
    while(True):
        y = float(input("Type numbers to add them:"))
        if y != 0:
            number += y
        else:
            return number

def inboth(list1,list2):
    list,x,y = [],0,-1
    while(True):
        if x < len(list1):
            x+=1
            y+=1
            if list1[y] in list2:
                list+=[list1[y]]
        else:
            break
    return list

def concat(list1,list2):
    list3,x,y = [],0,-1
    while(True):
        x+=1
        y+=1
        list3+=[list1[y]]
        if x == len(list1):
            x,y = 0,-1
            while(True):
                x+=1
                y+=1
                list3 +=[list2[y]]
                if x == len(list2):
                    return list3

def geometric(list):
    x,ret = -1,True
    while(x+1 <len(list)):
        x+=1
        if x < len(list)-1:
            if list[x]*2 == list[x+1]:
                ret = True
            else:
                ret = False
                break



    return ret

def fib(integer):
    x,list = 1,[1,1,2]
    while(True):
        x+=1
        if integer > len(list)-1:
            list += [list[x] + list[x-1]]
            if integer == len(list)-1:
                return list[integer]
        else:
            return list[integer]

def mystery(integer):
    x,y = integer,-1
    while(x >= 1):
        y+=1
        x/=2
    return(y)

def exclamation(string):
    x,string1 = -1,''
    while(True):
        x+=1
        string1 += string[x]
        if string[x] in 'aeiou':
            string1 += string[x]*3
        if len(string) == x+1:
            string1 += string[x]
            return string1

def factorial(n):
    res= 1
    for i in range(2,n+1):
        res*=i
    return res

def approxe(integer):
    e1,e2,i,error = [1/factorial(0)],[1/factorial(0)+1/factorial(1)],0, integer
    while(sum(e2) - sum(e1) > error):
        i+= 1
        e1 = e2
        e2 = e2 + [1/factorial(i)]
    return sum(e2)

def approxPi(err):
    'err:float, return:float'
    pi = 4
    prev = 0
    cnt = 1
    while True:
        if abs(pi-prev) < err:
            break
        prev = pi
        if cnt %2 == 1:
            pi -= 4/(1+(2*cnt))
        else:
            pi += 4/(1+(2*cnt))
        cnt+=1
    return pi

def heron(n,error):
    'n: int, error:float, return:float'
    prev= 1
    while True:
        curr = 0.5 * (prev+n/prev)
        if abs(curr-prev) <= error:
            return curr
        prev = curr

def cipher(enc, s):
    'enc:string, s: string, return:string'
    acc = ''
    for i in s:
        acc+=enc[int(i)]
    return acc

def distanvebetweenMinandMax(list):
    """

    :param list: list
    :return: int
    """
    x,y,z,a = -1,-1,-1,-1
    for items in range(len(list)):
        if list[items] < x:
            x=y
            y+=1
        else:
            y+=1
        if list[items] > x:
            z=a
            a+=1
        else:
            a+=1
    return z-x
print(distanvebetweenMinandMax([1, -4, -7, 7, 8, 11]))

def numunique(list):
    """

    :param list: list
    :return: int
    """
    lists = []
    for items in list:
        if items not in lists:
            lists += [items]
    return len(lists)

print(numunique([11, 11, 11, 11, 22, 33, 44, 44, 44, 44, 44, 55, 55, 66, 77, 88, 88]))

def removeduplicates(list):
    """

    :param list: list
    :return: list
    """
    list1 = []
    for items in list:
        if items not in list1:
            list1 += [items]
    return list1

print(removeduplicates([11, 11, 11, 11, 22, 33, 44, 44, 44, 44,
44, 55, 55, 66, 77, 88, 88]))

def create2D(x,y):
    """

    :param x: int
    :param y: int
    :return: list(list)
    """
    list =[]
    for item in range(x):
        columns = []
        for items in range(y):
            z= item*items
            columns +=[z]
        list+=[columns]
    return list
print(create2D(5000,3))