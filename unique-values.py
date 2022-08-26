from pprint import pprint

if __name__ == "__main__":
    list_inp = [100, 75, 100, 20, 75, 12, 75, 25]

    pprint(list_inp)

    set_res = set(list_inp)
    print("The unique elements of the input list using set():\n")
    list_res = (list(set_res))

    for item in list_res:
        print(item)
