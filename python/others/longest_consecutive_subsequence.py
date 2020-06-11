def longest_consecutive_subsequence(input_list):
    lookup_dict = dict()

    smallest_element = max(input_list)
    max_length = 0

    for index, element in enumerate(input_list):
        lookup_dict[element] = index

    print(smallest_element)
    print(lookup_dict)

    for index, element in enumerate(input_list):
        length = 0
        start_element = element
        while start_element in lookup_dict.keys():
            length += 1
            if max_length < length:
                max_length = length
                smallest_element = start_element
            start_element -= 1

        length = 0
        start_element = element
        while start_element in lookup_dict.keys():
            length += 1
            if max_length < length:
                max_length = length
                if smallest_element > start_element:
                    smallest_element = start_element
            start_element += 1

    print(smallest_element, max_length)

    result = []
    for i in range(max_length):
        result.append(smallest_element)
        smallest_element += 1
    return result


print(longest_consecutive_subsequence(
    [2, 12, 9, 16, 10, 5, 3, 20, 25, 11, 1, 8, 6]))
