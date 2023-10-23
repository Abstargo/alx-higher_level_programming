#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list0 = []
    for i in range(list_length):
        try:
            el = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            el = 0
        except ZeroDivisionError:
            print("division by 0")
            el = 0
        except IndexError:
            print("out of range")
            el = 0
        finally:
            list0.append(el)
    return (list0)
