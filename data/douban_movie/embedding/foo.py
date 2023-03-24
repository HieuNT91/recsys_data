f = open('user.embedding_64', 'r')
f1 = open('item.embedding_64', 'r')

with open('foo_all.tsv', 'w') as of, open('foo_all_meta.tsv', 'w') as metaof:
    metaof.write('User/Movie\n')
    for line in f.readlines():
        emb = line.strip().split()
        emb = emb[1:]
        s = ''
        for e in emb:
            s += str(e)
            s += '\t'
        of.write(s)
        of.write('\n')
        metaof.write('User\n')
    
    for line in f1.readlines():
        emb = line.strip().split()[1:]
        s = ''
        for e in emb:
            s += str(e)
            s += '\t'
        of.write(s)
        of.write('\n')
        metaof.write('Movie\n')


