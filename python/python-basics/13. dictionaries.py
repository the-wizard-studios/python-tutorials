# Define a Dictionary
anime = {
    1: 'Dragon Ball',
    2: 'One Piece',
    3: 'Naruto'
}

# Print Dictionary Keys
print("- Print Anime Dictionary Keys -")
print(anime.keys())

# Print Dictionary Values
print("-\n Print Anime Dictionary Values -")
print(anime.values())

# Loop Dictionary
print("\n- Loop through Dictionary -")
for x in anime:
    print(anime[x])

# Loop Dictionary
print("\n- Loop through Dictionary -")
for key, value in anime.items():
    print(f"key: {key}, value: {value}")

# Access specific item from Dictionary, e.g, 1st item => key=1
print("\n- First item value in Anime Dictionary -")
print(anime[1])

# Access specific item from Dictionary using get() method, e.g, 2nd item => key=2
print("\n- Second item value in Anime Dictionary -")
print(anime.get(2))

# Access last item
print("\n- Last item value in Anime Dictionary -")
# Convert to list first, and then access last value with key=-1
print(list(anime.values())[-1])

# Add item in Dictionary
print("\n- Add item in Anime Dictionary -")
anime[4] = "Attack on Titan"
print(anime)

# Overwrite Value, e.g, overwrite value of key=3
print("\n- Overwrite value in Anime Dictionary -")
anime[3] = "Bleach"
print(anime)

# Remove Specific item, e.g, remove key=3
print("\n- Remove specific item in Anime Dictionary -")
anime.pop(3)
print(anime)

# - Bonus -
import json

print("\n- Print in terminal using indentation -")
print(json.dumps(anime, indent=4))
