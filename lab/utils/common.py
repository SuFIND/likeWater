def getValueWithDefault(aMap, key, defaultVal=None):
    v = aMap.get(key, defaultVal)
    if v is None:
        v = defaultVal
    return v
