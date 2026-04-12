import colorama
from colorama import Fore, Style
from textblob import TextBlob
import random 

colorama.init()

print(f"{Fore.CYAN}🕵️‍♀️ Welcome to SENTIMENT! 🔍{Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()

if not user_name:
    agent_names = ["Shadow", "Echo", "Cipher", "Nova", "Vortex", "Phoenix", "Raven", "Blaze"]
    user_name = random.choice(agent_names)
    print(f"{Fore.RED}No name entered. You will be known as Agent {user_name}!{Style.RESET_ALL}")

conversation_history = []

print(f"\n{Fore.CYAN}Hello, Agent {user_name}!{Style.RESET_ALL}")
print(f"Type a sentence and I will analyze its sentiment 🔍")
print(f"Commands: {Fore.YELLOW}reset{Fore.CYAN}, {Fore.YELLOW}history{Fore.CYAN}, {Fore.YELLOW}exit{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.GREEN}You: {Style.RESET_ALL}").strip()
    
    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue
    
    # EXIT
    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE}🚪 Exiting Sentiment Spy...{Style.RESET_ALL}")
        
        # 🔥 FINAL REPORT
        if conversation_history:
            total = len(conversation_history)
            positives = sum(1 for x in conversation_history if x[2] == "Positive")
            negatives = sum(1 for x in conversation_history if x[2] == "Negative")
            neutrals = sum(1 for x in conversation_history if x[2] == "Neutral")

            print(f"\n{Fore.CYAN}📊 Final Sentiment Report:{Style.RESET_ALL}")
            print(f"Total Entries: {total}")
            print(f"{Fore.GREEN}Positive: {positives}{Style.RESET_ALL}")
            print(f"{Fore.RED}Negative: {negatives}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Neutral: {neutrals}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}No data to report.{Style.RESET_ALL}")

        print(f"{Fore.CYAN}Farewell, Agent {user_name}! 🕵️‍♀️{Style.RESET_ALL}")
        break
    
    # RESET
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}🔄 All conversation history cleared!{Style.RESET_ALL}")
        continue
    
    # HISTORY
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}📋 Conversation History:{Style.RESET_ALL}")
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
                
                print(f"{idx}. {color}{emoji} {text} "
                      f"(Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")
        continue
    
    # SENTIMENT ANALYSIS
# SENTIMENT ANALYSIS
       # SENTIMENT ANALYSIS
    polarity = TextBlob(user_input).sentiment.polarity

    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"

        print(random.choice([
            f"{Fore.BLUE}That's great to hear! 😎{Style.RESET_ALL}",
            f"{Fore.BLUE}Love that energy 🔥{Style.RESET_ALL}",
            f"{Fore.BLUE}Nicee, glad you're feeling good!{Style.RESET_ALL}",
            f"{Fore.BLUE}W mood fr{Style.RESET_ALL}"
        ]))

        if polarity == 1:
            print(f"{Fore.MAGENTA}Wow, that's a perfect 1! You're on cloud nine! ☁️{Style.RESET_ALL}")

    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😞"

        print(random.choice([
            f"{Fore.BLUE}I'm sorry to hear that 😔{Style.RESET_ALL}",
            f"{Fore.BLUE}Hope things get better soon{Style.RESET_ALL}",
            f"{Fore.BLUE}That sucks, but you'll get through it 💪{Style.RESET_ALL}",
            f"{Fore.BLUE}Stay strong friend{Style.RESET_ALL}"
        ]))

        if polarity == -1:
            print(f"{Fore.MAGENTA}Yikes, a perfect -1! I hope it gets better. 😬{Style.RESET_ALL}")

    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

        print(random.choice([
            f"{Fore.BLUE}You seem pretty neutral about that{Style.RESET_ALL}",
            f"{Fore.BLUE}Just a normal vibe I see{Style.RESET_ALL}",
            f"{Fore.BLUE}Nothing too strong there{Style.RESET_ALL}",
            f"{Fore.BLUE}Chill response{Style.RESET_ALL}"
        ]))

    # SAVE HISTORY (THIS MUST BE OUTSIDE THE IF/ELSE)
    conversation_history.append((user_input, polarity, sentiment_type))

    print(f"{color}{emoji} {sentiment_type} sentiment detected! "
          f"(Polarity: {polarity:.2f}){Style.RESET_ALL}")
    
