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

