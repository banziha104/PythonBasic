def sum(a,b):
    return a + b

def safe_sum(a,b):
    if type(a) != type(b):
        print("더할 수 없음")
        return
    else:
        print("더할 수 있음")
        result = sum(a,b)
        return result