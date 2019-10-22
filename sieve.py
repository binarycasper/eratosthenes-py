

def sieve(n):

    n += 1  # Add 1 to the number
    a = [True] * n  # Initialize the array with numbers
    a[0] = a[1] = False  # Set 0 and 1 to False

    for i in range(2, n):  # Enumerate numbers
        if a[i]:
            for j in range(i*i, n, i):  # Enumerate multiples
                a[j] = False

    for i, value in enumerate(a):
        if value:
            print(i)  # Print prime numbers


if __name__ == '__main__':

    print("Sieve of Eratosthenes")

    number = -1

    while number < 0:
        number = int(input("Enter a number").upper())
        if number < 0:
            print("The number should be positive")

    sieve(number)



