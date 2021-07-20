from functools import reduce



def list_dict_duplicate_removal(data_list):
    def run_function(x, y):
        return x if y in x else x + [y]

    return reduce(run_function, [[], ] + data_list)
