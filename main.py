"""
MadLibs
Author: 
Period/Core:


"""

#If needed, the stories can be found here: https://docs.google.com/document/d/1-rHWl163wXRi4GAgnejGqiduUowRTOv6sXdhaRxtMvo/edit?usp=sharing
#Only those who need this document have been granted access.
from colored import fg, attr
color_start =  fg('chartreuse_1')
color_name = fg(51)
color_error = fg(196)

#I also want to try a new naming scheme which I believe helps a lot with readability. It is changing the "one"s and "two"s, etc. in a sentence to 1s and 2s. This at least helps me notice which variables are which quicker.

reset = attr('reset') #To initalize the colors
def ask_prompts_1(): #Story 1's prompts
  global proper_noun_1
  global first_name_1
  global time_unit
  global proper_noun_2
  global first_name_2
  global adverb_1
  global last_name_1
  global noun_1
  global verb_1
  global plural_noun_1
  global adjective_1
  global movement_verb_1
  global noun_2
  global noun_3
  global number_1
  global adverb_2
  global adjective_2
  global noun_4
  global verb_2
  global adjective_3
  global place_1
  proper_noun_1 = input("Please give me a proper noun. ")
  first_name_1 = input("Please give me a first name. ")
  time_unit = input("Please give me a unit of time. ")
  proper_noun_2 = input("Please give me a proper noun. ")
  first_name_2 = input("Please give me a first name. ")
  adverb_1 = input("Please give me an adverb. ")
  last_name_1 = input("Please give me a last name. ")
  noun_1 = input("Please give me a noun. ")
  verb_1 = input("Please give me a verb. ")
  plural_noun_1 = input("Please give me a plural noun. ")
  adjective_1 = input("Please give me an adjective. ")
  movement_verb_1 = input("Please give me a verb describing movement. ")
  noun_2 = input("Please give me a noun. ")
  noun_3 = input("Please give me another noun. ")
  number_1 = input("Please give me a number (single character). ")
  if(int(number_1) != 1):
    time_unit += "s"
  adverb_2 = input("Please give me an adverb. ")
  adjective_2 = input("Please give me an adjective. ")
  noun_4 = input("Please give me a noun. ")
  verb_2 = input("Please give me a verb. ")
  adjective_3 = input("Please give me an adjective. ")
  place_1 = input("Please give me a place. ")
def ask_prompts_2(): #Story 2's prompts
  input("")

print("Let's play" + color_name + " Silly Sentences!" + reset + "\n\nTo play, you just need to answer the prompts in the console. For example, if I ask for a noun, you could provide a noun such as \"elephant\" or a verb like \"run\" if I ask for a verb.")
print(color_start + "\n\nLet's get started!\n\n" + reset)

while True:
  story_choice_str = input("Would you like to try story 1, which is about a vacation, or story 2, which is about a day outside the house?\nPlease respond with the number of the story you want: ")
  if story_choice_str.isnumeric():
    story_choice_int = int(story_choice_str)
    if(story_choice_int < 3 and story_choice_int > 0):
      break;
    else:
      print(color_error + "\nSorry, but that isn't 1 or 2. Please try again.\n" + reset)
  else:
    print(color_error + "\nSorry, but that isn't an integer. The number should be a single character, such as \"1\" in case you haven't done that already. Please try again.\n" + reset)

if(story_choice_int == 1):
  ask_prompts_1()
  print(first_name_1 + " and their family, the " + last_name_1 + " family, are going to the " + proper_noun_1 + "'s " + proper_noun_2 + " this summer.\n")
  print(f"\"I can't wait to {verb_1} in the {noun_1}!\" {first_name_2} {adverb_1} said.\n") #I just wanted to try out some string interpolation, I've never used it in Python before and find it incredibly helpful.
  print("\"Are you sure the " + plural_noun_1 + " won't catch you?\"")
elif(story_choice_int == 2):
  ask_prompts_2()
else:
  print("If you got this message, something went terribly wrong. If possible, please report this to me. I got " + story_choice_str + ", but expected 1 or 2.")