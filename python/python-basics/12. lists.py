# Define a list
anime = ['Dragon Ball', 'One Piece', 'Naruto']

# Print list
print("- Print Anime List -")
print(anime)

# Loop List
print("\n- Loop through List -")
for x in anime:
    print(x)

# Access specific item from list, e.g, 1st item => index=0
print("\n- First item in Anime List -")
print(anime[0])

# Access last item
print("\n- Last item in Anime List -")
print(anime[-1])

# Append item in List
print("\n- Append item in Anime List -")
anime.append("Attack on Titan")
print(anime)

# Insert at Specific Index, e.g, insert at 3rd Position => index=2
print("\n- Insert item at specific index in Anime List -")
anime.insert(2, "Bleach")
print(anime)

# Print Range of Items in Anime List, e.g, 2nd item to 4th item
print("\n- Print Range of Items in Anime List -")
print(anime[1:4])

# Sort List
print("\n- Sort Anime List -")
anime.sort()
print(anime)

# Sort List in reverse order
print("\n- Sort Anime List in Reverse Order -")
anime.sort(reverse=True)
print(anime)

# Remove Specific item, e.g, remove 2nd item, index=1
print("\n- Remove specific item in Anime List -")
anime.pop(1)
print(anime)

# Remove last item => Do not enter any value as parameter in 'pop'
print("\n- Remove last item in Anime List -")
anime.pop()
print(anime)

# Change Item Value, e.g, change 3rd value in Anime List => index=2
print("\n- Change Item Value -")
anime[2] = "Demon Slayer"
print(anime)