import random

def main():
    templates = [
        """It was about {Number} {Measure of time} ago when I arrived at the hospital in a {Mode of Transportation}. The hospital is a/an {Adjective} place, there are a lot of {Adjective2} {Noun} here. There are nurses here who have {Color} {Part of the Body}. If someone wants to come into my room I told them that they have to {Verb} first. I’ve decorated my room with {Number2} {Noun2}. Today I talked to a doctor and they were wearing a {Noun3} on their {Part of the Body 2}. I heard that all doctors {Verb} {Noun4} every day for breakfast. The most {Adjective3} thing about being in the hospital is the {Silly Word} {Noun}!""",
        
        """This weekend I am going camping with {Proper Noun (Person’s Name)}. I packed my lantern, sleeping bag, and {Noun}. I am so {Adjective (Feeling)} to {Verb} in a tent. I am {Adjective (Feeling) 2} we might see a(n) {Animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {Verb2}. I have heard that the {Color} lake is great for {Verb (ending in ing)}. Then we will {Adverb (ending in ly)} hike through the forest for {Number} {Measure of Time}. If I see a {Color} {Animal} while hiking, I am going to bring it home as a pet! At night we will tell {Number} {Silly Word} stories and roast {Noun2} around the campfire!!""",
        
        """Dear {Proper Noun (Person’s Name)}, I am writing to you from a {Adjective} castle in an enchanted forest. I found myself here one day after going for a ride on a {Color} {Animal} in {Place}. There are {Adjective2} {Magical Creature (Plural)} and {Adjective3} {Magical Creature (Plural)2} here! In the {Room in a House} there is a pool full of {Noun}. I fall asleep each night on a {Noun2} of {Noun (Plural)3} and dream of {Adjective4} {Noun (Plural)4}. It feels as though I have lived here for {Number} {Measure of time}. I hope one day you can visit, although the only way to get here now is {Verb (ending in ing)} on a {Adjective5} {Noun5}!!"""
    ]

    print("Choose a template to fill in:")
    print("1: Template 1")
    print("2: Template 2")
    print("3: Template 3")

    choice = input("Enter the number of the template you want to use: ")
    if choice == '1':
        template = templates[0]
    elif choice == '2':
        template = templates[1]
    elif choice == '3':
        template = templates[2]
    else:
        print("Invalid choice. Exiting.")
        return

    prompts = {
        "{Number}": "Enter a number: ",
        "{Measure of time}": "Enter a measure of time (e.g., days, months): ",
        "{Mode of Transportation}": "Enter a mode of transportation: ",
        "{Adjective}": "Enter an adjective: ",
        "{Adjective2}": "Enter another adjective: ",
        "{Noun}": "Enter a noun: ",
        "{Color}": "Enter a color: ",
        "{Part of the Body}": "Enter a part of the body: ",
        "{Verb}": "Enter a verb: ",
        "{Number2}": "Enter another number: ",
        "{Noun2}": "Enter another noun: ",
        "{Noun3}": "Enter a noun: ",
        "{Part of the Body 2}": "Enter another part of the body: ",
        "{Noun4}": "Enter another noun: ",
        "{Adjective3}": "Enter one more adjective: ",
        "{Silly Word}": "Enter a silly word: ",
        "{Proper Noun (Person’s Name)}": "Enter a proper noun (person's name): ",
        "{Adjective (Feeling)}": "Enter an adjective describing a feeling: ",
        "{Adjective (Feeling) 2}": "Enter another adjective describing a feeling: ",
        "{Animal}": "Enter an animal: ",
        "{Verb2}": "Enter another verb: ",
        "{Verb (ending in ing)}": "Enter a verb ending in -ing: ",
        "{Adverb (ending in ly)}": "Enter an adverb ending in -ly: ",
        "{Place}": "Enter a place: ",
        "{Room in a House}": "Enter a room in a house: ",
        "{Magical Creature (Plural)}": "Enter a plural magical creature: ",
        "{Magical Creature (Plural)2}": "Enter another plural magical creature: ",
        "{Noun2}": "Enter another noun: ",
        "{Noun (Plural)3}": "Enter a plural noun: ",
        "{Adjective4}": "Enter another adjective: ",
        "{Noun (Plural)4}": "Enter a plural noun: ",
        "{Adjective5}": "Enter an adjective: ",
        "{Noun5}": "Enter a noun: "
    }
    for placeholder, prompt in prompts.items():
        replacement = input(prompt)
        template = template.replace(placeholder, replacement, 1)  

    print("\nHere's your story:")
    print(template)

if __name__ == "__main__":
    main()
