def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    index = {}
    # loop though weight list with
    # if the compliment is in the dictionary
    # find the index of the compliment
    # other wise put weight in the index
    for i in range(length):
        curr_weight = weights[i]
        compliment_weight = limit - curr_weight
        if compliment_weight in index:
            compliment_index = index[compliment_weight]
            indices_list = [compliment_index, i]
            indices_list.sort(reverse=True)
            return indices_list
        else:
            index[curr_weight] = i

    # return None


# print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
