#!/usr/bin/python3
# Author - Olaoluwa Dolapo

i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print(f"{chr(c - i)}", end="")
    i = 32 if i == 0 else 0
