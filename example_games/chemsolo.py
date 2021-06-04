from stratsynth import Coalition_strat_synth

def main():
    Coalition_strat_synth(gamename="as2K", noa=2, win_nodes="{Win}", lose_nodes=["{Lose}", "{Lose2}"], start_nodes="{Start}")
    #Coalition_strat_synth("G2K", 2, "{win-win}", "{lose-lose}", "{start-start}")


main()