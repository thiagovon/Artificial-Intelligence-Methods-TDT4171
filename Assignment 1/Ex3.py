import numpy as np

# Exercise 3 Part 1 

def simulateBirthdayProb(nPeople, nSims=10000):
    birthdays = np.random.randint(0, 365, size=(nSims, nPeople))
    
    birthdays.sort(axis=1)
    
    hasDuplicate = (birthdays[:, 1:] == birthdays[:, :-1]).any(axis=1)
    
    return np.mean(hasDuplicate)

nRange = range(10, 51) 
results = {}

print("Running simulation for Part 1...")
for n in nRange:
    results[n] = simulateBirthdayProb(n)

probs = np.array(list(results.values()))
nValues = np.array(list(results.keys()))

countGe50 = np.sum(probs >= 0.5)
totalN = len(nValues)
proportion = countGe50 / totalN

indicesGe50 = np.where(probs >= 0.5)[0]
smallestN = nValues[indicesGe50[0]] if len(indicesGe50) > 0 else None

print("Part 1 Results:")
print(f"Smallest N for >= 50%: {smallestN}")
print(f"Proportion of N in [10, 50] with >= 50% chance: {proportion:.4f} ({countGe50}/{totalN})")


# Exercise 3, Part 2 

def simulateFullCollection():
    daysCovered = set()
    groupSize = 0
    while len(daysCovered) < 365:
        newBirthday = np.random.randint(0, 365)
        daysCovered.add(newBirthday)
        groupSize += 1
    return groupSize

print("\nRunning simulation for Part 2 (this may take a moment)...")
nSimsPart2 = 1000 
collectionSizes = [simulateFullCollection() for _ in range(nSimsPart2)]
expectedGroupSize = np.mean(collectionSizes)

print("Part 2 Results:")
print(f"Expected group size to cover all birthdays: {expectedGroupSize:.2f}")