"""Construct definite ordering edges from fictional closed time intervals."""
from dataclasses import dataclass
from itertools import permutations

@dataclass(frozen=True)
class Event:
    ident: str
    earliest: int
    latest: int

def edges(events):
    if len({e.ident for e in events})!=len(events):
        raise ValueError("duplicate identity")
    if any(e.earliest>e.latest for e in events):
        raise ValueError("invalid interval")
    return {(a.ident,b.ident) for a,b in permutations(events,2)
            if a.latest<b.earliest}

def main():
    a,b,c,d = (Event("A",0,2),Event("B",1,4),
               Event("C",5,7),Event("D",7,9))
    graph=edges([a,b,c,d])
    assert graph=={("A","C"),("A","D"),("B","C"),("B","D")}
    assert ("A","B") not in graph
    assert ("C","D") not in graph
    assert edges([d,c,b,a])==graph
    assert edges([])==set()
    assert edges([a])==set()
    assert edges([Event("X",1,1),Event("Y",2,2)])=={("X","Y")}
    for bad in ([a,a],[Event("bad",5,4)]):
        try:
            edges(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid input accepted")
    for x,y in sorted(graph):
        print(x,"definitely before",y)
    print("9 partial-order checks passed")

if __name__=="__main__":
    main()
