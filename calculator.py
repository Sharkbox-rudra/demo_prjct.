while True:
    intro = input("✨😎Hey Guys........ I am A Calculator Buddy 🤗😍🤗\n😊 Press Enter key: ")
    if intro == "":

        try:
            m = int(input("📌Enter The 1st Number: "))
            
        except ValueError as v:
            print(v)
            continue

    try:
        n= int(input("📌Enter The 2nd Number: "))

    except ValueError as v:
        print(v)
        continue

    def sum():
        print(f"✅ Addition Of Numbers:\n📌{m}+{n} = {m+n}")
    def subs():
        if (m>n):
            print(f"✅ Substraction Of These Numbers:\n📌{m} - {n}  = {m-n}")
        else:
            print(f"✅ Substraction Of These Numbers:\n📌{n} - {m}  = {n-m}")
    def multy():
        print(f"✅ Multiplication Of these Numbers:\n📌{m} * {n} = {m*n}")

    def div():
        if (m>n):
            print(f"✅ Division Of These Numbers:\n📌{m} / {n} = {round(m/n,2)}")
        elif (m == 0 or n == 0):
            print("😕😕 Can't Divisible By Zero\n\t 😀Pls...Enter A Valid Number")
        else:
            print(f"✅ Division Of These Numbers:\n📌{n} / {m} = {round(n/m,2)}")
            
        
    def mod():
        if (m>n):
            print(f"✅ Mod value:\n📌{m} % {n} = {m%n}")
        else:
            print(f"✅ Mod value:\n📌{n} % {m} = {n%m}")

    while True:        

        whatDo = input("Thank You For Putting Numbers\n\n Let Me Know What You Want To Do\n(Add(+)/substract(-)/Multiply(*)/Division(/)/Modulas(%): ").strip()
        if (whatDo == "+"):
            sum()
        elif (whatDo == "-"):
            subs()
        elif (whatDo == "*"):
            multy()
        elif (whatDo == "/"):
            div()
        elif (whatDo == "%"):
            mod()

        againcalc = input("✔Calculate more? (yes/no): ").strip().lower()
        if againcalc != "yes":
            print("✅Done!")
            break
                
    again = input("🤩Are You Want to continue? (yes/no):  ").strip().lower()
    if again != "yes":
        print("✨😎OK FRIEND,,\n  Meet You Again Soon...💖💖")
        break
