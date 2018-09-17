def validate_pin(pin):
    if pin.isdecimal():
        return(len(pin) == 6 or len(pin) == 4)
    else:
        return False




print(validate_pin("1"),False)
print(valiNdate_pin("12"),False)
print(validate_pin("123"),False)
print(validate_pin("12345"),False)
print(validate_pin("1234567"),False)
print(validate_pin("-1234"),False)
print(validate_pin("1.234"),False)
print(validate_pin("-1.234"),False)
print(validate_pin("00000000"),False)
print("n")
print(validate_pin("a234"),False)
print(validate_pin(".234"),False)
print(validate_pin("-123"),False)
print(validate_pin("-1.234"),False)
print(validate_pin("1234"),True)
print(validate_pin("0000"),True)
print(validate_pin("1111"),True,)
print(validate_pin("123456"),True)
print(validate_pin("098765"),True)
print(validate_pin("000000"),True, "Wrong output for '000000'")
print(validate_pin("123456"),True)