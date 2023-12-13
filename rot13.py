#!/usr/bin/env python3

# WEEK EIGHT PORTFOLIO

if __name__ == '__main__':

    def rot13(phrase):
        abc = 'abcdefghijklmnopqrstuvwxyz'
        out_phrase = ''

        for char in phrase:
            out_phrase += abc[(abc.find(char)+13)%26]
        return out_phrase

phrase = input('Enter phrase to encrypt: ')
print(rot13(phrase))
print(rot13(rot13(phrase)))



age = 10 + 20
age = age + 5
print(age)

print("the age value is", age)

result = 20

x= 10
type(x)
print(x)

name = "Ryan_Hardman"
print (name)

name = 'Hello, is your name "Bwian"?'
print (name)

name = "Hello, is your name 'Bwian'?"
print (name)

print ("this is a string containing a backslash (\) \na single quote ('),\n" 'a double quote (")\nand is split across multiple lines')

print ("""this is a string containing a backslash (\),\na single quote ('),\na double quote (")\nand is split across multiple lines""")

total = 100
print("the total is", total)
total = total + 99
print("the total is now", total)

total = 100
total += 99
print("the total is now", total)

total -= 1
print("the total is", total)

total *= 4
print("the total is", total)

total /= 2
print("the total is", total)

print(type(False))
print(type(1000))
print(type(100.11))
print(type("Hello"))
print(type(True))
print(type(100 / 5))
print(type(100 // 5))

print(10+10)
print("10"+"10")
print("ABC"*10)
