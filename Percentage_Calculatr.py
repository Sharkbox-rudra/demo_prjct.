print("🤩🤩 Welcome to our percentage calculator🤩🤩\n")
while True:


    percept = input("📌 Are you want to calculate percentage(yes/no) :").strip().lower()
    if percept == "yes":
        try:
            m = int(input("📌 Enter the main value : "))
            n = int(input("📌 Enter percentage(%) :"))
            print(f"✅ Calculated Value :: {m * (n/100)}")
        except ValueError:
            print("📌 Please Enter valid number 😓😓")

    elif(percept != "no"):
        print("📌 Enter Right command 😐😕")
        continue

    percept2 = input("📌 Are You Want to find out percentage(yes/no) :").strip().lower()
    if percept2 == "yes":
        try:
            m = int(input("📌 Enter the main value : "))
            n = int(input("📌 Enter sub-value : "))
            print(f"✅ {round(n * (100/m),2)} %")
        except ValueError:
            print("📌 Enter a valid number😐😕")

    elif percept2 != "no" :
        print("📌 Enter Right command 😐😕")
        continue

    again = input("📌 Do you Want to Continue?(yes/no): ").strip().lower()
    if again != "yes":
        print("Thank You💖... Come soon next time😍😊")
        break
     

