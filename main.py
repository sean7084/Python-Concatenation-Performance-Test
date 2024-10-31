import timeit

def method_plus_single():
    var1 = 'alpha'
    var2 = 'bravo, charlie'
    return var1 + var2

def method2_join_single():
    var1 = 'alpha'
    names1 = [var1, 'bravo, charlie']
    return ', '.join(names1)

def method_fstring_single():
    var1 = 'alpha'
    return (f"{var1}, bravo, charlie")

def method_format_single():
    var1 = 'alpha'
    return ("{}, bravo, charlie".format(var1))

print(timeit.timeit(method_plus_single, number= 10000000))
print(timeit.timeit(method2_join_single, number= 10000000))
print(timeit.timeit(method_fstring_single, number= 10000000))
print(timeit.timeit(method_format_single, number= 10000000))

def method_plus_9():
    var1 = 'alpha'
    var2 = 'bravo'
    var3 = 'charlie'
    var4 = 'delta'
    var5 = 'echo'
    var6 = 'foxtrot'
    var7 = 'golf'
    var8 = 'hotel'
    var9 = 'india'
    return var1 + ' ,' + var2 + ' ,' + var3 + ' ,' + var4 + ' ,' + var5 + ' ,' + var6 + ' ,' + var7 + ' ,' + var8 + ' ,' + var9 + ' ,' + 'juliet'

def method2_join_9():
    var1 = 'alpha'
    var2 = 'bravo'
    var3 = 'charlie'
    var4 = 'delta'
    var5 = 'echo'
    var6 = 'foxtrot'
    var7 = 'golf'
    var8 = 'hotel'
    var9 = 'india'
    names1 = [var1, var2, var3, var4, var5, var6, var7, var8, var9, 'juliet']
    return ', '.join(names1)

def method_fstring_9():
    var1 = 'alpha'
    var2 = 'bravo'
    var3 = 'charlie'
    var4 = 'delta'
    var5 = 'echo'
    var6 = 'foxtrot'
    var7 = 'golf'
    var8 = 'hotel'
    var9 = 'india'
    return (f"{var1}, {var2}, {var3}, {var4}, {var5}, {var6}, {var7}, {var8}, {var9}, 'juliet'")

def method_format_9():
    var1 = 'alpha'
    var2 = 'bravo'
    var3 = 'charlie'
    var4 = 'delta'
    var5 = 'echo'
    var6 = 'foxtrot'
    var7 = 'golf'
    var8 = 'hotel'
    var9 = 'india'
    return ("{}, {}, {}, {}, {}, {}, {}, {}, {}, juliet".format(var1, var2, var3, var4, var5, var6, var7, var8, var9))

print(timeit.timeit(method_plus_9, number= 10000000))
print(timeit.timeit(method2_join_9, number= 10000000))
print(timeit.timeit(method_fstring_9, number= 10000000))
print(timeit.timeit(method_format_9, number= 10000000))