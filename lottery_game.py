import random
print("Lottery Game")
def generate_random_number():
    return random.randint(1, 100)

def check_lottery(number):
    if number % 13 == 0:
        return "Congratulations! You win this lottery."
    else:
        return get_random_moral_fact()

def get_random_moral_fact():
    moral_facts = [
        "Gambling should be done responsibly.",
        "Remember, the house always has an advantage.",
        "It's important to set limits when gambling.",
        "Gambling is not a reliable way to make money.",
        "Consider the potential consequences of gambling.",
    ]
    return random.choice(moral_facts)

def main():
    random_number = generate_random_number()
    result_message = check_lottery(random_number)

    print(f"Generated number: {random_number}")
    print(result_message)
main()
