import random

colours = ["R", "G", "B", "Y", "W", "O"]
tries = 10
code_length = 4

def generate_code():
    code = []
    for _ in range(code_length):
        color = random.choice(colours)
        code.append(color)
    return code

def guess_code(): 
    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != code_length:
            print(f"You must guess {code_length} colours.")
            continue

        for colour in guess:
            if colour not in colours: 
                print(f"Invalid colour: {colour}. Try again.")
                break 
        else: 
            break

    return guess

def check_code(guess, code):
    correct_pos = 0
    incorrect_pos = 0
    colour_counts = {color: code.count(color) for color in code}

    for guess_colour, code_colour in zip(guess, code):
        if guess_colour == code_colour:
            correct_pos += 1 
            colour_counts[guess_colour] -= 1

    for guess_colour, code_colour in zip(guess, code):
        if guess_colour != code_colour and guess_colour in colour_counts and colour_counts[guess_colour] > 0:
            incorrect_pos += 1
            colour_counts[guess_colour] -= 1

    return correct_pos, incorrect_pos

def game(): 
    code = generate_code()
    for attempts in range(1, tries + 1): 
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == code_length: 
            print(f"You guessed the code in {attempts} tries")
            break
        else:
            print(f"Correct position: {correct_pos}, Incorrect position: {incorrect_pos}")

game()