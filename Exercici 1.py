# EXERCICI 1: Aquesta funció ens prepara un menú en mode text.
def getOpt(textOpts, inputOptText, rangeList, dictionary, exceptions):
    print(textOpts)
    new_dict = []
    new_except = []
    if len(list(dictionary.keys())) != 0:

        for i in list(dictionary.keys()):
            new_dict.append(str(i))

    if len(exceptions) != 0:

        for i in exceptions:
            new_except.append(str(i))

    while True:
        opt = input(inputOptText)
        if opt in list(map(str, rangeList)):
            return int(opt)

        elif opt in new_dict:
            return list(dictionary.keys())[new_dict.index(opt)]

        elif opt in new_except:
            return exceptions[new_except.index(opt)]
        else:
            input("ERROR | Non-valid option, press any key to continue")


# print(type(getOpt("\n1)Login\n2)Create user\n3)Show Adventures\n4)Exit", "\nElige tu opción:",
# [1,2,3,4], {"@":2, "123": "dd"}, ["w","e",-1])))
