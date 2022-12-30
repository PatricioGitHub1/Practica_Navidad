# from les_meves_funcions import dades
# print("hello world")
# print("DSADSAD")
# dict = {"esew":2, 23: 2}
# print(type("0.9"))
# print(len(dict))
# print("-1".isnumeric())
# dictio = {1:2, "ds":12, "dasds":"d"}
# for i in dictio:
#     print(i)
# llista = [12, 23, 2, 21, 51, 9]
# for i in range(len(llista)):
#     for j in range(len(llista)-1):
#         if llista[j] < llista[j+1]:
#             llista[j + 1], llista[j] = llista[j], llista[j + 1]
#
# print(llista)
# print(list(dades.dict_articulos.values()))
# for i in list(dades.dict_articulos.values()):
#     print(type(i))
orden = "des"
diccionario = {3: 5, 4: 4, 1: 5, 2: 2}
list_ans = [3, 4, 1, 2]
for j in range(len(list_ans)):
    for k in range(len(list_ans) - 1):
        if orden == "des":
            if diccionario[list_ans[k]] < diccionario[list_ans[k + 1]]:
                list_ans[k], list_ans[k + 1] = list_ans[k + 1], list_ans[k]
print(list_ans)