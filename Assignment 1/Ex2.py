import numpy as np

def playRound():
    # 0: Cherry, 1: Lemon, 2: Bell, 3: Bar
    w1, w2, w3 = np.random.randint(0, 4, 3)
    
    if w1 == 3 and w2 == 3 and w3 == 3: return 20 # Bar
    if w1 == 2 and w2 == 2 and w3 == 2: return 15 # Bell
    if w1 == 1 and w2 == 1 and w3 == 1: return 5  # Lemon
    if w1 == 0 and w2 == 0 and w3 == 0: return 3  # 3 Cherry
    if w1 == 0 and w2 == 0: return 2              # 2 Cherry
    if w1 == 0: return 1                          # 1 Cherry
    return 0

def simulateGame(startCoins=10, nSims=50000):
    playsList = []
    for _ in range(nSims):
        coins = startCoins
        plays = 0
        while coins > 0:
            coins -= 1
            win = playRound()
            coins += win
            plays += 1
        playsList.append(plays)
    return np.mean(playsList), np.median(playsList)

meanPlays, medianPlays = simulateGame()
print(f"Mean: {meanPlays}, Median: {medianPlays}")