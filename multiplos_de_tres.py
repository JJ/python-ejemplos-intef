
def suma_cifras(n):
    return sum(map(int, list(str(n))))


def is_multiple_of_3(n):
    sum = suma_cifras(n)
    if (sum >= 10):
        return is_multiple_of_3(sum)
    else:
        if (sum == 3) or (sum == 6) or (sum == 9):
            return True
        else:
            return False


print(is_multiple_of_3(333333))
print(is_multiple_of_3(333334))
