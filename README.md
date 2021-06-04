# Bachelor Thesis Work
We have studied the effects of search algorithms on strategy synthesis with a tool that utilizes MKBSC.

The MKBSC tool was created by August Jacobsson & Helmer Nylén and can be found [here](https://github.com/HelmerNylen/mkbsc).
The original strategy synthesizer tool was created by Jakob Lycken and Simon Westerlund and can be found [here](https://github.com/JakobLycken/strategysynthesiser).

## Requirements
The required packages to run the MKBSC (and thus the entire thing) are:
- [NetworkX](https://networkx.github.io/), which can be installed via `pip3 install networkx`
- [pydot](https://github.com/erocarrera/pydot), which can be installed via `pip3 install pydot`
- [Graphviz](https://www.graphviz.org/), which can be downloaded from their website

Simply install these at the root folder.

The project is set up in such a way that you can quickly get started by `main.py` in the root folder. This will run a game we created about robots trying to tighten bolts, i.e. this: 

```python
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
```

and the program will generate strategies for it with these parameters: 
```python
Coalition_strat_synth(gamename="NK", noa=2, win_nodes="{win}", lose_nodes="{lose}", start_nodes="{start}", take_time = True, search= "")
```

The two additional parameters added in our contribution are the ``take_time`` and ``search`` which can be specified to print the time of the strategy synthesizing, and to change the search algorithm used to traverse the graph.


