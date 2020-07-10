def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    index = {}
    result = []
    # first pass solution can't handle large test
    # for i in range(len(a)):
    #     curr = a[i]
    #     negative = -curr
    #     if negative in a and negative > 0:
    #         index[curr] = negative
    #         result.append(index[curr])
    for num in a:
        if num >= 0:
            if num in index:
                result.append(num)
            else:
                index[num] = 1
        else:
            negative = -num
            if negative in index:
                result.append(negative)
            else:
                index[negative] = 1

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
