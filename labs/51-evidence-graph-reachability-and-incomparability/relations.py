"""Compare order hypotheses in a small synthetic evidence graph."""
def reachable(start,target,edges):
    todo=[start]
    seen={start}
    while todo:
        node=todo.pop()
        for a,b in edges:
            if a==node:
                if b==target:
                    return True
                if b not in seen:
                    seen.add(b)
                    todo.append(b)
    return False

def relation(a,b,nodes,edges):
    if a not in nodes or b not in nodes:
        return "UNKNOWN"
    if any(x not in nodes or y not in nodes for x,y in edges):
        return "INVALID_GRAPH"
    if any(reachable(n,n,edges) for n in nodes):
        return "CYCLE"
    if a==b:
        return "SAME_NODE"
    if reachable(a,b,edges):
        return "BEFORE"
    if reachable(b,a,edges):
        return "AFTER"
    return "INCOMPARABLE"

def main():
    nodes={"a","b","c","d"}
    edges=[("a","b"),("b","d"),("a","c")]
    cases=[
        ("a","d",edges,"BEFORE"),("d","a",edges,"AFTER"),
        ("b","c",edges,"INCOMPARABLE"),("c","d",edges,"INCOMPARABLE"),
        ("a","a",edges,"SAME_NODE"),("a","x",edges,"UNKNOWN"),
        ("a","d",edges+[("d","a")],"CYCLE"),
        ("a","d",edges+[("a","x")],"INVALID_GRAPH"),
        ("a","d",[],"INCOMPARABLE"),
    ]
    for a,b,e,want in cases:
        got=relation(a,b,nodes,e)
        assert got==want,(a,b,got)
        print(a,b,got)
    print("9/9 graph relation cases passed")

if __name__=="__main__":
    main()
