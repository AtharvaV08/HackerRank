import re

txt = "The rain the in Spain"
x = re.search("rain.*Spain$", txt)
print(f"match.span: {x.span()}")
print(f"match.string: {x.string}")
print(f"match.group: {x.group()}")


txt = "The rain the in rain Spain"
x = re.findall(r"h.{3}n", txt)
print(x)

print("--------------------------------\n\n")
print("--- #Find all lower case characters alphabetically between 'a' and 'm':")
txt = "The rain in Spain"
x = re.findall("[a-m]", txt)
print(x)

print("--------------------------------\n\n")
print("--- #Find all digit characters:")
txt = "That  123 will a4567b be 59 dollars"
x = re.findall("\d", txt)
print(x)


print("--------------------------------\n\n")
print("--- #Check if the string starts with" 'The')
txt = "The rain in Spain"
x = re.findall("\AThe", txt)
print(x)
# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")


print("--------------------------------\n\n")
print("--- #Check if 'ain' is present at the beginning of a WORD:")
txt = "The rain in Spain"
x = re.findall(r"\bain", txt)
print(x)


print("--------------------------------\n\n")
print("--- #Check if 'ain' is present at the end of a WORD:")
txt = "The rain in Spain"
x = re.findall(r"ain\b", txt)
print(x)


print("--------------------------------\n\n")
print("--- #Check if 'ain' is present, but NOT at the beginning of a word:")
txt = "ain The rain in Spain"
x = re.findall(r"\Bain", txt)
print(x)


print("--------------------------------\n\n")
print("--- #Check if 'ain' is present, but NOT at the end of a word:")
txt = "The rain in Spain"
x = re.findall(r"ain\B", txt)
print(x)


print("--------------------------------\n\n")
print("--- #Return a match at every no-digit character:")
txt = "The rain124 in 223156 Spain"
x = re.findall("\D", txt)
print(x)


print("--------------------------------\n\n")
print("--- #Return a match at every white-space character:")
txt = "The rain in Spain"
x = re.findall("\s", txt)
print(x)

print("--------------------------------\n\n")
print("--- #Return a match at every NON white-space character:")
txt = "The rain in Spain"
x = re.findall("\S", txt)
print(x)


print("--------------------------------\n\n")
print("--- #Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):")
txt = "The rain  _ - in 123Spain"
x = re.findall("\w", txt)
print(x)


print("--------------------------------\n\n")
print("--- #Return a match at every NON word character (characters NOT between a and Z. Like '!', '?' white-space etc.):")
txt = "The rain _ - }  $ # ^in Spain"
x = re.findall("\W", txt)
print(x)


print("--------------------------------\n\n")
print("--- #Check if the string ends with 'Spain':")
txt = "The rain in Spain"
x = re.findall("Spain\Z", txt)
print(x)



txt = "9595123456"
x = re.findall(r"[0-9]{10}", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")


txt = "atharvavaidya08@gmail.com"
txt1 = "atharvavaidya08@email.com"
txt2 = "atharva._*vaidya08@gmail.in"
txt3 = "JohnDoe@Example.com"
txt4 = "user@domain"
txt5 = "@domain.com"
txt6 = "user@.com"
txt7= "user@domain..com"

x = re.search(r"[a-zA-Z0-9].*@[a-zA-Z]+'.'{1}[a-z]*", txt7)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")


print("--------------------------------\n\n")
print("--- #Search for a sequence that starts with 'he', followed by two (any) characters, and an 'o':")
txt = "hello planet"
x = re.findall("he..o", txt) #Dot represents how many characters we want in middle
# means we have to give start and end and in middle the dot represents the numbers of characters we want to search
print(x)


print("--------------------------------\n\n")
print("--- #Check if the string starts with 'hello':")
txt = "hello planet"
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")


print("--------------------------------\n\n")
print("--- #Check if the string ends with 'planet':")
txt = "hello planet"
x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")


print("--------------------------------\n\n")
print("--- #Search for a sequence that starts with 'he', followed by 0 or more  (any) characters, and an 'o':")
txt = "hello planet"
x = re.findall("he.*o", txt)
print(x)


print("--------------------------------\n\n")
print("--- #Search for a sequence that starts with 'he', followed by 1 or more  (any) characters, and an 'o':")
txt = "hello planet"
x = re.findall("he.+o", txt)
print(x)


print("--------------------------------\n\n")
print("--- #Search for a sequence that starts with 'he', followed by 0 or 1  (any) characters, and an 'o':")
txt = "hello planet"
x = re.findall("he.?o", txt)
print(x)
#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"


print("--------------------------------\n\n")
print("--- #Search for a sequence that starts with 'he', followed by exactly 2 (any) characters, and an 'o':")
txt = "hello planet"
x = re.findall("he.{2}o", txt)
print(x)


print("--------------------------------\n\n")
print("--- #Check if the string contains either 'falls' or 'stays':")
txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("falls|stays", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


print("--------------------------------\n\n")
print("--- #Return a list containing every occurrence of 'ai':")
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


txt = "The rain in Spain"

#Check if "Portugal" is in the string:

x = re.findall("Portugal", txt)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

#search()
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


#Split the string at the first white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)


#Replace all white-space characters with the digit "9":

txt = "The rain in Spain"
x = re.sub("\s", "atyha", txt)
print(x)


#Replace the first two occurrences of a white-space character with the digit 9:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)