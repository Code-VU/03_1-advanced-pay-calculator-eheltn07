def calculatePay():
    # This first line is provided for you
    hours = input("Enter Hours: ")
    hours = float(hours)

    rate = input("Enter Rate: ")
    rate = float(rate)

    if hours > 40:
        overtime_hours = hours - 40
        normal_hours = 40

        overtime_pay = overtime_hours * rate * 1.5
        normal_pay = normal_hours * rate

        gross_pay = normal_pay + overtime_pay
    else:
        gross_pay = hours * rate

    print (f"Pay: {gross_pay}")
    
    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
