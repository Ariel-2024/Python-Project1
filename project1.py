import random 

path_to_file = "word.txt"
with open(path_to_file, "r+") as f:
    words= f.read().split("\n")
print("Welcome to the Guessing Game!")
guessed_word = random.choice(words).lower()
#print(Guessed_word)

#Word displayed with underscore not showing the full word
blank = "" 
length_of_word = len(guessed_word)

for letter in range(length_of_word):
    blank += "_" 
print(blank)
#List to track guessed letter and No of turns for the word
letters_guessed = []
display = list(blank)
turns = length_of_word 

#Using The while loop

while turns > 0 and "_" in display:
  #INPUT FOR THE WORD
   guess = input("Guess a letter: ").lower()
   print(guess)
   
#The player can only guess a single letter at each time
   if len(guess) > 1:
      print("Please guess one letter at a time.")
      continue
#Player cannot guess a word twice
   if guess in letters_guessed:
     print("You have already guessed this letter. Try again")
     continue
   
   letters_guessed.append(guess)
#If word is guessed correctly and its position
   if guess in guessed_word:
      turns -= 1
      print(f"Good guess. you have {turns} turns left ")
      for i in range(length_of_word):
       if guessed_word[i] == guess:
        display[i] = guess
        print( " ".join(display))

   else:
      turns -= 1
      print(f"Incorrect guess. you have {turns} turns left")

print("Word: ", " ".join(display))
print("Guessed letters: ", ", ".join(letters_guessed))
#if word is not guessed correctly.
if "_" in display:
    final = input("Guess the full word: ").lower()
    if final == guessed_word:
        print("Correct! You win!")
    else:
        print("FAIL, Game over.")
else:
    print(" GREAT,You guessed the word!")
      



   
