def multiple_of_6():
    """
    Returns a multiple of 6, keeps asking otherwise
    :return: int
    """
    while True:
        try:
            n = input("Please give me a multiple of 6:")
            n = int(n)
            if n % 6 == 0: #means the remainder is 0
                return n
            else:
                print("That is not a multiple of 6.")
            # if n / 6 == n // 6
        except ValueError:
            print("That is not a valid number.")

multiple_of_6()