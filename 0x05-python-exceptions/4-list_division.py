#!usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Write a function that divides element by element 2 lists"""
    result = []
    for i in range(list_length):
        try:
            el_1 = my_list_1[i] if i < len(my_list_1) else 0
            el_2 = my_list_2[i] if i < len(my_list_2) else 0
            result.append(el_1 / el_2)
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
            result.append(0)
    return (result)