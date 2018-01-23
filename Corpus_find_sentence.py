
def find_sentence_indictionary(input,list_of_words_in_dict):
    output_list = []
    extra_string = ''

    for x in input:
        if x in list_of_words_in_dict:
            output_list.append(x)
        else:
            extra_string = extra_string + x
            if extra_string in list_of_words_in_dict:
                output_list.append(extra_string)
                print(output_list)
                extra_string = ''
    print(output_list)



input = "Narendramodiistheprimeministerofindia"
list_of_words_in_dict = ['Narendra','modi','is','the','primeminister','of','india']
find_sentence_indictionary(input,list_of_words_in_dict)