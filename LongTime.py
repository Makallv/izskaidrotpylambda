import time


def main():
    start_time = time.perf_counter()

    def long_compile():
        numbers = list(map(lambda number: number, range(100_000_000)))

        for x in numbers:
            for j in numbers:
                c: int = x ** j

        return c # NOQA

    long_compile()
    end_time = time.perf_counter()

    compile_time = end_time - start_time

    print(compile_time)


if __name__ == '__main__':
    main()
