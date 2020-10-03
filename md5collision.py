from hashlib import md5
from itertools import combinations_with_replacement
import string

startingbytes = '0e'

for i in range(1,25):  #MD5 collisions starts from here loop work

    ps = combinations_with_replacement(string.digits, i) 
    for p in ps:
        to_hash = start + ''.join(p)

        m=md5()
        m.update(to_hash.encode('utf-8'))
        then_hash = m.hexdigest()

        if then_hash[:2] == start and then_hash[2:].isnumeric():  #it checks for collision of MD5 string
            print("COLLISON HASHES")
            print(f"{to_hash} -> {then_hash}")
            exit()
