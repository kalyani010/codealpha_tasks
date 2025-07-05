import random

# Word list
words = ["apple", "robot", "cloud", "space", "python"]
word = random.choice(words)

# Game setup
display = ["_"] * len(word)
guessed = []
attempts = 6

print("🎮 Welcome to Hangman!")
print("🎯 Guess the word one letter at a time.")
print("❌ You can make 6 incorrect guesses.\n")

# Game loop
while attempts > 0:
    print(f"\n🔤 Word: {' '.join(display)}")
    print(f"📘 Guessed Letters: {' '.join(sorted(guessed))}")
    print(f"❤️ Remaining Attempts: {attempts}")

    guess = input("👉 Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single letter.")
        continue

    if guess in guessed:
        print("🔁 You already guessed that letter.")
        continue

    guessed.append(guess)

    if guess in word:
        print("✅ Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print(f"❌ '{guess}' is not in the word.")
        attempts -= 1

    if "_" not in display:
        print(f"\n🎉 You won! The word was: {word}")
        break

if "_" in display:
    print(f"\n💀 Game over! The correct word was: {word}")
