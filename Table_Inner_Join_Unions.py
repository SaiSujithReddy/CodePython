

table1 = (('L',15),('I',12),('H',14),('J',1),('C',9),('X',4),('N',11))
table2 = (('B',13),('O',23),('H',56),('V',777),('B',171),('X',43),('N',65))


def table_inner_join_union(table1,table2):
    dict_1 = {}
    dict_2 = {}
    dict_3 = {}
    output_list_tuples = []

    for x in table1:
        dict_1[x[0]] = x[1]

    for x in table2:
        dict_2[x[0]] = x[1]

    for x in dict_1:
        if x in dict_2:
            dict_3[x] = [dict_1[x],dict_2[x]]

    sorted_keys = sorted(dict_3.keys())

    for x in sorted_keys:
        output_list_tuples.append((x,dict_3[x][0],dict_3[x][1]))

    print(dict_1)
    print(dict_2)
    print(dict_3)
    print(output_list_tuples)


table_inner_join_union(table1,table2)