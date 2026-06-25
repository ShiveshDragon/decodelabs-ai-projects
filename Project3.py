# AI Recommendation System

# Item database
items = {
    "Interstellar": ["sci-fi", "space", "adventure"],
    "Inception": ["sci-fi", "thriller", "action"],
    "The Dark Knight": ["action", "crime", "thriller"],
    "John Wick": ["action", "crime"],
    "The Conjuring": ["horror", "thriller"],
    "Friends": ["comedy", "drama"],
    "Breaking Bad": ["crime", "drama"],
    "Stranger Things": ["sci-fi", "thriller", "adventure"]
}

print("Available interests:")
print("sci-fi, action, thriller, comedy, horror, drama, crime, adventure, space")

# User input
user_input = input("\nEnter your interests separated by commas: ")

# Convert input into a clean list
user_preferences = [
    interest.strip().lower()
    for interest in user_input.split(",")
]

recommendations = []

# Similarity matching
for item, tags in items.items():
    score = 0
    for preference in user_preferences:
        if preference in tags:
            score += 1

    if score > 0:
        recommendations.append((item, score))

# Sort by highest similarity
recommendations.sort(key=lambda x: x[1], reverse=True)

# Display results
if recommendations:
    print("\nRecommended for you:\n")

    for item, score in recommendations:
        print(f"{item}  | Match Score: {score}")

else:
    print("\nNo matching recommendations found.")