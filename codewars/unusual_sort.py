def unusual_sort(array):
    alpha_array = []
    num_array = []
    for char in array:
        if type(char) == str and char.isalpha():
            alpha_array.append(char)
        else:
            if num_array:
                for n, val in enumerate(num_array):
                    if int(char) > int(val):
                        if len(num_array) - 1 > n:
                            continue
                        else:
                            num_array.append(char)
                    elif type(val) == str:
                        num_array.insert(n, char)
                    elif num_array and len(num_array) >= n:
                        if int(char) < num_array[n + 1]:
                            num_array.insert(n + 1, char)
                    else:
                        num_array.append(char)
            else:
                num_array.append(char)

    alpha_array.sort()
    return alpha_array + num_array

print unusual_sort([3, "3", "2", 2, "2", "1", 1, "a", "b", "c", ])
