#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    for i in range(0, len(weights)):

        item = hash_table_retrieve(ht, limit - weights[i])
        if item != None:

            if weights[i] + weights[item] == limit:
                tmp = [None] * 2
                if i > item:
                    tmp[0] = i
                    tmp[1] = item
                else:
                    tmp[0] = item
                    tmp[1] = i

                return tmp
        hash_table_insert(ht, weights[i], i)
    

    return None


weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)

print(answer_2)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
