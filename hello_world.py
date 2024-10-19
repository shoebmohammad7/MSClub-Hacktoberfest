logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    logging.info("Script started.")
    
    user_name = input("What's your name? ").strip()  # Get user input and remove extra spaces
    
    # Error handling for empty input
    while not user_name:
        print("You didn't enter a name. Please try again.")
        user_name = input("What's your name? ").strip()
    
    greet(user_name)
    logging.info("Script ended.")
    
