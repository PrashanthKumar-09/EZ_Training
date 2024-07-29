# Context:
# In the fantasy adventure game, "Chronicles of Numeria," players embark on quests that involve solving numerical puzzles to unlock ancient secrets and treasures. One of the key challenges is identifying palindromic numbers to open magical gates and chests. A palindrome is a number that reads the same forward and backward, such as 121 or 3443. The game needs a reliable and efficient tool to check if a given number is a palindrome to ensure smooth and engaging gameplay.
# Scenario:
# Players of "Chronicles of Numeria" frequently encounter enchanted doors and chests that require them to enter palindromic numbers to proceed. To maintain the game's immersive experience, the game engine must quickly and accurately determine if the numbers entered by players are palindromes. This requires a robust algorithm that can handle various inputs and provide instant feedback.

# Method 1

n=input()
t=n[::-1]
if n==t:
    print("palindrome")
else:
    print("not palindrome")

# Method 2
n=int(input())
t=n
ans2=0
while n>0:
    digit=n%10
    ans2=ans2*10+digit
    n=n//10
if(t==ans2):
    print("palindrome")
else:
    print("not palindrome")
