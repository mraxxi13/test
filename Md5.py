import hashlib

key1 = "23eeeb4347bdd26bfc6b7ee9a3b755dd"
key2 = "202cb962ac59075b964b07152d234b70"
key3 = "78f825aaa0103319aaa1a30bf4fe3ada"
key4 = "3daa9b9a0cd29195de716a044c73783f"

def sa():
        u1 = input("username")
        u2 = (hashlib.md5(u1.encode('utf-8')).hexdigest())
        if u2 == key1:
            return
        else:
            print("salah username")
            ii = input("Untuk login kembali, ketikkan Y ")
            if ii == "Y":
                return sa()
            elif ii == "y":
                return sa()
            else:
                quit()

sa()

def sasa():
    p1 = input("password")
    p2 = (hashlib.md5(p1.encode('utf-8')).hexdigest())
    if p2 == key2:
        return
    else:
        print("Salah password")
        i = input("Untuk memasukkan password kembali, ketikkan Y ")
        if i == "Y":
            return sa()
        elif i == "y":
            return sa()
        else:
            quit()
sasa()

def md():
    mdhash = input("masukkan string")
    print("md5 anda: " + hashlib.md5(mdhash.encode('utf-8')).hexdigest())

md()

