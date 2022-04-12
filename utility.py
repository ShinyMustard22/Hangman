def file_len(filename):
    with open(filename) as f:
        for i, _ in enumerate(f):
            pass
    return i + 1


def list_to_string(the_list):
    string = ""
    for i in the_list:
        string = string + i

    return string
