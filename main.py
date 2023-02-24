import sys
import time
import json
from Admin import Admin
from User import User

print("-------------------------------------------->>>>>Welcome to Online Food App <<<<<-------------------------------------------------\n")
time.sleep(5)
demo1 = User()
print(demo1.login("lucky12@gmail.com", "Lucky"))

while True:
    l = []
    rs = 0
    order_history = {}
    print("+=" * 50)
    print("------>>>>>Press P 👉👉 For Place New Order")
    print("------>>>>>Press U 👉👉 For Update Profile")
    print("------>>>>>Press H 👉👉 For Get History From App")
    print("------>>>>>Press E 👉👉 For Exit From App")
    print("--------------------------------------------------------")
    user_input = input("Press Button :")
    if user_input == "P" or user_input == "p":
        with open("Food Item.json", "r") as f:
            temp = json.load(f)
        print("1.", temp["1"]["Quantity"], " ", temp["1"]["Food Name"], "..........................",
              temp["1"]["Price"], "Rupee")
        print("2.", temp["2"]["Quantity"], " ", temp["2"]["Food Name"], "..........................",
              temp["2"]["Price"], "Rupee")
        print("3.", temp["3"]["Quantity"], " ", temp["3"]["Food Name"], "..........................",
              temp["3"]["Price"], "Rupee")
        print("Press 0 for End ")
        print()
        print("------------------------->>>>>Press 999 For Place Your Order <<<<------------------------")
        ch = 1
        while ch != 0:
            ch = int(input(" Press Button For Order----> "))
            if ch == 1:
                rs += 240
                l.append(temp["1"]["Food Name"])

            elif ch == 2:
                rs += 320
                l.append(temp["2"]["Food Name"])

            elif ch == 3:
                rs += 900
                l.append(temp["3"]["Food Name"])

            elif ch == 999:
                print(l)
                order_history = {"Order History": l, "Total Bill": rs}
                with open("Payment.json", "w") as f:
                    json.dump(order_history, f, indent=5)
                time.sleep(2)
                print("Total Bill : - ", rs)
                print(" ****************Your Order Got Placed*****************")
                print("You'll Get Your Order Soon")
                print()
                print("******************Thanks For Using Online Food App********************")
                break

    elif user_input == "H" or user_input == "h":
        with open("Payment.json", "r") as f:
            temp = json.load(f)
            print(temp)

    elif user_input == "U" or user_input == "u":
        demo1.update_profile()

    elif user_input == "E" or user_input == "e":
        time.sleep(3)
        print("*-*-*-*-*-*-*-*-*Thanks For Using Online Food App*-*-*-*-*-*-*-*-*")
        sys.exit()
        