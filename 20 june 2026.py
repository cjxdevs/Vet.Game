#Random animal with random disease generator
import random
animals = [
    "dog", "cat", "horse", "cow", "sheep", "goat", "pig", "chicken", "duck", "turkey",
    "rabbit", "guinea pig", "hamster", "gerbil", "mouse", "rat", "ferret", "parrot", "budgerigar",
    "canary", "goldfish", "koi", "guppy", "betta", "angelfish", "turtle", "tortoise", "lizard",
    "gecko", "iguana", "chameleon", "snake", "python", "boa", "frog", "toad", "salamander",
    "newt", "monkey", "chimpanzee", "gorilla", "orangutan", "baboon", "lemur", "elephant", "rhinoceros",
    "hippopotamus", "giraffe", "zebra", "donkey", "mule", "bison", "buffalo", "yak", "reindeer",
    "moose", "elk", "deer", "antelope", "gazelle", "impala", "kangaroo", "koala", "wombat",
    "platypus", "echidna", "tiger", "lion", "leopard", "jaguar", "cheetah", "puma", "lynx",
    "bobcat", "wolf", "coyote", "fox", "jackal", "bear", "polar bear", "panda", "raccoon",
    "skunk", "badger", "otter", "mink", "weasel", "mole", "hedgehog", "porcupine", "armadillo",
    "sloth", "anteater", "tapir", "walrus", "seal", "sea lion", "dolphin", "orca", "whale",
    "shark", "ray", "octopus", "squid", "cuttlefish", "lobster", "crab", "shrimp", "snail",
    "slug", "worm", "bee", "butterfly", "moth", "beetle", "dragonfly", "grasshopper", "cricket",
    "spider", "scorpion", "centipede", "millipede"
]
diseases = [
    "rabies", "parvovirus", "distemper", "leptospirosis", "lyme disease", "ringworm",
    "mange", "fleas", "ticks", "heartworm", "roundworm", "tapeworm", "hookworm",
    "parvo", "kennel cough", "influenza", "pneumonia", "bronchitis", "asthma",
    "diabetes", "kidney failure", "liver disease", "heart disease", "arthritis",
    "cancer", "tumor", "abscess", "infection", "sepsis", "anemia", "dehydration",
    "malnutrition", "obesity", "allergies", "dermatitis", "conjunctivitis",
    "glaucoma", "cataracts", "deafness", "epilepsy", "stroke", "paralysis"
]

#treatments for diseases
treatments = {
    "rabies": ["rabies vaccine", "supportive care"],
    "parvovirus": ["intravenous fluids", "antiemetics", "metronidazole"],
    "distemper": ["supportive care", "amoxicillin", "anticonvulsants"],
    "leptospirosis": ["doxycycline", "penicillin"],
    "lyme disease": ["doxycycline", "amoxicillin"],
    "ringworm": ["clotrimazole", "miconazole", "terbinafine"],
    "mange": ["ivermectin", "selamectin", "amitraz"],
    "fleas": ["fipronil", "imidacloprid"],
    "ticks": ["fipronil", "permethrin"],
    "heartworm": ["ivermectin", "milbemycin", "melarsomine"],
    "roundworm": ["pyrantel pamoate", "fenbendazole"],
    "tapeworm": ["praziquantel", "epsiprantel"],
    "hookworm": ["pyrantel pamoate", "fenbendazole"],
    "parvo": ["intravenous fluids", "antiemetics", "metronidazole"],
    "kennel cough": ["doxycycline", "amoxicillin", "cough suppressants"],
    "influenza": ["supportive care", "fluids", "anti-inflammatories"],
    "pneumonia": ["enrofloxacin", "amoxicillin", "oxygen therapy"],
    "bronchitis": ["bronchodilators", "corticosteroids", "antibiotics"],
    "asthma": ["bronchodilators", "corticosteroids"],
    "diabetes": ["insulin"],
    "kidney failure": ["fluid therapy", "phosphate binders"],
    "liver disease": ["dietary management", "antioxidants", "ursodeoxycholic acid"],
    "heart disease": ["furosemide", "ACE inhibitors", "pimobendan"],
    "arthritis": ["meloxicam", "carprofen", "joint supplements"],
    "cancer": ["chemotherapy", "surgery", "radiation", "pain management"],
    "tumor": ["surgical removal", "chemotherapy"],
    "abscess": ["drainage", "amoxicillin", "enrofloxacin"],
    "infection": ["amoxicillin", "doxycycline", "enrofloxacin"],
    "sepsis": ["intravenous fluids", "broad-spectrum antibiotics", "hospitalization"],
    "anemia": ["iron supplements", "blood transfusion"],
    "dehydration": ["intravenous fluids", "oral rehydration"],
    "malnutrition": ["nutritional support", "dietary correction"],
    "obesity": ["dietary management", "exercise"],
    "allergies": ["antihistamines", "corticosteroids", "hypoallergenic diet"],
    "dermatitis": ["topical treatment", "corticosteroids", "antibiotics"],
    "conjunctivitis": ["neomycin", "anti-inflammatories"],
    "glaucoma": ["latanoprost", "timolol", "surgery"],
    "cataracts": ["surgery", "topical anti-inflammatories"],
    "deafness": ["no treatment", "supportive care"],
    "epilepsy": ["phenobarbital", "potassium bromide"],
    "stroke": ["supportive care", "physical therapy"],
    "paralysis": ["physical therapy", "anti-inflammatories"]
}

affected_animal = random.choice(animals)
affected_disease = random.choice(diseases)
correct_treatment = treatments[affected_disease]

print(f"A {affected_animal} has been suffering from {affected_disease}")


player_guess = input(f"what drug would you like to give to {affected_animal} with the disease {affected_disease}? ")
if player_guess.lower() in correct_treatment:
    print(f"Congratualtions! you were able to save the {affected_animal}")
else :
    print(f"Sad you weren't able to save the {affected_animal}")
    print(f"the correct drug(s) to give were {correct_treatment}")



