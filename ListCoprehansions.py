def main():
    my_string = "HelloMyNameIsMaria"
    my_string = "".join(
        [i if i.islower() else " " + i.lower() if i in ["N", "I"] else " " + i for i in my_string]
    )[1:]

    print(my_string)

    number_list = []
    for i in range(10000):
        number_list.append(i)

    number_list_comprehension = [number for number in range(10000)]

    print(number_list)
    print(number_list_comprehension)


if __name__ == '__main__':
    main()
