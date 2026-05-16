import os
import datetime
from model import predict_intent

def handle_command(text):
    intent = predict_intent(text)
    print(f"[DEBUG] Predicted intent: {intent}")

    if intent == "list_files":
        os.system("ls")

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

    elif intent == "system_uptime":
        os.system("uptime")

    elif intent == "kernel_info":
        os.system("uname -a")

    elif intent == "cpu_info":
        os.system("lscpu")

    elif intent == "current_user":
        os.system("whoami")

    elif intent == "hostname":
        os.system("hostname")

    else:
        print("❓ Command not recognized")
