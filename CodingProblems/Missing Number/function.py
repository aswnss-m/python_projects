def find_missing(list_name):
    min_val = min(list_name)
    max_val = max(list_name)
    missing = list()

    for i in range(min_val,max_val):
        if i>0:
            if i not in list_name:
                missing.append(i)
            else:
                missing.append(max_val+1)
             
        else:
            continue
    try:
        return min(missing)
    except:
        return(1)
