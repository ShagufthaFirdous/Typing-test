import json 
import time 
import random 
from difflib import SequenceMatcher

with open ("passages.json", "r") as file :
    passages = json.load(file)

print("=" * 60)
print("TYPING TEST".center(70))
print("=" *60)

# CHOOSE DIFFICULTY LEVEL 

print("Choose your difficulty level:\n1. Easy\n2. Medium\n3. Hard")
choice = int(input("\nEnter your choice (1/2/3):"))

if choice == 1:
    difficulty = "easy"
elif choice == 2:
    difficulty = "medium"
elif choice == 3:
    difficulty = "hard"
else:
    print("\nInvalid choice. Starting with Easy mode.")
    difficulty = "easy"

# SELECTING RANDOM PASSAGE 

text = random.choice(passages[difficulty])

print("\n" + "-" * 70)
print(f"\nDifficulty : {difficulty.upper()}")
print("\n" + "-" * 70)

print("\nType the following passage:")
print(text)
input("\nPress Enter when you are ready to type...")
print("\nStart typing!")

start_time = time.time() 
typed_text = input("\n>")
end_time = time.time()
time_taken = end_time - start_time


# ANALYZING THE TYPED TEXT 

match = SequenceMatcher(None,text,typed_text)
correct_char = 0 
incorrect_char = 0 
extra_char = 0 
missing_char = 0 

for tag, originalStart, originalEnd, typedStart, typedEnd in match.get_opcodes():
    original_length = originalEnd - originalStart
    typed_length = typedEnd - typedStart

    if tag == "equal":
        correct_char += original_length

    elif tag == "replace":
        incorrect_count = min(original_length,typed_length)
        incorrect_char += incorrect_count
        if typed_length > original_length:
            extra_char += typed_length - original_length
        elif original_length > typed_length:
            missing_char += original_length - typed_length

    elif tag == "insert":
        extra_char += typed_length

    elif tag == "delete":
        missing_char += original_length




# ACCORDING TO STANDARD TYPING CONVENTION (5 CHARAS = 1 WORD)

minutes = time_taken/60
# CALCULATING WORDS PER MINUTE
if minutes > 0:
    wpm = (len(typed_text)/5)/minutes
else: 
    wpm = 0 

# CALCULATING ACCURACY 
total_accuracy = max(len(text), len(typed_text))

if total_accuracy > 0 :
    accuracy = (correct_char/total_accuracy) * 100
else:
    accuracy = 0 

errors = incorrect_char + missing_char + extra_char

# DISPLAY THE RESULT 

print("=" * 60)
print("RESULT".center(70))
print("=" * 70)
print(f"Difficult            : {difficulty.upper()}")
print(f"Time taken           : {time_taken:.2f} seconds")
print(f"Characters typed     : {len(typed_text)}")
print(f"Correct characters   : {correct_char}")
print(f"Incorrect characters : {incorrect_char}")
print(f"Extra Characters     : {extra_char}")
print(f"Missing Characters   : {missing_char}")
print(f"Total Errors         : {errors}")
print(f"Accuracy             : {accuracy:.2f}%")
print("=" * 60)



