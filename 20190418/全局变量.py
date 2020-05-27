g_num= int(input())
g_bool = "False"
def mod_global_var(g_num):
    global g_bool
    if g_num%2:
        g_bool = "True"
    else:
        g_bool = "False"
    return g_bool
mod_global_var(g_num)
print(g_bool)