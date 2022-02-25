# NAME : SARVESH PATIL
# ROLL NO : 46
# Write a program to check number is prime or not

def prime_checker(input_num):
    if input_num > 1:
        for j in range(2, int(input_num / 2) + 1):
            if (input_num % j) == 0:
                print(input_num, "is not a prime number")
                break
        else:
            print(input_num, "is a prime number")
    else:
        print(input_num, "is not a prime number")


a = int(input("Enter an input number: "))
prime_checker(a)