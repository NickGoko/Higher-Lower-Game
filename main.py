# display logo
from art import logo, vs
from game_data import data
import random 

print(logo)
def format_account(account):
  """format account data into printable format"""
  account_name = account['name']
  account_description = account['description']
  account_country = account['country']
  return(f"{account_name}, a {account_description} from {account_country}")  

def check_answer(guess, a_followers, b_followers):

  """Take user guess and use if string to check if user is correct"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
  

score = 0

game_should_continue = True # Make game repeatable 
account_b = random.choice(data)

while game_should_continue:
  # generate random accounts
  # making account position B become account as position A
  account_a = account_b
  account_b = random.choice(data)

  while account_a == account_b:
    account_b = random.choice(data)
  # print(account_a)
  # print(account_b)

  print(f"Compare A: {format_account(account_a)}")
  print(vs)

  print(f"Against B: {format_account(account_b)}")


  # ask user for guess
  guess = input("Who has more followers 'A' or 'B': ").lower()

  
  # get follower account of each account
  a_follower_count = account_a['follower_count']
  b_follower_count = account_b['follower_count']

  # check if user is correct
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  # feedback if user if is right
  if is_correct:
    score += 1
    print(f"You're right! Current Score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry, you're wrong. Final Score {score}")
  # give user score on their score
  # Keep score





# clear the screen between rounds 
