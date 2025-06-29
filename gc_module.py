import gc

print(gc.isenabled()) #true by default
gc.disable()
print(gc.isenabled())   # false
gc.enable()
print(gc.isenabled())   # true