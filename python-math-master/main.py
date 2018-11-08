from factorial import fac
from factorial_recurs import fac_recurs
from fibonacci import fib
from fibonacci_recurs import fib_rec
from simple_numbers import sim_num
from power import power
from power_recurs import power_recurs

if __name__ == "__main__":
    while True:
        userAnswer = input("Enter actions [fac, facRec, fib, fibRec, simNum, pow, powRec] or 'q' to quit: ")
        if userAnswer == "q":
            break
        else:
            userNumber = int(input("Enter number: "))
            if userAnswer == "fac":
                result = fac(userNumber)
                print(result)
            elif userAnswer == "facRec":
                result = fac_recurs(userNumber)
                print(result)
            elif userAnswer == "fib":
                result = fib(userNumber)
                print(result)
            elif userAnswer == "fibRec":
                result = fib_rec([0, 1], userNumber)
                print(result)
            elif userAnswer == "simNum":
                result = sim_num(userNumber)
                print(result)
            elif userAnswer == "pow":
                userPower = int(input("Enter power: "))
                result = power(userNumber, userPower)
                print(result)
            elif userAnswer == "powRec":
                userPower = int(input("Enter power: "))
                result = power_recurs(userNumber, userPower)
                print(result)
            else:
                print("No action")