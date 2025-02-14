d = {} #empty dict
eng_to_spa = {"one":"uno", "two": "dos", "three": "tres"} #english is the key
print(eng_to_spa)
print(eng_to_spa["three"])
eng_to_spa["pineapple"] = "piña"
eng_to_spa.update({"yes": "si", "no": "no", "I": "yo", "am": "soy", "dominican": "dominicano"})
print(eng_to_spa)
print(f"I know {len(eng_to_spa)} spanish words")
sentence = "I am dominican"
words = sentence.split()
translation = ""
for word in words:
    translation += eng_to_spa[word]+" "
print(f"{sentence} translates to: {translation}")
print(list(eng_to_spa.values()))
print(list(eng_to_spa.keys()))
x = eng_to_spa.pop("pineapple")
print(x)
print(eng_to_spa)

if "car" in eng_to_spa:
    print(eng_to_spa["car"])
else:
    print("I dont know this word")

print(eng_to_spa.get("car", "sorry dont know"))
eng_to_spa.setdefault("one", "sorry dont know")
eng_to_spa.setdefault("monkey", "sorry dont know")
print(eng_to_spa)