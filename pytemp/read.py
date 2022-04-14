with open('temp.txt') as f:
    lines = f.readlines()
i = 1
#np.array([43, 53, 97])
for x in lines: 
     word = x.split(',')
     print(f'p{i} = ' +'np.array' + '([' +word[0]+', ' +word[1]+' ,'+word[2].replace('\n','')+ '])') 
     i = i + 1
