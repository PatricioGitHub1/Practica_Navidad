def order_list(llista, ordre="des"):
    unkw_order = False
    try:
        if type(llista) != list:
            raise ValueError

        for i in range(len(llista)-1):
            if type(llista[i]) != type(llista[i+1]):
                raise TypeError

        if ordre not in ("des", "asc"):
            unkw_order = True
            raise TypeError

        if ordre == "asc":
            for i in range(len(llista)):
                for j in range(len(llista) - 1):
                    if llista[j] > llista[j + 1]:
                        llista[j + 1], llista[j] = llista[j], llista[j + 1]
            return llista

        else:
            for i in range(len(llista)):
                for j in range(len(llista) - 1):
                    if llista[j] < llista[j + 1]:
                        llista[j + 1], llista[j] = llista[j], llista[j + 1]
            return llista

    except ValueError:
        print("ERROR | 'Llista' parameter has to be a list")
    except TypeError:
        if unkw_order:
            print("ERROR | 'order' parameter only allows 'asc' or 'des' as values. ")
        else:
            print("ERROR | The list elements have to be all the same type")


print(order_list([12, 2, 56, 6, 2, -1], "asc"))
