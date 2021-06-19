def create_user(name, telephone, address):
    """Create users"""
    user = {
        'name': name,
        'phone': telephone,
        'address': address
         }
    return user
user1 = create_user("Alex", "+79271267278", "Zarechnaya")
user2 = create_user("Krestina", "+79372524600", "Zarechnaya")
print(user1)
print(user2)

def give_awards(medal, *persons):
    """Give medals to persons"""
    for person in persons:
        print("The Friend "+ person.title() + " is awarded of medal " + medal)
give_awards("Za Rodinu", "Vasya", "Petya")
give_awards("Za Stalina", "Alex", "Maks")