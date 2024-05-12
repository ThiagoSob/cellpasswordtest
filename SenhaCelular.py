print("-----"*10)

print("\n\nINFINITY PHONES\n\n")

print("-----"*10)

print("\n\nHELLO!\nLET'S START SETUP OF YOUR PHONE!\n\n")

print("-----"*10)

print("\n\nMake a password for accesses your new Phone:\n\n")

s = input("Password: ")
sr = input("Repeat Password: ")

print("\n\n")

print("-----"*10)

print("\n\n")

while(s != sr):
    print("The Repeat Password is different of the Password, please try again:")
    sr = input("Repeat Password: ")

print("\n\n")

print("-----"*10)

print("\n\n")

print("INITIALIZING YOUR PHONE!")

print("\n\n")

print("PASSWORD")
p = input()

print("\n\n")

print("-----"*10)

print("\n\n")

if(p == s):
    print("CORRECT PASSWORD!\nWELCOME!")
else:
    print("WRONG PASSWORD!\nFIRST TIME\nTRY AGAIN\nYOU HAVE MORE 2 TIMES!")
    print("\n\n")
    print("-----"*10)
    print("\n\n")
    print("PASSWORD")
    p = input()
    print("\n\n")
    print("-----"*10)
    print("\n\n")
    if(p == s):
        print("CORRECT PASSWORD!\nWELCOME!")
    else:
        print("WRONG PASSWORD!\nSECOND TIME!\nTRY AGAIN\nYOU HAVE ONLY ONE MORE TIME!")
        print("\n\n")
        print("-----"*10)
        print("\n\n")
        print("PASSWORD")
        p = input()
        print("\n\n")
        print("-----"*10)
        print("\n\n")
        if(p == s):
            print("CORRECT PASSWORD!\nWELCOME!")
        else:
            print("WORNG PASSWORD!\nYOU ARE BLOCK!")

print("\n\n")

print("-----"*10)
        

