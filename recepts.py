f=open('рецепт.txt','r')
g=open('format.txt','w')
g.write('cook_book = {'+'\n')
line = f.readline()
while line != '':
    line = line.rstrip('\n')
    g.write('\''+line+'\': ['+'\n')
    line=f.readline()
    n=int(line)
    i=1
    while i<=n:
        line=f.readline()
        line = line.rstrip('\n')
        a = line.split('|')
        a[1]=int(a[1])
        d = dict(ingridient_name=a[0], quantity =a[1], measure = a[2])
        g.write('  '+format(d)+'\n')
        i += 1
    g.write(']')
    line=f.readline()
    if line !='':
        g.write('],\n')
    else:
        g.write(']\n')
g.write('}') 
f.close()
g.close()
