def convert_sequence(type_data, *iterables):
    if type_data == "list":
        return [item for iterable in iterables for item in iterable]
    elif type_data == "tuple":
        return tuple(item for iterable in iterables for item in iterable)
    elif type_data == "set":
        return {item for iterable in iterables for item in iterable}
    else:
        raise ValueError(f"Unsupported type: {type_data}")

# !решение ментора
# BEGIN (write your solution here)
# \\def convert_sequence(target_type, *sequences):
# \\    convertion_table = {"list": list, "tuple": tuple, "set": set}
# \\    result = []

# \\    for sequence in sequences:
# \\        result.extend(sequence)

# \\    return convertion_table[target_type](result)
# END

# плохой вариант 1
#     match type_data:
#         case "list":
#             result = []
#         case "tuple":
#             result = ()
#         case "set":
#             result = set()

#     for iterable in iterables:
#         for item in iterable:
#             match type_data:
#                 case "list":
#                     result.append(item)
#                 case "tuple":
#                     result += (item,)
#                 case "set":
#                     result.add(item)
#     return result
    # return ["a", "c", 1, 2, 3]
