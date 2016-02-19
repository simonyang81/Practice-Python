def convert(func, seq):
    'conv. sequence of numbers to same type'
    return [func(eachNum) for eachNum in seq]

myseq = [123, 45.67, -6.2e8, 99999999L]

print convert(int, myseq)
print convert(long, myseq)
print convert(float, myseq)


def net_conn(host='127.0.0.1', port=80, stype='tcp'):
    print '%s:%d [%s]' % (host, port, stype)

net_conn()
net_conn(port=8080)
net_conn(port=8089, stype='UDP')
