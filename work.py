def get(inp, ind = [0,1,2]):
    # separate by line
    m = inp.split("\n")

    # decompose line into row vals
    rows = [x.split() for x in m]
    print(rows)

    for i in ind:
        print("\n".join([row[i] for row in rows]))
        print("\n\n")

    
def comp(inp):
    print("\n".join(inp.split()))

def dateform(inp):
    sep = inp.split()
    dates = list()
    cur = ""
    for i in range(len(sep)):
        #print(sep[i])
        if sep[i].lower() in ["monday,","tuesday,","wednesday,","thursday,","friday,","saturday,", "sunday,"]:#["january,", "february,", "march,", "april,", "may,", "june,","july,", "august,","september,", "october,","november,","december,"]:
            dates.append(cur)
            cur = sep[i]
        else:
            cur += " "
            cur += sep[i]
    dates.append(cur)
    print("\n".join(dates))

def expound(inp, key, rowlen = 3):
    """inp must be space separated rows and newline sep columns. keys must be contiguious dates"""
    keys = key.split("\n")
    inplines = inp.split("\n")
    inplines = [x.split() for x in inplines]
    datedic = dict()
    for i in inplines:
        datedic[i[0]] = i

    for key in keys:
        if key in datedic.keys():
            print(" ".join(datedic[key]))
        else:
            print(key + " 0 0")
    
