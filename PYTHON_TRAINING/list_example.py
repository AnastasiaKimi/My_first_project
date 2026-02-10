names = ['Efrat', 'Vered', 'Max']
grades = [90, 80, 70]
cities = ['Lod','Paris','Dubai']
cities.insert(4,'Haifa')
cities.remove("Haifa")
cities[2:4]

for name in names:
    print(name)
    l = len(name)
    print (f"the len of {name} is {l}")

    city_index_1=cities [1]
    length_of_list=len(cities)
    lod_counter=cities.count('Lod')
    is_Paris="Paris" in cities
    is_Rishon="Rishon" in cities

    print(f"is_Rishon? {is_Rishon}")
    print (f"is_Paris{is_Paris}")