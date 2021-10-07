

def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    return sorted(strings, key=last_letter)


def raise_to(exp: int):
    def raise_exp(base: int):
        return pow(base, exp)
    return raise_exp


if __name__ == "__main__":
    result = sort_by_last_letter(("sadf", "vadim"))
    print(result)

    cubed = raise_to(3)

    print(cubed(3))
