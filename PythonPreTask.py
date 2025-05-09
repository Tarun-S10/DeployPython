def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

string1 = "fried"
string2 = "fired"

if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
num = 2
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


def most_frequent(lst):
    if not lst:
        return None

    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    most_common = max(frequency, key=frequency.get)
    return most_common

my_list = [1, 9, 2, 1, 4, 1, 9, 6, 3]
print("Most frequent element:", most_frequent(my_list))

