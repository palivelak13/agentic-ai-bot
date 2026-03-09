# import json
# import schedule
# import time
# from datetime import datetime

# FILE = "bills.json"


# # Load bills from file
# def load_bills():
#     try:
#         with open(FILE, "r") as f:
#             return json.load(f)
#     except:
#         return []


# # Save bills to file
# def save_bills(bills):
#     with open(FILE, "w") as f:
#         json.dump(bills, f, indent=4)


# # Add bill
# def add_bill():
#     bills = load_bills()

#     name = input("Bill name: ")
#     due = input("Due date (YYYY-MM-DD): ")

#     bills.append({
#         "name": name,
#         "due": due
#     })

#     save_bills(bills)

#     print("✅ Bill added successfully")


# # Show all bills
# def list_bills():
#     bills = load_bills()

#     if not bills:
#         print("No bills saved")
#         return

#     print("\n📋 Your Bills:")
#     for i, bill in enumerate(bills, 1):
#         print(f"{i}. {bill['name']} - Due: {bill['due']}")
#     print()


# # Delete bill
# def delete_bill():
#     bills = load_bills()

#     list_bills()

#     num = int(input("Enter bill number to delete: "))

#     if 0 < num <= len(bills):
#         removed = bills.pop(num - 1)
#         save_bills(bills)
#         print(f"❌ Deleted {removed['name']} bill")
#     else:
#         print("Invalid selection")


# # Reminder check
# def check_reminders():
#     bills = load_bills()

#     today = datetime.today().date()

#     for bill in bills:
#         due_date = datetime.strptime(bill["due"], "%Y-%m-%d").date()

#         days_left = (due_date - today).days

#         if days_left == 2:
#             print(f"🔔 Reminder: {bill['name']} bill due in 2 days")

#         if days_left == 0:
#             print(f"⚠️ ALERT: {bill['name']} bill due TODAY!")


# # Agent commands
# def agent():

#     while True:

#         command = input("Agent command (add/list/delete/exit): ").lower()

#         if command == "add":
#             add_bill()

#         elif command == "list":
#             list_bills()

#         elif command == "delete":
#             delete_bill()

#         elif command == "exit":
#             print("Agent stopped")
#             break

#         else:
#             print("Unknown command")


# # Schedule reminder check
# schedule.every(10).seconds.do(check_reminders)


# # Run agent
# while True:
#     schedule.run_pending()
#     agent()
#     time.sleep(1)

#2
import json
import schedule
import time
import requests
from datetime import datetime

FILE = "bills.json"

BOT_TOKEN = "8634919146:AAFSgDV9_4ec_t34UhDiQZEonih5qnpC-is"
CHAT_ID = "6144184848"


# SEND TELEGRAM MESSAGE
def send_telegram(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=data)


# LOAD BILLS
def load_bills():

    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []


# SAVE BILLS
def save_bills(bills):

    with open(FILE, "w") as f:
        json.dump(bills, f, indent=4)


# ADD BILL
def add_bill():

    bills = load_bills()

    name = input("Bill name: ")

    while True:

        due = input("Due date (YYYY-MM-DD): ")

        try:
            datetime.strptime(due, "%Y-%m-%d")
            break

        except:
            print("Invalid date format!")

    bills.append({
        "name": name,
        "due": due
    })

    save_bills(bills)

    print("Bill added successfully")


# LIST BILLS
def list_bills():

    bills = load_bills()

    if not bills:
        print("No bills saved")
        return

    print("\nYour Bills:")

    for i, bill in enumerate(bills, 1):

        print(f"{i}. {bill['name']} - Due: {bill['due']}")

    print()


# DELETE BILL
def delete_bill():

    bills = load_bills()

    list_bills()

    num = int(input("Enter bill number to delete: "))

    if 0 < num <= len(bills):

        removed = bills.pop(num - 1)

        save_bills(bills)

        print(f"{removed['name']} bill deleted")

    else:
        print("Invalid number")


# CHECK REMINDERS
def check_reminders():

    bills = load_bills()

    today = datetime.today().date()

    for bill in bills:

        try:

            due_date = datetime.strptime(bill["due"], "%Y-%m-%d").date()

        except:

            continue

        days_left = (due_date - today).days

        if days_left == 2:

            message = f"Reminder: {bill['name']} bill due in 2 days"

            print(message)

            send_telegram(message)

        if days_left == 0:

            message = f"ALERT: {bill['name']} bill due TODAY!"

            print(message)

            send_telegram(message)


# AGENT COMMANDS
def agent():

    command = input("Agent command (add/list/delete/exit): ").lower()

    if command == "add":

        add_bill()

    elif command == "list":

        list_bills()

    elif command == "delete":

        delete_bill()

    elif command == "exit":

        print("Agent stopped")

        exit()

    else:

        print("Unknown command")


# RUN REMINDER EVERY 10 SECONDS
schedule.every(10).seconds.do(check_reminders)


# MAIN LOOP
while True:

    schedule.run_pending()

    agent()

    time.sleep(1)