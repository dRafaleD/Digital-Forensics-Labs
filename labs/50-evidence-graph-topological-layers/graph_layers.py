"""Synthetic partial-order graph; edges are supplied hypotheses."""
def layers(nodes, edges):
    pending=set(nodes)
    if any(a not in pending or b not in pending for a,b in edges):
        return "UNKNOWN_NODE",[]
    predecessors={n:set() for n in pending}
    for a,b in edges:
        predecessors[b].add(a)
    result=[]
    while pending:
        ready=sorted(n for n in pending if not predecessors[n]&pending)
        if not ready:
            return "CYCLE",result
        result.append(ready)
        pending.difference_update(ready)
    return "LAYERS",result

def main():
    cases=[
        (["a","b"],[("a","b")],("LAYERS",[["a"],["b"]])),
        (["a","b"],[],("LAYERS",[["a","b"]])),
        (["a","b","c"],[("a","c"),("b","c")],("LAYERS",[["a","b"],["c"]])),
        (["a","b","c"],[("a","b"),("b","c")],("LAYERS",[["a"],["b"],["c"]])),
        (["a","b"],[("a","b"),("b","a")],("CYCLE",[])),
        (["a"],[("a","a")],("CYCLE",[])),
        (["a"],[("a","x")],("UNKNOWN_NODE",[])),
        (["a","b"],[("a","b"),("a","b")],("LAYERS",[["a"],["b"]])),
        ([],[],("LAYERS",[])),
    ]
    for nodes,edges,want in cases:
        got=layers(nodes,edges)
        assert got==want,(got,want)
        print(got)
    print("9/9 graph cases passed")

if __name__=="__main__":
    main()
