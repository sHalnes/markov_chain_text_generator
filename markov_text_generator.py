#!/usr/bin/env python
from random import randint


def main():

    TEXT_LENGTH = 8000 # the length of the generated text

    # an output file
    output = open('markov_third_order.txt', 'w')
    output.write('Generatet random text.\n')

    data = ''
    # read the text
    try:
        with open('text.txt','r') as text:
            data = text.read().lower() # making to lowercase
    except:
        FileNotFoundError

    # making data to list, it would be easier to create a set of elements so we vill use only elements from our text to
    # generate markov text. In our list there are only 25 elements, instead of 30.
    data_list = list(data)

    # zero order dictionary
    zero_order_dict = list(set(data_list)) # actually it's a list

    # first order dictionary for 2-plets
    first_order_dict = dict()
    for i in range(len(data_list)-2):
        if data_list[i] not in first_order_dict:
            first_order_dict[data_list[i]] = []
        first_order_dict[data_list[i]].append(data_list[i+1])

    # second order dictionary for 3-plets
    second_order_dict = dict()
    for i in range(len(data_list)-3):
        tuplet = data_list[i] + data_list[i+1]
        if tuplet not in second_order_dict:
            second_order_dict[tuplet] = []
        second_order_dict[tuplet].append(data_list[i+2])

    # third order dictionaru foth 4-plets
    third_order_dict = dict()
    for i in range(len(data_list) - 4):
        triplet = data_list[i] + data_list[i+1] + data_list[i+2]
        if triplet not in third_order_dict:
            third_order_dict[triplet] = []
        third_order_dict[triplet].append(data_list[i+3])

    # now create the text
    # 1. choose the first random symbol
    generated_text = zero_order_dict[randint(0, len(zero_order_dict)-1)]

    # 2. choose the second random symbol
    generated_text += first_order_dict[generated_text][randint(0, len(first_order_dict[generated_text])-1)]

    # 3. choose the third random symbol
    generated_text += second_order_dict[generated_text][randint(0, len(second_order_dict[generated_text])-1)]

    # now we can generate other 8000 symbols
    counter = TEXT_LENGTH
    while counter > 0:
        lookup_symbol = generated_text[-3:]
        generated_text += third_order_dict[lookup_symbol][randint(0, len(third_order_dict[lookup_symbol])-1)]
        counter -= 1

    output.write(generated_text)
    output.close()


if __name__ == '__main__':
    main()