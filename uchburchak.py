def find_maximum_perimeter_triangle(n, lengths):
    lengths.sort(reverse=True)

    for i in range(n - 2):
        if lengths[i] < lengths[i + 1] + lengths[i + 2]:
            result = [lengths[i + 2], lengths[i + 1], lengths[i]]
            return result

    return -1

with open("INPUT.TXT", "r") as input_file:
    n = int(input_file.readline().strip())
    lengths = list(map(int, input_file.readline().split()))

result = find_maximum_perimeter_triangle(n, lengths)

with open("OUTPUT.TXT", "w") as output_file:
    if type(result) == list:
        output_file.write(" ".join(map(str, result)))
    else:
        output_file.write(str(result))
