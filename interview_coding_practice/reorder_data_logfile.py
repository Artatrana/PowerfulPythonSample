# Re-order data of a log file. Order the alphabeticall order, 

def reorderLogFiles(logs: list[str]) -> list[str] :

    # define the numberic and alpha emtry list
    res1, res2 = [], []

    # Iterate though the logs
    for log in logs:
        if (log.split()[1]).isdigit():
            res2.append(log)
        else:
            res1.append(log)

    res1 = res1.sort(key = lambda x: x[0])
    res1 = res1.sort(key = lambda x: x[1:])
    
    for i in range(len(res1)):
        res1[i] = (" ".join(res1[i]))
    
    res1.extend(res2)
    return res1

