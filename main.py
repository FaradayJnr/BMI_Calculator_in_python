# global declaration of variables
arr = ["kg/m^2", "g/cm^2"]  # string multiple array declaration
unit = 0  # integer variable named unit
height = 0.0  # double variable
weight = 0.0  # double variable
BMI = 0.0  # float variable

# function to calculate BMI and display results
def calc():
    print(arr[0])  # display the first element of the array with index 0
    print(arr[1])  # display the second element of the array with index 1
    unit = int(input("\nchoose a unit: [Type 1 or 2] "))  # take input as integer
    BMI = weight / (height * height)  # Body Mass Index is calculated by dividing the weight by the square of the height
    # using flow control statement (if ... else) to display the right unit.
    if unit == 1:
        print(f"BMI value is {BMI:.2f} {arr[0]}")
    elif unit == 2:
        print(f"BMI value is {BMI:.2f} {arr[1]}")

# main function to get input from user and call calc() function
def main():
    global height, weight  # declare the height and weight variables as global inside the main function
    print("########### Welcome to Intermediate BMI Calculator in Python ############")
    height = float(input("\nEnter your height: "))  # ask user to input the height
    weight = float(input("\nEnter your weight: "))  # ask the user to input the weight
    calc()  # call the calc() function already declared at the top

if __name__ == "__main__":
    main()  # execute main function
