full_name = 'Leonardo DiCaprio'
len_full_name = len(full_name)
print(len_full_name)
full_name_new = full_name.replace('Leonardo DiCaprio ', 'Leonid DiCaprio')
index = full_name.index('')
full_name_new_2 = 'Eli Cohen'
first_name = full_name[0:index]
first_name = full_name[index:len_full_name]
print(f'first_name: {first_name} last_name is {full_name}')
random_name = full_name[1:6]
count_from_last = full_name[-5:]
print(full_name_new)
