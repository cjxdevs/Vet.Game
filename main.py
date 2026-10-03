import random

from animal_disease import animal_diseases
from Disease import diseases
from animals import animals

# NARRATOR CHOICE
#narrator_choice_input = input("Choose your narrator type Normal or Unhinged: ").lower().strip()    
#if narrator_choice_input == "normal":
#    narrator = "normal"
#elif narrator_choice_input == "unhinged":
#    narrator = "unhinged"
#else:
#    print(f"Atleast choose the narrator choice correctly bro. Like what do you mean that you want a {narrator_choice_input} narrator")

print("=" * 30)
print("  Welcome fellow Vetrenarian")
print("=" * 30)

while True:

# PATIENT GENERATION
    species = random.choice(list(animals))
    breed = random.choice(animals[species]["breed"])
    possible_diseases = animal_diseases[species]
    disease = random.choice(possible_diseases)
    info_disease = diseases[disease]
    treatment = info_disease["treatment"]
    symptoms = info_disease["symptoms"]
    causes = info_disease["cause"]

# GAME START
    

    print("A new patient has arrived")
    input("Press enter for it's deatils.")
    print(f"Species: {species}")
    print(f"Breed: {breed}")
    for i in range(len(symptoms)):
        print("Symptoms", symptoms[i])

    player_ask = input("Do you want to treat this animal? : ").lower().strip()

    if player_ask == "yes":
        player_answer_disease = input("Enter your diagnosis : ")
        if player_answer_disease == disease:
            print("You got the disease correct")
        else:
            print("You got the disease wrong")

        print("===press Enter to continue===")
        player_answer_treatment = input("Enter the drug/treatment you would like to give the animal : ").lower().strip()
        if player_answer_treatment in treatment:
            print("You got that correct too")
        else:
            print("Uhh.. You got that wrong somehow ?")
    else:
        print("You walk away. The animal's owner is not pleased.")
    player_play_again = input("\nDo you want to treat another patient? (yes/no): ").lower().strip()
    if player_play_again != "yes":
        print("Thank you for it doc.")
        break