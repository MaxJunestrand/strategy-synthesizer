from mkbsc import MultiplayerGame, export, iterate_until_isomorphic
from stratsynth import Coalition_strat_synth

"""
Game of robots lifting cans of acid onto a conveyor belt.
"""

# states
L = ["start", "bad", "good", "lose", "win"]
# initial state
L0 = "start"
# action alphabet
Sigma = (("grab", "lift", "switch"), ("grab", "lift", "switch"))
# action labeled transitions
Delta = [
    ("start", ("grab", "grab"), "bad"), ("start", ("grab", "grab"), "good"),
    ("bad", ("switch", "switch"), "good"), ("good", ("switch", "switch"), "good"),
    ("bad", ("lift", "lift"), "lose"), ("bad", ("lift", "switch"), "lose"),
    ("bad", ("switch", "lift"), "lose"), ("good", ("switch", "lift"), "lose"),
    ("good", ("lift", "switch"), "lose"), ("good", ("lift", "lift"), "lose"),
]
# observation partitioning
Obs = [
    [["start"], ["bad"], ["good"], ["lose"], ["win"]],
    [["start"], ["bad", "good"], ["lose"], ["win"]]
]




"""
Game of robots choosing and bolting with different bolts
"""

# states
LN = ["start", "bad bolt", "good bolt", "lose", "fully tightened", "loosely tightened", "win"]
# initial state
LN0 = "start"
# action alphabet
SigmaN = (("take", "tighten", "next"), ("take", "tighten", "next"))
# action labeled transitions
DeltaN = [
    ("start", ("take", "take"), "good bolt"), ("start", ("take", "take"), "bad bolt"),
    
    ("good bolt", ("take", "take"), "good bolt"), ("bad bolt", ("take", "take"), "good bolt"),
    ("good bolt", ("tighten", "tighten"), "fully tightened"),("good bolt", ("tighten", "tighten"), "loosely tightened"),
    
    ("bad bolt", ("tighten", "tighten"), "lose"), ("bad bolt", ("tighten", "take"), "lose"),
    ("bad bolt", ("take", "tighten"), "lose"), 
    
    ("fully tightened", ("take", "tighten"), "lose"), ("fully tightened", ("next", "next"), "win"),
    ("fully tightened", ("tighten", "take"), "lose"), ("fully tightened", ("tighten", "tighten"), "fully tightened"), 
    
    ("loosely tightened", ("take", "tighten"), "lose"), ("loosely tightened", ("tighten", "tighten"), "fully tightened"),
    ("loosely tightened", ("take", "tighten"), "lose"), ("loosely tightened", ("next", "next"), "lose")
]
# observation partitioning
ObsN = [
    [["start"], ["good bolt", "bad bolt"], ["lose"], ["win"], ["fully tightened"], ["loosely tightened"]],
    [["start"], ["good bolt"], ["bad bolt"], ["lose"], ["win"], ["fully tightened", "loosely tightened"]]
]

#N is a MultiplayerGame-object
N = MultiplayerGame.create(LN, LN0, SigmaN, DeltaN, ObsN)
NK = N.KBSC() # (G)^K
N2K = NK.KBSC() # (G)^2K


# takes each agent from game G
N0 = N.project(0)  # (G|0)
N1 = N.project(1)  # (G|1)

# applies the KBSC to each agent's game
NK0 = N0.KBSC()  # (G|0)^K
NK1 = N1.KBSC()  # (G|1)^K

#G is a MultiplayerGame-object
G = MultiplayerGame.create(L, L0, Sigma, Delta, Obs)
GK = G.KBSC() # (G)^K
G2K = GK.KBSC() # (G)^2K


# takes each agent from game G
G0 = G.project(0)  # (G|0)
G1 = G.project(1)  # (G|1)

# applies the KBSC to each agent's game
GK0 = G0.KBSC()  # (G|0)^K
GK1 = G1.KBSC()  # (G|1)^K


# export the game to ./pictures/
#export(N, "N")
#export(NK, "NK")

#export(NK0, "NK0")
#export(NK1, "NK1")


#game = Coalition_strat_synth(gamename="GK", noa=2, win_nodes="{win}", lose_nodes="{lose}", start_nodes="{start}", take_time = True, search= "backwards")
#game.start_test()


game = Coalition_strat_synth(gamename="NK", noa=2, win_nodes="{win}", lose_nodes="{lose}", start_nodes="{start}", take_time = True, search= "")
game.start_test()


# takes each agent's game from the expanded game GK
GK0_ = GK.project(0)  # G^K|0
GK1_ = GK.project(1)  # G^K|1


#This would be used for G3K's agents. Something is wonky with the MKBSC
#G2K0_ = G2K.project(0)
#G2K1_ = G2K.project(1)


G2K0 = GK0_.KBSC()  # (G^K|0)^K
G2K1 = GK1_.KBSC()  # (G^K|1)^K

# export the GK game to ./pictures/GK.png
export(G2K, "G2K")

export(GK0_, "GK0_")
export(GK1_, "GK1_")

export(G2K0, "G2K0")
export(G2K1, "G2K1")

# exporting for G3K's agents. Not used in this iteration.
#export(G2K0_, "G2K0")
#export(G2K1_, "G2K1")

#game = Coalition_strat_synth("G2K", 2, "{win-win}", "{lose-lose}", "{start-start}")
#game.start_test()

#cont below for multiple KBSC-applications
