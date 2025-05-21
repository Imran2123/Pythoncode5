def is_even(n):
    """Return True if n is even, False otherwise."""
    return n % 2 == 0

def is_odd(n):
    """Return True if n is odd, False otherwise."""
    return n % 2 != 0

if __name__ == "__main__":
    num = int(input("Enter a number: 8"))
    print(f"{num} is even: {is_even(num)}")
    print(f"{num} is odd: {is_odd(num)}")
