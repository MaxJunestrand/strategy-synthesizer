#!/usr/bin/env python3
from mkbsc import MultiplayerGame, iterate_until_isomorphic, export
from stratsynth import Coalition_strat_synth

def main():
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
        ("bad", ("switch", "lift"), "lose"), ("bad", ("switch", "lift"), "lose"),
        ("good", ("lift", "switch"), "lose"), ("good", ("lift", "lift"), "win")
    ]
    # observation partitioning
    Obs = [
        [["start"], ["bad"], ["good"], ["lose"], ["win"]],
        [["start"], ["bad", "good"], ["lose"], ["win"]]

    ]

    # G is a MultiplayerGame-object, and so are GK and GK0
    G = MultiplayerGame.create(L, L0, Sigma, Delta, Obs)
    GK = G.KBSC()
    G2K = GK.KBSC()

    G0 = G.project(0)  # (G|0)
    G1 = G.project(1)  # (G|1)


    GK0 = G0.KBSC()  # (G|0)^K
    GK1 = G1.KBSC()  # (G|1)^K

    GK0_ = GK.project(0)  # G^K|0
    GK1_ = GK.project(1)  # G^K|1


    #This would be used for G3K's agents. Something is wonky with the MKBSC
    G2K0_ = G2K.project(0)
    G2K1_ = G2K.project(1)


    G2K0 = GK0_.KBSC()  # (G^K|0)^K
    G2K1 = GK1_.KBSC()  # (G^K|1)^K

    # export the GK game to ./pictures/GK.png
    export(G, "G")
    export(GK, "GK")
    export(G2K, "G2K")

    export(GK0_, "GK0_")
    export(GK1_, "GK1_")

    export(GK0, "GK0")
    export(GK1, "GK1")

    export(G2K0, "G2K0")
    export(G2K1, "G2K1")
    export(G2K0_, "G2K0")
    export(G2K1_, "G2K1")



def mainGK():
    Coalition_strat_synth(gamename="GK", noa=2, win_nodes=["{win}", "{good}"], lose_nodes="{lose}", start_nodes="{start}")


def mainG2K():
    Coalition_strat_synth("G2K", 2, "{win-win}", "{lose-lose}", "{start-start}")

#main()

mainGK()

mainG2K()