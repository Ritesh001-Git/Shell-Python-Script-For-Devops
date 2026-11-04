with open("a1.txt","r") as src:
    with open("a2.txt","x") as dest:
        dest.write(src.read())