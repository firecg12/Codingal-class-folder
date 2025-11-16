def bill():
    global bille
    bille = int(input("Enter the total bill amount: "))

bill()

while True:
    Payment = int(input("Enter the payment amount: "))
    change_of_bill = bille - Payment

    if bille == 0:
        print("No bill to pay.")
        print("Have a nice day!")
        break

    if change_of_bill > 0:
        print("You need to pay more.")
        print("Your remaining bill is:", change_of_bill)
        bille = change_of_bill  # Update bill for the next payment loop

    elif change_of_bill < 0:
        print("Your change is:", abs(change_of_bill))
        print("Please collect your change.")
        break

    else:
        print("Thank you for the exact payment.")
        break

