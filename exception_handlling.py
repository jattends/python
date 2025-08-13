try:
    res = "100" / 20

except ArithmeticError:
    print("Arithmetic problem.")

except Exception :
    print("Something went wrong!")
    print("hai")