import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize colorama for colored output
colorama.init()

# Print intro
print(f"{Fore.CYAN}Welcome to Sentiment Spy! {Style.RESET_ALL}")

# Ask user for name
user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Mystery Agent"  # Fallback if no name provided

# Store conversation history: list of tuples (text, polarity, sentiment_type)
conversation_history = []

print(f"{Fore.CYAN}Alright {user_name}, I will analyze your sentences using TextBlob "
      f"and show you the sentiment. {Style.RESET_ALL}")
print(f"{Fore.YELLOW}Type 'exit' to quit.{Style.RESET_ALL}")
print(f"{Fore.YELLOW}Type 'history' to view past sentiments.{Style.RESET_ALL}")
print(f"{Fore.YELLOW}Type 'clear' to clear history.{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.GREEN}You: {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    # Exit command
    if user_input.lower() == "exit":
        print(f"{Fore.BLUE}Exiting Sentiment Spy. Farewell, Agent {user_name}!{Style.RESET_ALL}")
        break

    # Clear history command
    if user_input.lower() == "clear":
        conversation_history.clear()
        print(f"{Fore.YELLOW}All conversation history cleared.{Style.RESET_ALL}")
        continue

    # History command
    if user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                print(f"{idx}. {text} -> {sentiment_type} "
                      f"(Polarity: {polarity:.2f})")
        continue

    # Analyze sentiment
    analysis = TextBlob(user_input)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment_type = "Positive"
        color = Fore.GREEN
    elif polarity < 0:
        sentiment_type = "Negative"
        color = Fore.RED
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW

    print(f"{color}Sentiment: {sentiment_type} "
          f"(Polarity: {polarity:.2f}){Style.RESET_ALL}")

    # Save to history
    conversation_history.append((user_input, polarity, sentiment_type))
