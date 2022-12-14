from hashlib import sha3_512
from itertools import product

hash1 = "8932856f406e80b3e7770543c4cea1be541b513784bf14d6f57eed73b75f5da0546c74290902472342a1223840aa7fd92ff1db9a93d3b25d65219c2cf36d8307"
hash2 = "eaf23bef2a0744d6889f71526a30e3fd97dbb325e49e7c9b736b38219c67066d1d7878af61a10eea056afa5eb76ca842da9606b28762badf2fdeea081b0f9495"

found = False
pass_length = 0
alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()+'


while not found:
    pass_length += 1
    combinations = product(alph, repeat=pass_length)
    for comb in combinations:
        password = ''.join(comb)
        print(password)
        if sha3_512(password.encode("utf-8")).hexdigest() == hash1:
            print("pass: " + password)
            found = True
            break