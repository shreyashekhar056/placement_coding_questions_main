import random

# Get player names
name1 = input("Enter player 1: ")
name2 = input("Enter player 2: ")

print("\nComputer has fixed 5 numbers in the range of 1 to 10.")
print("You guys have to guess them... Ready???")

# Generate 5 unique random numbers between 1 and 10
nums = []
while len(nums) != 5:
    d = random.randint(1, 10)
    if d not in nums:
        nums.append(d)

# Uncomment for testing:
# print("DEBUG: Fixed numbers are", nums)

print("--------------------")

# Initialize scores and guesses
s1 = 0
s2 = 0
player1_guesses = []
player2_guesses = []

# Game runs for 3 rounds (each round both players guess)
for round_num in range(1, 4):
    print(f"\n======= Round {round_num} =======")

    # Player 1's turn
    print(f"{name1}, guess your number:")
    ch1 = int(input())
    while ch1 in player1_guesses or ch1 in player2_guesses:
        ch1 = int(input("Already chosen, pick another: "))
    player1_guesses.append(ch1)
    if ch1 in nums:
        print("✅ Correct!")
        s1 += 1
    else:
        print("❌ Wrong!")

    # Player 2's turn
    print(f"{name2}, guess your number:")
    ch2 = int(input())
    while ch2 in player1_guesses or ch2 in player2_guesses:
        ch2 = int(input("Already chosen, pick another: "))
    player2_guesses.append(ch2)
    if ch2 in nums:
        print("✅ Correct!")
        s2 += 1
    else:
        print("❌ Wrong!")

# Final result
print("\n================= RESULT =================")
print("Fixed numbers were:", nums)
print(f"{name1}'s guesses: {player1_guesses} | Score: {s1}")
print(f"{name2}'s guesses: {player2_guesses} | Score: {s2}")

if s1 > s2:
    print(f"🏆 {name1} wins!")
elif s2 > s1:
    print(f"🏆 {name2} wins!")
else:
    print("🤝 It's a tie!")