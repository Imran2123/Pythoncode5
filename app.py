def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

if __name__ == "__main__":
    num = int 8
    print(f"{num} is even: {is_even(num)}")
    print(f"{num} is odd: {is_odd(num)}")
