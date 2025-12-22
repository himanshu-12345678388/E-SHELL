import os
import datetime
from model import predict_intent

def handle_command(text):
    intent = predict_intent(text)
    print(f"[DEBUG] Predicted intent: {intent}")

    if intent == "list_files":
        os.system("ls")

    elif intent == "make_dir":
        name =input("folder name:")
        os.system(f"mkdir {name}")

    elif intent == "delete_file":
        name=input("file name:")
        os.system(f"rm {name}")

    elif intent == "open_firefox":
        os.system("firefox &")

    elif intent == "calculator":
        os.system("gnome-calculator &")


    elif intent == "current_dir":
        os.system("pwd")

    elif intent == "disk_usage":
        os.system("df -h")

    elif intent == "memory_usage":
        os.system("free -h")

    elif intent == "date_time":
        print(datetime.datetime.now())

    else:
        print("❓ Command not recognized")