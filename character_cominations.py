def char_combi(string):
    combi_list = []
    for char1 in range(len(string)-1, -1, -1):
        for char2 in range(len(combi_list)):
            combi_list.append(string[char1] + string[char2])
        combi_list.append(string[char1])

    return combi_list

print(char_combi('abc'))
