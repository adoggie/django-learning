
		
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
  guess = int(raw_input("Your guess: "))
  if guess == random_number:
    print "You win!"
    break
  guesses_left -= 1
else:
  print "You lose."

 
 
 phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
	if char == "A" or char == "a":
		print 'X', 
	else:
		print char, 


#Don't delete this print statement!
print




fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
  if f == 'tomato':
    print 'A tomato is not a fruit!' # (It actually is.)
    break
  print 'A', f
else:
  print 'A fine selection of fruits!'      
  
  
  
  
  
def digit_sum(n):
	mc = 0 
	s = str(n)
	# 1234 => "1234"
	for c in s:
		mc += int(c)
	return mc 
	
	
	
	
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

def reverse(text):
  # text - 'zyc'
	mc = ''
	size = len(text)
	while size > 0 : 
		mc= mc + text[size-1]
		size -= 1 
	return mc 
	
	
def anti_vowel(text):
    t=""
    for c in text:
        for i in "ieaouIEAOU":
            if c==i:
                c=""
            else:
                c=c
        t=t+c
    return t
	
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
  word = word.lower()
  total = 0
  for letter in word:
    for leter in score:
      if letter == leter:
        total = total + score[leter]
  return total
  
def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result
	
def remove_duplicates(inputlist):
    if inputlist == []:
        return []
    
# Sort the input list from low to high    
    inputlist = sorted(inputlist)
# Initialize the output list, and give it the first value of the now-sorted input list
    outputlist = [inputlist[0]]

# Go through the values of the sorted list and append to the output list
# ...any values that are greater than the last value of the output list
    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)
        
    return outputlist

def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2 
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean
   
print median([2, 4, 5, 9])

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
	basket = 0
	for mc in scores:
		basket += mc
	return basket

print grades_sum(grades)

def grades_average(grades_input):
	average = 0
	sum = grades_sum(grades_input)
	average = sum / (len(grades_input)*1.0)
	return average

print grades_average(grades)	
	
	
