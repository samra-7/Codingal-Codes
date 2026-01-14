import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize colorama
colorama.init()

print(f"{Fore.CYAN}🌟 Welcome to Sentiment Spy! {Style.RESET_ALL}")

# Ask user name
user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Mystery Agent"

conversation_history = []

print(f"{Fore.CYAN}Hello, Agent {user_name}!{Style.RESET_ALL}")
print(
    f"Type a sentence and I will analyze it.\n"
    f"Type {Fore.YELLOW}'reset'{Style.RESET_ALL} to clear history, "
    f"{Fore.YELLOW}'history'{Style.RESET_ALL} to view it, "
    f"{Fore.YELLOW}'exit'{Style.RESET_ALL} to quit.\n"
)

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please type something or a valid command.{Style.RESET_ALL}")
        continue

    # EXIT
    if user_input.lower() == "exit":
        print(f"{Fore.BLUE}👋 Exiting Sentiment Spy. Farewell, Agent {user_name}!{Style.RESET_ALL}")
        break

    # RESET
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}🧹 Conversation history cleared!{Style.RESET_ALL}")
        continue

    # HISTORY
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}⚠️ No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}📜 Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😞"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"

                print(
                    f"{idx}. {color}{emoji} {text} "
                    f"(Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}"
                )
        continue

    # ANALYZE SENTIMENT
    polarity = TextBlob(user_input).sentiment.polarity

    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😞"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    # SAVE HISTORY
    conversation_history.append((user_input, polarity, sentiment_type))

    # PRINT RESULT
    print(f"{color}{emoji} {sentiment_type} sentiment detected! "
          f"(Polarity: {polarity:.2f}){Style.RESET_ALL}")
