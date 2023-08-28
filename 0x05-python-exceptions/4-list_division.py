#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            division_result = my_list_1[i] / my_list_2[i]
        except (IndexError, ZeroDivisionError):
            division_result = 0
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
            elif my_list_2[i] == 0:
                print("division by 0")
        except (TypeError, ValueError):
            division_result = 0
            print("wrong type")
        finally:
            result.append(division_result)

                        return result
