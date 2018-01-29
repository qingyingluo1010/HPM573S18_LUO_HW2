

import HUI3 as eq

print("Score for ", [2, 1, 1, 2, 1, 2, 1, 3])
print(eq.get_score(vision=2, hearing=1, speech=1, ambulation=2, dexterity=1, emotion=2, cognition=1, pain=3))

print("Score for ", [2, 1, 1, 2, 1, 2, 1, 6])
print(eq.get_score(vision=2, hearing=1, speech=1, ambulation=2, dexterity=1, emotion=2, cognition=1, pain=6))

