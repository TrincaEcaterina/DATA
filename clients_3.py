


guests_1 = [ "Bethaney Bain", "Kacey Johns", "Manpreet Saunders" ]
guests_2 = [ "Elwood Curtis", "Diya Griffin", "Kacey Johns" ]
guests_3 = [ "Tobey Weiss", "Kadie Barnes", "Diya Griffin" ]
all_guests = [*guests_1, *guests_2,*guests_3]
uniq_guests= []

# all_guests = guests_1 + guests_2 + guests_3

# all_guests = [elem for elemnts in [guests_1,guests_2,guests_3] for elem in elemnts]

for names in all_guests:
    if names not in uniq_guests:
        uniq_guests.append(names)
print(uniq_guests)


