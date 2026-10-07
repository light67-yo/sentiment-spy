import colorama 
from colorama import Fore, Style
from textblob import TextBlob

# Initialize colorama for colored output
colorama.init()

# Emoji for the start of a program
print(f"{Fore.CYAN}🚀 welcome to sentiment spy! 🚀 {Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Mysterious Agent" # fallback if user doesn't provide a name

# Store conversation as a list of tuples: (text, polarity, sentiment_type)
conversation_history = []

print(f"\n{Fore.CYAN}Hello, Agent {user_name}!")
print(f"type a sentence and i will analyze your sentence with TextBlob and show you the sentiment.")
print(f"Type {Fore.YELLOW}exit{Fore.CYAN} to quit.{Style.RESET_ALL}\n"
  f"or {Fore.YELLOW}exit{Fore.CYAN} to quit.{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()