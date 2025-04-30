import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import requests
import random
import string
import threading
import time

# Application Info
APP_NAME = 'NebulaTest'
APP_VERSION = 'vBETA 0.1'

# Function to generate a random Nitro code
def generate_nitro_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

# Function to check if a Nitro code is valid
def check_nitro_code(code):
    url = f"https://discord.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)
    return response.status_code == 200

# Discord Nitro Generator
def discord_nitro_generator():
    num_codes = simpledialog.askinteger("Discord Nitro Generator", "Enter the number of Nitro codes to generate:")
    if num_codes is None:
        return
    result = ""
    for _ in range(num_codes):
        nitro_code = generate_nitro_code()
        result += f"Generated Nitro Code: {nitro_code}\n"
        if check_nitro_code(nitro_code):
            result += "Valid Nitro Code found!\n"
            break
    else:
        result += "No valid Nitro codes were found.\n"
    messagebox.showinfo("Discord Nitro Generator", result)

# Discord Webhook Delete
def discord_webhook_delete():
    url = simpledialog.askstring("Discord Webhook Delete", "Please enter the Discord Webhook URL:")
    if url:
        response = requests.delete(url)
        if response.status_code == 204:
            messagebox.showinfo("Discord Webhook Delete", "Webhook deleted successfully.")
        else:
            messagebox.showerror("Discord Webhook Delete", "Failed to delete webhook. Please check the URL.")

# Discord Webhook Info
def discord_webhook_info():
    url = simpledialog.askstring("Discord Webhook Info", "Please enter the Discord Webhook URL:")
    if url:
        response = requests.get(url)
        if response.status_code == 200:
            webhook_info = response.json()
            info = (
                f"Name: {webhook_info.get('name', 'N/A')}\n"
                f"Channel ID: {webhook_info.get('channel_id', 'N/A')}\n"
                f"Guild ID: {webhook_info.get('guild_id', 'N/A')}\n"
                f"Token: {webhook_info.get('token', 'N/A')}"
            )
            messagebox.showinfo("Discord Webhook Info", info)
        else:
            messagebox.showerror("Discord Webhook Info", "Failed to retrieve webhook information. Please check the URL.")

# Discord Webhook Spammer
def discord_webhook_spammer():
    url = simpledialog.askstring("Discord Webhook Spammer", "Please enter the webhook URL:")
    if not url:
        return
    message = simpledialog.askstring("Discord Webhook Spammer", "Please enter the message to send:")
    if not message:
        return
    amount = simpledialog.askinteger("Discord Webhook Spammer", "Please enter the amount of messages to send:")
    if not amount:
        return
    delay = simpledialog.askfloat("Discord Webhook Spammer", "Please enter the delay between messages (in seconds):")
    if delay is None:
        return

    stop_spam = False

    def send_messages():
        nonlocal stop_spam
        for _ in range(amount):
            if stop_spam:
                break
            response = requests.post(url, json={"content": message})
            if response.status_code == 204:
                print("Message sent successfully")
            else:
                print("Failed to send message")
            time.sleep(delay)
        messagebox.showinfo("Discord Webhook Spammer", "Spamming completed.")

    def stop_spamming():
        nonlocal stop_spam
        stop_spam = True

    threading.Thread(target=send_messages, daemon=True).start()
    stop_button = ttk.Button(root, text="Stop Spamming", command=stop_spamming)
    stop_button.pack()

# Main GUI
root = tk.Tk()
root.title(f"{APP_NAME} {APP_VERSION}")
root.geometry("400x400")
root.configure(bg="#2c3e50")

# Style configuration
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10, relief="flat", background="#3498db", foreground="white")
style.map("TButton", background=[("active", "#2980b9")], relief=[("active", "flat")])

# Header
header = tk.Label(root, text=f"Welcome to {APP_NAME} {APP_VERSION}", font=("Arial", 16), bg="#2c3e50", fg="white")
header.pack(pady=10)

sub_header = tk.Label(root, text="Choose an option:", font=("Arial", 12), bg="#2c3e50", fg="white")
sub_header.pack(pady=5)

# Buttons
style.configure("TButton", font=("Arial", 12), padding=10, relief="flat", background="#3498db", foreground="black")
style.map("TButton", background=[("active", "#2980b9")], relief=[("active", "flat")])

ttk.Button(root, text="Discord Nitro Generator", command=discord_nitro_generator).pack(pady=5)
ttk.Button(root, text="Discord Webhook Delete", command=discord_webhook_delete).pack(pady=5)
ttk.Button(root, text="Discord Webhook Info", command=discord_webhook_info).pack(pady=5)
ttk.Button(root, text="Discord Webhook Spammer", command=discord_webhook_spammer).pack(pady=5)

ttk.Button(root, text="Exit", command=root.quit).pack(pady=20)

root.mainloop()
# Made by fysix. on discord.
