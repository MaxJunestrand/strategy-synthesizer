'''
Ändrad: 2020-03-16
Smiskar ut massor av olika KBSCs. Läs längst ned vilka

'''


from mkbsc import MultiplayerGame, export, iterate_until_isomorphic

#states
L = ["Start", "1", "2", "3", "4", "Lose", "Lose2", "Win"]
#initial state
L0 = "Start"
#action alphabet
Sigma = (("a", "b"), ("a, b"))
#action labeled transitions
Delta = [
    ("Start", ("a", "a"), "1"), ("Start", ("b", "b"), "2"),("Start", ("a", "b"), "Start"),("Start", ("b", "a"), "Start"),
    ("1", ..., "3"),
    ("2", ("b", "b"), "3"), ("2", ("a", "a"), "Lose2"),("2", ("b", "a"), "2"),("2", ("a", "b"), "2"),
    ("Lose2", ("a","a"),"4"),("Lose2", ("b","a"),"Lose2"),("Lose2", ("a","b"),"Lose2"),("Lose2", ("b","b"),"Lose2"),
    ("3", ("a", "b"), {"Lose", "4"}), ("3", ("b", "a"), "3"),("3", ("a", "a"), "3"),("3", ("b", "b"), "3"),
    ("4", ..., "Win"),
    ("Win", ..., "Win")
]
#observation partitioning
Obs = [
    [["1"],["2"], ["Win"], ["Start"], ["3"],["4"],["Lose"],["Lose2"]],
    [["1"],["2"], ["Win"], ["Start"], ["3"],["4"],["Lose"],["Lose2"]]
]

#G is a MultiplayerGame-object, and so are GK and GK0
G = MultiplayerGame.create(L, L0, Sigma, Delta, Obs)
GK = G.KBSC()
GK0 = GK.project(0)

G0 = G.project(0)
G0K = G0.KBSC()
G1 = G.project(1)
G1K = G1.KBSC()
gamename = "as2"


#export the GK game to ./pictures/GK.png
export(G, gamename, view=False) # Multiplayer game
export(GK, gamename+"K") # Multiplayer KBSC

#export(G0, gamename+"0",view=False) # Agent 0 singleplayer game
#xport(GK0, gamename+"K0",view=False) # Agent 0 multiplayer KBSC
export(G0K, gamename+"K0") # Agent 0 singleplayer KBSC
export(G1K, gamename+"K1") # Agent 0 singleplayer KBSC