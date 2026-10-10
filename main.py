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

    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

# check for commands
    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE} Exiting sentimenet spy. farewall, Agent {user_name}!{Style.RESET_ALL}")
        break

    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.Cyan} All Conversation history cleared.{Style.RESET_ALL}")
        continue

    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.Cyan}Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                # choose color & emoji based on sentiment 
                if sentiment_type == "positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "negative":
                    color = Fore.RED
                    emoji = "😞"
                else:
                    color = Fore.YELLOW
                    emoji = "😭"

                print(f"{idx}. {color}{emoji} {text} "
                          f"(Polarity: {polarity:.2f}, Sentiment: {sentiment_type}){Style.RESET_ALL}")
        continue

    # Analyze sentiment
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "negative"
        color = Fore.RED
        emoji = "😞"
    else:
        sentiment_type = "neutral"
        color = Fore.YELLOW
        emoji = "😭"

     # Store in history
    conversation_history.append((user_input, polarity, sentiment_type)) 

    #print results with color, emoji, and polarity
    print(f"{color}{emoji} {sentiment_type} sentiment detected!" f"polarity: {polarity:.2f}")