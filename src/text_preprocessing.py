def process(input,max):
    data = []
    #max = 500
    lines = input.splitlines()
    for line in lines:
        if len(line) <= max:
            data.append(line+"\n")
        else:
            #comma,semicolon & period preprocessing
            line = line.replace(". ", ".")
            line = line.replace(";", ",")
            line = line.replace(", ", ",")
            #period-based breakdown
            sentences = line.split(".")
            for snt in sentences:
                if len(snt) <= max:
                    data.append(snt)
                else:
                    #comma-based breakdown
                    halves = snt.split(",")
                    for hv in halves:
                        if len(hv) <= max:
                            data.append(hv)
                        else:#last resort (individual words)
                            words = hv.split()
                            phrase = ""
                            if len(words) != 0:
                                for w in words:
                                    if len(phrase+w) > max:
                                        data.append(phrase)
                                        phrase = ""
                                    else:
                                        phrase += w
                                data.append(phrase)
    result = []
    cell = ""
    for chunk in data:
        if len(cell+chunk) > max:
            result.append(cell)
            cell = chunk
        else:
            cell += chunk
    result.append(cell)
    return result