filenames = ["1.dox", "2.doc", "3.dop"]

filenames = [name.replace(".", "-") + ".txt" for name in filenames]

print(filenames)