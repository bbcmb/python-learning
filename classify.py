prices=[100,20,50,80]

expensive=0
normal=0
cheap=0

for price in prices:
    if price > 50:
        expensive += 1
    elif price == 50:
        normal += 1
    else:
        cheap += 1


print("expensive:",expensive)
print("normal:",normal)
print("cheap",cheap)
