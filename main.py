# # import json
# # import schedule
# # import time
# # from datetime import datetime

# # FILE = "bills.json"


# # # Load bills from file
# # def load_bills():
# #     try:
# #         with open(FILE, "r") as f:
# #             return json.load(f)
# #     except:
# #         return []


# # # Save bills to file
# # def save_bills(bills):
# #     with open(FILE, "w") as f:
# #         json.dump(bills, f, indent=4)


# # # Add bill
# # def add_bill():
# #     bills = load_bills()

# #     name = input("Bill name: ")
# #     due = input("Due date (YYYY-MM-DD): ")

# #     bills.append({
# #         "name": name,
# #         "due": due
# #     })

# #     save_bills(bills)

# #     print("✅ Bill added successfully")


# # # Show all bills
# # def list_bills():
# #     bills = load_bills()

# #     if not bills:
# #         print("No bills saved")
# #         return

# #     print("\n📋 Your Bills:")
# #     for i, bill in enumerate(bills, 1):
# #         print(f"{i}. {bill['name']} - Due: {bill['due']}")
# #     print()


# # # Delete bill
# # def delete_bill():
# #     bills = load_bills()

# #     list_bills()

# #     num = int(input("Enter bill number to delete: "))

# #     if 0 < num <= len(bills):
# #         removed = bills.pop(num - 1)
# #         save_bills(bills)
# #         print(f"❌ Deleted {removed['name']} bill")
# #     else:
# #         print("Invalid selection")


# # # Reminder check
# # def check_reminders():
# #     bills = load_bills()

# #     today = datetime.today().date()

# #     for bill in bills:
# #         due_date = datetime.strptime(bill["due"], "%Y-%m-%d").date()

# #         days_left = (due_date - today).days

# #         if days_left == 2:
# #             print(f"🔔 Reminder: {bill['name']} bill due in 2 days")

# #         if days_left == 0:
# #             print(f"⚠️ ALERT: {bill['name']} bill due TODAY!")


# # # Agent commands
# # def agent():

# #     while True:

# #         command = input("Agent command (add/list/delete/exit): ").lower()

# #         if command == "add":
# #             add_bill()

# #         elif command == "list":
# #             list_bills()

# #         elif command == "delete":
# #             delete_bill()

# #         elif command == "exit":
# #             print("Agent stopped")
# #             break

# #         else:
# #             print("Unknown command")


# # # Schedule reminder check
# # schedule.every(10).seconds.do(check_reminders)


# # # Run agent
# # while True:
# #     schedule.run_pending()
# #     agent()
# #     time.sleep(1)

# #2
# import json
# import schedule
# import time
# import requests
# from datetime import datetime

# FILE = "bills.json"

# BOT_TOKEN = "8634919146:AAFSgDV9_4ec_t34UhDiQZEonih5qnpC-is"
# CHAT_ID = "6144184848"


# # SEND TELEGRAM MESSAGEset CHAT_ID=your_chat_id
# def send_telegram(message):

#     url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

#     data = {
#         "chat_id": CHAT_ID,
#         "text": message
#     }

#     requests.post(url, data=data)


# # LOAD BILLS
# def load_bills():

#     try:
#         with open(FILE, "r") as f:
#             return json.load(f)
#     except:
#         return []


# # SAVE BILLS
# def save_bills(bills):

#     with open(FILE, "w") as f:
#         json.dump(bills, f, indent=4)


# # ADD BILL
# def add_bill():

#     bills = load_bills()

#     name = input("Bill name: ")

#     while True:

#         due = input("Due date (YYYY-MM-DD): ")

#         try:
#             datetime.strptime(due, "%Y-%m-%d")
#             break

#         except:
#             print("Invalid date format!")

#     bills.append({
#         "name": name,
#         "due": due
#     })

#     save_bills(bills)

#     print("Bill added successfully")


# # LIST BILLS
# def list_bills():

#     bills = load_bills()

#     if not bills:
#         print("No bills saved")
#         return

#     print("\nYour Bills:")

#     for i, bill in enumerate(bills, 1):

#         print(f"{i}. {bill['name']} - Due: {bill['due']}")

#     print()


# # DELETE BILL
# def delete_bill():

#     bills = load_bills()

#     list_bills()

#     num = int(input("Enter bill number to delete: "))

#     if 0 < num <= len(bills):

#         removed = bills.pop(num - 1)

#         save_bills(bills)

#         print(f"{removed['name']} bill deleted")

#     else:
#         print("Invalid number")


# # CHECK REMINDERS
# def check_reminders():

#     bills = load_bills()

#     today = datetime.today().date()

#     for bill in bills:

#         try:

#             due_date = datetime.strptime(bill["due"], "%Y-%m-%d").date()

#         except:

#             continue

#         days_left = (due_date - today).days

#         if days_left == 2:

#             message = f"Reminder: {bill['name']} bill due in 2 days"

#             print(message)

#             send_telegram(message)

#         if days_left == 0:

#             message = f"ALERT: {bill['name']} bill due TODAY!"

#             print(message)

#             send_telegram(message)


# # AGENT COMMANDS
# def agent():

#     command = input("Agent command (add/list/delete/exit): ").lower()

#     if command == "add":

#         add_bill()

#     elif command == "list":

#         list_bills()

#     elif command == "delete":

#         delete_bill()

#     elif command == "exit":

#         print("Agent stopped")

#         exit()

#     else:

#         print("Unknown command")


# # RUN REMINDER EVERY 10 SECONDS
# schedule.every(10).seconds.do(check_reminders)


# # MAIN LOOP
# while True:

#     schedule.run_pending()

#     agent()

#     time.sleep(1)

#3

import json
import schedule
import time
import requests
import threading
import os
import logging
from datetime import datetime

# NEW: Load .env variables
from dotenv import load_dotenv
load_dotenv()

FILE = "bills.json"

# Load secrets from .env
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    raise ValueError("BOT_TOKEN and CHAT_ID must be set in the .env file")

# Logging setup
logging.basicConfig(
    filename="reminder.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def send_telegram(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        requests.post(url, data=data, timeout=10)
        logging.info("Message sent to Telegram")

    except requests.exceptions.RequestException as e:
        logging.error(f"Telegram error: {e}")


def load_bills():

    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r") as f:
            return json.load(f)

    except json.JSONDecodeError:
        logging.error("JSON file corrupted")
        return []


def save_bills(bills):

    temp_file = FILE + ".tmp"

    with open(temp_file, "w") as f:
        json.dump(bills, f, indent=4)

    os.replace(temp_file, FILE)


def add_bill():

    bills = load_bills()

    name = input("Bill name: ").strip()

    while True:

        due = input("Due date (YYYY-MM-DD): ")

        try:
            datetime.strptime(due, "%Y-%m-%d")
            break

        except ValueError:
            print("Invalid date format")

    remind_days = input("Remind before days (default 2): ").strip()

    remind_days = int(remind_days) if remind_days.isdigit() else 2

    bills.append({
        "name": name,
        "due": due,
        "remind_before": remind_days,
        "reminded": False
    })

    save_bills(bills)

    print("Bill added successfully")


def list_bills():

    bills = load_bills()

    if not bills:
        print("No bills saved")
        return

    print("\nSaved Bills:\n")

    for i, bill in enumerate(bills, 1):

        print(
            f"{i}. {bill['name']} | Due: {bill['due']} | Remind {bill['remind_before']} days"
        )


def delete_bill():

    bills = load_bills()

    if not bills:
        print("No bills to delete")
        return

    list_bills()

    try:

        num = int(input("Bill number to delete: "))

        if 0 < num <= len(bills):

            removed = bills.pop(num - 1)

            save_bills(bills)

            print(f"{removed['name']} deleted")

        else:
            print("Invalid number")

    except ValueError:
        print("Please enter a valid number")


def check_reminders():

    bills = load_bills()

    today = datetime.today().date()

    updated = False

    for bill in bills:

        try:
            due_date = datetime.strptime(bill["due"], "%Y-%m-%d").date()

        except:
            continue

        days_left = (due_date - today).days

        if days_left == bill["remind_before"] and not bill["reminded"]:

            message = f"Reminder: {bill['name']} bill due in {days_left} days"

            send_telegram(message)

            bill["reminded"] = True

            updated = True

            time.sleep(1)

        if days_left == 0:

            message = f"⚠ ALERT: {bill['name']} bill due TODAY!"

            send_telegram(message)

            time.sleep(1)

    if updated:
        save_bills(bills)


def agent():

    print("\nCommands: add | list | delete | exit")

    command = input("Enter command: ").lower()

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


def scheduler_loop():

    schedule.every(1).minutes.do(check_reminders)

    while True:

        schedule.run_pending()

        time.sleep(1)


threading.Thread(target=scheduler_loop, daemon=True).start()

while True:

    agent()