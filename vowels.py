my_list = ['abhiram','nithanth','indragith']
for w in my_list:
    if isinstance(w, str) and w and w[0].lower() in 'aeiou':
        print(w)