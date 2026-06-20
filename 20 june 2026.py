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
    "rabies": "rabies vaccine (pre-exposure) / supportive care (post-exposure)",
    "parvovirus": "intravenous fluids, antiemetics, antibiotics (metronidazole)",
    "distemper": "supportive care, antibiotics (amoxicillin), anticonvulsants",
    "leptospirosis": "antibiotics (doxycycline, penicillin)",
    "lyme disease": "antibiotics (doxycycline, amoxicillin)",
    "ringworm": "antifungal (clotrimazole, miconazole, terbinafine)",
    "mange": "antiparasitic (ivermectin, selamectin, amitraz)",
    "fleas": "topical flea treatment (fipronil, imidacloprid)",
    "ticks": "topical tick treatment (fipronil, permethrin)",
    "heartworm": "preventative (ivermectin, milbemycin), adulticide (melarsomine)",
    "roundworm": "dewormer (pyrantel pamoate, fenbendazole)",
    "tapeworm": "dewormer (praziquantel, epsiprantel)",
    "hookworm": "dewormer (pyrantel pamoate, fenbendazole)",
    "parvo": "intravenous fluids, antiemetics, antibiotics (metronidazole)",
    "kennel cough": "antibiotics (doxycycline, amoxicillin), cough suppressants",
    "influenza": "supportive care, fluids, anti-inflammatories",
    "pneumonia": "antibiotics (enrofloxacin, amoxicillin), oxygen therapy",
    "bronchitis": "bronchodilators, corticosteroids, antibiotics",
    "asthma": "bronchodilators, corticosteroids",
    "diabetes": "insulin, dietary management",
    "kidney failure": "fluid therapy, phosphate binders, dietary management",
    "liver disease": "dietary management, antioxidants, ursodeoxycholic acid",
    "heart disease": "diuretics (furosemide), ACE inhibitors, pimobendan",
    "arthritis": "NSAIDs (meloxicam, carprofen), joint supplements",
    "cancer": "chemotherapy, surgery, radiation, pain management",
    "tumor": "surgical removal, chemotherapy",
    "abscess": "drainage, antibiotics (amoxicillin, enrofloxacin)",
    "infection": "antibiotics (amoxicillin, doxycycline, enrofloxacin)",
    "sepsis": "intravenous fluids, broad-spectrum antibiotics, hospitalization",
    "anemia": "iron supplements, blood transfusion, treat underlying cause",
    "dehydration": "intravenous fluids, oral rehydration",
    "malnutrition": "nutritional support, dietary correction",
    "obesity": "dietary management, exercise",
    "allergies": "antihistamines, corticosteroids, hypoallergenic diet",
    "dermatitis": "topical treatment, corticosteroids, antibiotics",
    "conjunctivitis": "topical antibiotics (neomycin), anti-inflammatories",
    "glaucoma": "eye drops (latanoprost, timolol), surgery",
    "cataracts": "surgery (removal), topical anti-inflammatories",
    "deafness": "no treatment (supportive care), hearing aids (rare)",
    "epilepsy": "anticonvulsants (phenobarbital, potassium bromide)",
    "stroke": "supportive care, physical therapy, treat underlying cause",
    "paralysis": "physical therapy, anti-inflammatories, treat underlying cause"
}
affected_animal = random.choice(animals )
affected_disease = random.choice(diseases)
correct_treatment = treatments[affected_disease]
print(f"A {affected_animal} has been suffering from {affected_disease}")
print(f"To cure it you need to give {correct_treatment}")

 
