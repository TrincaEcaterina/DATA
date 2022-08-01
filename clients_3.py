


guests_1 = [ "Bethaney Bain", "Kacey Johns", "Manpreet Saunders" ]
guests_2 = [ "Elwood Curtis", "Diya Griffin", "Kacey Johns" ]
guests_3 = [ "Tobey Weiss", "Kadie Barnes", "Diya Griffin" ]
all_guests = guests_1 + guests_2 + guests_3
uniq_guests= []


for names in all_guests:
    if names not in uniq_guests:
        uniq_guests.append(names)
        uniq_guests.sort()
        
print('\n'.join(uniq_guests))


