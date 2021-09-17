def depreciate(currPrice,year):
    base = 106950
    temp = (base - currPrice)/year
    depPercent = (temp/base) * 100
    return depPercent
