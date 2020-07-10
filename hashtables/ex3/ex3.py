def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # dict is the arr[0] values as key
    # check following arrays if anything mathes key in dict
    # if it does increment the number key in dict
    # check the dict if the value == the length of arrays, that's the key we need to append to result
    index = {}
    result = []
    for num in arrays[0]:
        index[num] = 1
    for arr in arrays[1:]:
        for num in arr:
            if num in index:
                index[num] += 1
            else:
                index[num] = 1
    for key, value in index.items():
        if value == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
    # print(intersection([
    #     [1, 2, 3],
    #     [1, 4, 5],
    #     [1, 6, 7]
    # ]))
