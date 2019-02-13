def sort_array(source_array):

    for i in range(0, len(source_array)):
        for j in range(i, len(source_array)):
            if(source_array[i] % 2 == 1 and source_array[j] % 2 == 1):
                if(source_array[j] < source_array[i]):
                    aux = source_array[i]
                    source_array[i] = source_array[j]
                    source_array[j] = aux
    return source_array
// for each element in source_array count i
//     for each element in source _array starting from i
//         if remainder of element at i / 2 == 1 && remainder of element at j / 2 == 1
//             check if element at j < element at i
//                 aux = element at i
//                 element at i = element at j
//                 element at j = aux
