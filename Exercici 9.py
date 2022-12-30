# EXERCICI 9: Exercici 9
# Crearem una funció amb el nom print_item(id,**values). Que rebrà un id d’article i
# opcionalment una sèrie de paràmetres del tipus clau=valor.


def print_item(id, **values):
    id_error = False
    try:
        if id not in list(dades.dict_articulos.keys()):
            id_error = True
            raise ValueError

        if len(values) != 0:
            for i in list(values.keys()):
                if i not in list(dades.dict_articulos[id].keys()):
                    raise ValueError

        print("ID".ljust(10) + str(id).rjust(40))
        for i in dades.dict_articulos[id]:
            if i in values:
                print(i.ljust(10) + str(values[i]).rjust(40))
            else:
                print(i.ljust(10) + str(dades.dict_articulos[id][i]).rjust(40))

    except ValueError:
        if id_error:
            print("ERROR | ID not from an existing article")
        else:
            print("ERROR | One of the given parameters is not valid")

