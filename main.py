import simplecrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
with open("passwords.txt", "r") as p:
    while True:
        try:
            pasw = p.readline().strip()
            if not pasw:
                break
            res = simplecrypt.decrypt(pasw, encrypted).decode('utf8')
            print(pasw)
            print(res)
        except simplecrypt.DecryptionException:
            pass