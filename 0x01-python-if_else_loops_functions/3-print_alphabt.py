#!/usr/bin/python3
# Author - Olaoluwa Dolapo
for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print(f"{chr(letter)}", end="")
