# EXERCICI 11 Que rebrà 3 paràmetres, “diccionari”, “ordre” i “key”.
def order_dict_by_key(diccionario, orden, key=""):
    unkw_order = False
    dict_w_no_key = False
    key_w_no_dict = False
    unkw_key = False
    diff_type = False
    try:
        list_ans = []
        if orden not in ("asc", "des"):
            unkw_order = True
            raise TypeError

        elif key == "":
            for i in list(diccionario.keys()):
                if type(diccionario[i]) == dict:
                    dict_w_no_key = True
                    raise TypeError
                else:
                    list_ans.append(i)
            for j in range(len(list_ans)):
                for k in range(len(list_ans)-1):
                    if type(diccionario[list_ans[k]]) != type(diccionario[list_ans[k+1]]):
                        diff_type = True
                        raise TypeError
                    else:
                        if orden == "des":
                            if diccionario[list_ans[k]] < diccionario[list_ans[k+1]]:
                                list_ans[k], list_ans[k+1] = list_ans[k+1], list_ans[k]
                        if orden == "asc":
                            if diccionario[list_ans[k]] > diccionario[list_ans[k + 1]]:
                                list_ans[k], list_ans[k+1] = list_ans[k+1], list_ans[k]
            return list_ans

        elif key != "":
            for i in list(diccionario.keys()):
                if type(diccionario[i]) != dict:
                    key_w_no_dict = True
                    raise TypeError
                elif key not in list(diccionario[i].keys()):
                    unkw_key = True
                    raise TypeError
                else:
                    list_ans.append(i)

            for j in range(len(list_ans)):
                for k in range(len(list_ans)-1):
                    if type(diccionario[list_ans[k]][key]) != type(diccionario[list_ans[k+1]][key]):
                        diff_type = True
                        raise TypeError
                    else:
                        if orden == "des":
                            if diccionario[list_ans[k]][key] < diccionario[list_ans[k + 1]][key]:
                                list_ans[k], list_ans[k + 1] = list_ans[k + 1], list_ans[k]
                        if orden == "asc":
                            if diccionario[list_ans[k]][key] > diccionario[list_ans[k + 1]][key]:
                                list_ans[k], list_ans[k + 1] = list_ans[k + 1], list_ans[k]
            return list_ans

    except TypeError:
        if unkw_order:
            print("ERROR | 'orden' parameter only allows 'asc' or 'des' as values.")
        elif dict_w_no_key:
            print("ERROR | If you are dealing with other dictionaries as values, you have to specifie a 'key'.")
        elif key_w_no_dict:
            print("ERROR | You can only give a parameter to 'key' when the dicionary's values are other dictionaries.")
        elif unkw_key:
            print("ERROR | Given key is not valid.")
        elif diff_type:
            print("ERROR | Can't compare values with different types.")
        return ""

