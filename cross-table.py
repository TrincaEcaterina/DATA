
# CROSS TABLE / cars consumtions

consum = [
    # L/100km
    #10-20km/h       50-60km/h      100-120km/h
    [2.0,              3.0,          4.0 ,         5.0],     # 1.2l
    [3.0,              5.0,          6.0 ,        7.0 ],     # 2.0l
    [10.0,             15.0,        20.0,        22.0 ]      # 8.0l
]
# HW : 4th colum 150-200km/h
col_lables =[ '10-20km/h', '50-60km/h', '100-120km/h', '150-200km/h']
row_lables =[ '1.2l', '2.0l','8.0l','10.l']

# PRINTS HEADER
print(end="    ")
for ci in range(len(consum[0])):
    print(f'|{col_lables[ci]:>12}|', end="")

print()
# PRINTS HEADER


for ri in range(len(consum)):
    print (row_lables[ri],end="")

    # prints one raw
    for ci in range(len(consum[0])):
        print(f"|{consum[ri][ci]:>12.1f}|", end="")
    print()
    # prints one raw
