gender = input("enter the gender, female or male. ")
age = int(input("enter the age"))


if age>20 and gender == "male":
    print("the individual is taxable")
elif age<=35 and age>=18 and gender == "female":
    print("the individual is taxable")
else:
    print("the individual is not taxable")