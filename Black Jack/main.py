import random  # Importing the random module to generate random numbers (for card drawing)
from art import logo  # Importing the logo artwork to display at the start of the game


def draw_card():
    ### Returns a random card from the deck ###
    # List of card values (11 represents an Ace, 10 is for face cards like King, Queen, Jack)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)  # Select a random card from the list
    return card


def calculate_score(cards):
    ## Calculates and returns the score from the list of cards ##
    # If the sum of cards is 21 and there are only 2 cards (Blackjack), return 0 (special case)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # If there is an Ace (value 11) and the score exceeds 21, convert Ace to 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)  # Remove Ace from the list
        cards.append(1)  # Add a value of 1 instead of 11
    return sum(cards)  # Return the total sum of the cards


def compare(u_score, d_score):
    # Compare user and dealer scores and return an outcome
    if u_score == d_score:
        return "Draw"  # If scores are equal, it's a draw
    elif d_score == 0:
        return "Loser, Dealer has Blackjack"  # If dealer has Blackjack, user loses
    elif u_score == 0:
        return "Holy smokes you won with a Blackjack"  # If user has Blackjack, user wins
    elif u_score > 21:
        return "You busted big boy"  # If user's score exceeds 21, they lose (busted)
    elif d_score > 21:
        return "Opponent went over. You didn't do anything special"  # If dealer busts, user wins
    elif u_score > d_score:
        return "Tada! You did it. Yay you beat a computer."  # If user score is higher, user wins
    else:
        return "Oof ... maybe next time tiger..."  # If dealer score is higher, dealer wins


def play_game():
    print(logo)  # Print the game's logo artwork
    user = []  # List to store user's cards
    dealer = []  # List to store dealer's cards
    dealer_score = -1  # Initialize dealer score
    user_score = -1  # Initialize user score
    is_game_over = False  # Flag to track if the game is over

    # Draw 2 cards for both user and dealer
    for _ in range(2):
        user.append(draw_card())
        dealer.append(draw_card())

    # Game loop - continue until the game is over
    while not is_game_over:
        user_score = calculate_score(user)  # Calculate the user's score
        dealer_score = calculate_score(dealer)  # Calculate the dealer's score
        print(f"Your cards: {user}, current score: {user_score}")  # Show user's cards and score
        print(f"Dealer's first card: {dealer[0]}")  # Show dealer's first card (hide the second)

        # Check for special cases (Blackjack or bust)
        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True  # End the game if there's a winner or bust
        else:
            # Ask the user if they want to draw another card
            user_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_deal == 'y':
                user.append(draw_card())  # Draw another card if 'y' is pressed
            else:
                is_game_over = True  # End the game if 'n' is pressed

    # Dealer's turn: the dealer will keep drawing cards until their score is at least 17
    while dealer_score != 0 and dealer_score < 17:
        dealer.append(draw_card())  # Dealer draws another card
        dealer_score = calculate_score(dealer)  # Recalculate dealer's score

    # Show final hands and scores
    print(f"Your final hand: {user}, final score: {user_score}\n")
    print(f"Dealer's final hand: {dealer}, final score: {dealer_score}\n")

    # Compare the scores and print the result
    print(compare(user_score, dealer_score))


# Main game loop - ask if the user wants to play again
while input("You tryin play a game of Blackjack?? Type 'y' for yes or 'n' for no. ").lower() == 'y':
    print("\n" * 20)  # Clear the screen (optional)
    play_game()  # Start a new game