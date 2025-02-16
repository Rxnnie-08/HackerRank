s = input()
is_alnum = is_alpha = is_digit = is_lower = is_upper = False

for char in s:
    is_alnum |= char.isalnum()
    is_alpha |= char.isalpha()
    is_digit |= char.isdigit()
    is_lower |= char.islower()
    is_upper |= char.isupper()

print(is_alnum)
print(is_alpha)
print(is_digit)
print(is_lower)
print(is_upper)