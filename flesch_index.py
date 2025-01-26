f=open("input.txt","r")
t=f.read()
words=t.split()
print(words)
word_count=len(words)
print(word_count)
sentence_endings = ['.', '!', '?', ';', ':']
sentence_count = 0
current_sentence = ""

for char in t:
    if char in sentence_endings:  
        if current_sentence.strip():  
            sentence_count += 1
        current_sentence = ""  
    else:
        current_sentence += char  

if current_sentence.strip():
    sentence_count += 1


print("Sentence count:", sentence_count)
vowels = "aeiou"
syllable_count = 0
for word in words:
    word = word.lower()  
    if len(word) <= 3:
        syllable_count += 1
        continue

    word_syllables = 0
    i = 0
    while i < len(word):
        if word[i] in vowels:
            if i + 1 < len(word) and word[i + 1] in vowels:
                word_syllables += 1
                i += 2  
            else:
                word_syllables += 1
                i += 1
        else:
            i += 1

    if word.endswith("es") or word.endswith("ed"):
        word_syllables -= 1
    elif word.endswith("e") and not word.endswith("le"):
        word_syllables -= 1
    if word_syllables < 1:
        word_syllables = 1

    syllable_count += word_syllables

print("Syllable count:", syllable_count)
f=round(206.835-1.1015*(word_count/sentence_count)-84.6*(syllable_count/word_count))

print( " flesch index:",f)
g=round(0.39*(word_count/sentence_count)+11.8*(syllable_count/word_count)-15.59)
print(" grade :",g)

if g>=0 and g<=30:
    print(" college level ")
elif g>=50 and g<=60:
        print(" school level ")
        
elif g>=90 and g<=100:
        print("4 th grade ")
