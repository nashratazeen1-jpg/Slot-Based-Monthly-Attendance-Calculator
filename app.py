import time
print("\n")
print("\t\t\t\t|||||||> ============================================================= <|||||||")
print("\t\t\t\t|||||||> Welcome To Nashra's: Slot-Based Monthly Attendance Calculator <|||||||")
print("\t\t\t\t|||||||> ============================================================= <|||||||\n\n")

time.sleep(2)

print("Which Month-type Attendance You want to Calculate?...\n")
time.sleep(2)
print("------------------------------------------------------------------------------------------")
print("a. 28 Days Month 📅      b. 30 Days Month 📅       c. 31 Days Month 📅      d. 15 days 🕒")
print("------------------------------------------------------------------------------------------\n\n")
time.sleep(2)

op = input("Select the Option: ")

match op:
    case 'a':
        print("You Entered Option (a)..,There are Total 24 College Days!...\n")
        time.sleep(2)

        mst = int(input("Enter Total MORNING SLOTS (10AM-12AM) You Attended (?/24): "))
        if ( mst > 24 ):
            print("⚠️  You Entered Invalid Number,...TRY AGAIN!.")
            mst = int(input("Enter Total MORNING SLOTS (10AM-12AM) You Attended (?/24): "))

        time.sleep(1)

        ast = int(input("Enter Total AFTERNOON SLOTS (1PM-3PM) You Attended (?/24): "))
        if ( ast > 24 ):
            print("⚠️  You Entered Invalid Number,...TRY AGAIN!.")
            ast = int(input("Enter Total AFTERNOON SLOTS (1PM-3PM) You Attended (?/24): "))

        time.sleep(1)

        evt = int(input("Enter Total EVENING SLOTS (3PM-5PM) You Attended (?/24): "))
        if ( evt > 24 ):
            print("⚠️  You Entered Invalid Number,...TRY AGAIN!.")
            evt = int(input("Enter Total EVENING SLOTS (3PM-5PM) You Attended (?/24): "))

        time.sleep(2)

        totalslots = mst + ast + evt
        print("\n📌 Total Slots You Attended this Month (?/72): ", totalslots)
        time.sleep(2)


        TAM = (totalslots/72)*100
        print(f"\n🎯 Your Attendance of This Month is: {TAM:.2f}% 📊")
        time.sleep(2)
        print("\t\t\t\t\t\t\t|||||||> ======= <|||||||")
        print("\t\t\t\t\t\t\t|||||||> THE END <|||||||")
        print("\t\t\t\t\t\t\t|||||||> ======= <|||||||")
        
        

    case 'b':
        print("You Entered Option (b)..,There are Total 26 College Days!...\n")
        time.sleep(2)

        mst = int(input("Enter Total MORNING SLOTS (10AM-12AM) You Attended (?/26): "))
        if ( mst > 26 ):
            print("⚠️  You Entered Invalid Number,...TRY AGAIN!.")
            mst = int(input("Enter Total MORNING SLOTS (10AM-12AM) You Attended (?/26): "))

        time.sleep(1)

        ast = int(input("Enter Total AFTERNOON SLOTS (1PM-3PM) You Attended (?/26): "))
        if ( ast > 26 ):
            print("⚠️  You Entered Invalid Number,...TRY AGAIN!.")
            ast = int(input("Enter Total AFTERNOON SLOTS (1PM-3PM) You Attended (?/26): "))

        time.sleep(1)

        evt = int(input("Enter Total EVENING SLOTS (3PM-5PM) You Attended (?/26): "))
        if ( evt > 26 ):
            print("⚠️  You Entered Invalid Number,...TRY AGAIN!.")
            evt = int(input("Enter Total EVENING SLOTS (3PM-5PM) You Attended (?/26): "))

        time.sleep(2)

        totalslots = mst + ast + evt
        print("\n📌 Total Slots You Attended this Month (?/78): ", totalslots)
        time.sleep(2)


        TAM = (totalslots/78)*100
        print(f"\n🎯 Your Attendance of This Month is: {TAM:.2f}% 📊")
        time.sleep(2)
        print("\t\t\t\t\t\t\t|||||||> ======= <|||||||")
        print("\t\t\t\t\t\t\t|||||||> THE END <|||||||")
        print("\t\t\t\t\t\t\t|||||||> ======= <|||||||")
        

    case 'c':
        print("You Entered Option (c)..,There are Total 27 College Days!...\n")
        time.sleep(2)

        mst = int(input("Enter Total MORNING SLOTS (10AM-12AM) You Attended (?/27): "))
        if ( mst > 27 ):
            print("⚠️  You Entered Invalid Number,...TRY AGAIN!.")
            mst = int(input("Enter Total MORNING SLOTS (10AM-12AM) You Attended (?/27): "))

        time.sleep(1)

        ast = int(input("Enter Total AFTERNOON SLOTS (1PM-3PM) You Attended (?/27): "))
        if ( ast > 27 ):
            print("⚠️  You Entered Invalid Number,...TRY AGAIN!.")
            ast = int(input("Enter Total AFTERNOON SLOTS (1PM-3PM) You Attended (?/27): "))

        time.sleep(1)

        evt = int(input("Enter Total EVENING SLOTS (3PM-5PM) You Attended (?/27): "))
        if ( evt > 27 ):
            print("⚠️  You Entered Invalid Number,...TRY AGAIN!.")
            evt = int(input("Enter Total EVENING SLOTS (3PM-5PM) You Attended (?/27): "))

        time.sleep(2)

        totalslots = mst + ast + evt
        print("\n📌 Total Slots You Attended this Month (?/81): ", totalslots)
        time.sleep(2)


        TAM = (totalslots/81)*100
        print(f"\n🎯 Your Attendance of This Month is: {TAM:.2f}% 📊\n\n")
        time.sleep(2)
        print("\t\t\t\t\t\t\t|||||||> ======= <|||||||")
        print("\t\t\t\t\t\t\t|||||||> THE END <|||||||")
        print("\t\t\t\t\t\t\t|||||||> ======= <|||||||")

    case 'd':
        print("You Entered Option (d)..,There are Total 15 College Days!...\n")
        time.sleep(2)

        mst = int(input("Enter Total MORNING SLOTS (10AM-12AM) You Attended (?/15): "))
        if ( mst > 15 ):
            print("⚠️  You Entered Invalid Number,...TRY AGAIN!.")
            mst = int(input("Enter Total MORNING SLOTS (10AM-12AM) You Attended (?/15): "))

        time.sleep(1)

        ast = int(input("Enter Total AFTERNOON SLOTS (1PM-3PM) You Attended (?/15): "))
        if ( ast > 15 ):
            print("⚠️  You Entered Invalid Number,...TRY AGAIN!.")
            ast = int(input("Enter Total AFTERNOON SLOTS (1PM-3PM) You Attended (?/15): "))

        time.sleep(1)

        evt = int(input("Enter Total EVENING SLOTS (3PM-5PM) You Attended (?/15): "))
        if ( evt > 15 ):
            print("⚠️  You Entered Invalid Number,...TRY AGAIN!.")
            evt = int(input("Enter Total EVENING SLOTS (3PM-5PM) You Attended (?/15): "))

        time.sleep(2)

        totalslots = mst + ast + evt
        print("\n📌 Total Slots You Attended this Month (?/45): ", totalslots)
        time.sleep(2)


        TAM = (totalslots/45)*100
        print(f"\n🎯 Your Attendance of This Month is: {TAM:.2f}% 📊")
        time.sleep(2)
        print("\t\t\t\t\t\t\t|||||||> ======= <|||||||")
        print("\t\t\t\t\t\t\t|||||||> THE END <|||||||")
        print("\t\t\t\t\t\t\t|||||||> ======= <|||||||")

    case _:
        print("⚠️  You Entered Invalid Ooption!..Choose btwn (a to d) !!!...")

ṇ