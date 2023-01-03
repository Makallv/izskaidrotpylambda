"""
Lambda explanation if needed
"""
import time


def main():

    def list_comprehension():
        list_comp: list[int] = [i ** 2 for i in range(10000)]  # List of 10000 squared numbers
        print(list(i for i in list_comp if i % 2 == 0))  # Printing only numbers that mod with 2

    start_time1 = time.perf_counter()
    list_comprehension()
    end_time1 = time.perf_counter()

    def lambda_list():
        numbers = list(map(lambda x: x ** 2, range(10000)))  # List of 10000 squared numbers using lambda
        print(list(c for c in numbers if c % 2 == 0))  # Printing only numbers that mod with 2

    start_time2 = time.perf_counter()
    lambda_list()
    end_time2 = time.perf_counter()

    def appending():
        numbers_list: list[int] = []  # List declaration of type int
        for r in range(10000):
            numbers_list.append(r ** 2)  # Appending square of a number to the list

        print(list(w for w in numbers_list if w % 2 == 0))  # Printing only numbers that mod with 2

    start_time3 = time.perf_counter()
    appending()
    end_time3 = time.perf_counter()

    compile_time1 = end_time1 - start_time1
    compile_time2 = end_time2 - start_time2
    compile_time3 = end_time3 - start_time3

    print(f'compile time for the first or list comprehension function {compile_time1}')
    print(f'compile time for the second or lambda function {compile_time2}')
    print(f'compile time for the third or appending function {compile_time3}')


if __name__ == '__main__':
    main()
