from recommender import classify, recommend

hours = 6.25

print("Category:", classify(hours))
print("Suggestion:", recommend(hours))