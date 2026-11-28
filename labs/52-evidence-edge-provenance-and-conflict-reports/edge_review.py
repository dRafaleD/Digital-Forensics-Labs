"""Synthetic ordering claims with explicit source provenance."""
def review(rows):
    claims={}
    for before,after,source in rows:
        if before==after or not source:
            return "INVALID_CLAIM",[]
        claims.setdefault((before,after),set()).add(source)
    conflicts=[]
    for a,b in sorted(claims):
        if a<b and (b,a) in claims:
            conflicts.append((a,b,sorted(claims[a,b]),sorted(claims[b,a])))
    return ("CONFLICT" if conflicts else "NO_DIRECT_CONFLICT"),conflicts

def main():
    cases=[
        ([],("NO_DIRECT_CONFLICT",[])),
        ([("a","b","s1")],("NO_DIRECT_CONFLICT",[])),
        ([("a","a","s1")],("INVALID_CLAIM",[])),
        ([("a","b","")],("INVALID_CLAIM",[])),
        ([("a","b","s1"),("a","b","s1")],("NO_DIRECT_CONFLICT",[])),
        ([("a","b","s1"),("b","a","s2")],
         ("CONFLICT",[("a","b",["s1"],["s2"])])),
        ([("b","a","s2"),("a","b","s1"),("a","b","s3")],
         ("CONFLICT",[("a","b",["s1","s3"],["s2"])])),
        ([("a","b","s1"),("b","c","s2"),("c","a","s3")],
         ("NO_DIRECT_CONFLICT",[])),
    ]
    for rows,want in cases:
        got=review(rows)
        assert got==want,(got,want)
        print(got)
    print("8/8 claim review cases passed")

if __name__=="__main__":
    main()
