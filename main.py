from art import logo, vs
from game_data import data
from random import choice
from replit import clear



def play():
  print(logo)
  is_game_over = False
  score = 0
  while not is_game_over:
    
    """Takes the account data and returns a printable format """  
    def format_data(account):
      account_name = account['name']
      account_descr = account['description']
      account_country = account['country']
      return f"{account_name}, a {account_descr}, from {account_country}"
    
    def check_answer(guess, a_followers, b_followers):
      """Checks followers against user's guess and returns True if they got it right. Or False if they got it wrong."""
      if a_followers > b_followers:
        return guess == "A"
      else:
        return guess == "B"
    
    
    # Genarate two randomly generated persons from the list
    first_contender = choice(data)
    second_contender = choice(data)
    while first_contender == second_contender:
      second_contender = choice(data)
    
    print(f'Compare A: {format_data(first_contender)}')
    print(vs)
    print(f'Against B: {format_data(second_contender)}')

    guess = input("Who has more followers? 'A' or 'B': ").upper()
    # compare who has higher followers
    first_contender_followers = first_contender['follower_count']
    second_contender_followers = second_contender['follower_count']
    
    is_correct = check_answer(guess, first_contender_followers, second_contender_followers)
    
    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score is: {score}") 
    else:
      score = score
      print(f"Sorry, that's wrong. final score: {score}")
      is_game_over = True   
    
play()
while input("Do you want to play again? 'Y' or 'N' ").lower() == 'y':
  clear()
  play()



# Angela's version

# def get_random_account():
#   """Get data from random account"""
#   return random.choice(data)

# def format_data(account):
#   """Format account into printable format: name, description and country"""
#   name = account["name"]
#   description = account["description"]
#   country = account["country"]
#   # print(f'{name}: {account["follower_count"]}')
#   return f"{name}, a {description}, from {country}"

# def check_answer(guess, a_followers, b_followers):
#   """Checks followers against user's guess 
#   and returns True if they got it right.
#   Or False if they got it wrong.""" 
#   if a_followers > b_followers:
#     return guess == "a"
#   else:
#     return guess == "b"


# def game():
#   print(logo)
#   score = 0
#   game_should_continue = True
#   account_a = get_random_account()
#   account_b = get_random_account()

#   while game_should_continue:
#     account_a = account_b
#     account_b = get_random_account()

#     while account_a == account_b:
#       account_b = get_random_account()

#     print(f"Compare A: {format_data(account_a)}.")
#     print(vs)
#     print(f"Against B: {format_data(account_b)}.")
    
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)

#     clear()
#     print(logo)
#     if is_correct:
#       score += 1
#       print(f"You're right! Current score: {score}.")
#     else:
#       game_should_continue = False
#       print(f"Sorry, that's wrong. Final score: {score}")

# game()


# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.