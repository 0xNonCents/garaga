from tools.py.bn128_field import FQ2

def bin_c(u):
    b=bin(u)
    f = b[0:10] + ' ' + b[10:19] + '...' + b[-16:-8] + ' ' + b[-8:]
    return f

def bin_64(u):
    b=bin(u)
    little = '0b'+b[2:][::-1]
    f='0b'+' '.join([b[2:][i:i+64] for i in range(0, len(b[2:]), 64)])
    return f
def bin_8(u):
    b=bin(u)
    little = '0b'+b[2:][::-1]
    f="0b"+' '.join([little[2:][i:i+8] for i in range(0, len(little[2:]), 8)])
    return f

def print_u_256_info(u, un):
    u = u.low + (u.high << 128) 
    print(f" {un}_{u.bit_length()}bits = {bin_c(u)}")
    print(f" {un} = {u}")
def print_affine_info(p, pn):
    print(f"Affine Point {pn}")
    print_u_256_info(p.x, 'X')
    print_u_256_info(p.y, 'Y')

def print_felt_info(u, un):
    print(f" {un}_{u.bit_length()}bits = {bin_8(u)}")
    print(f" {un} = {u}")
    # print(f" {un} = {int.to_bytes(u, 12, 'big')}")

def print_u_512_info(u, un):
    u = u.d0 + (u.d1 << 128) + (u.d2<<256) + (u.d3<<384) 
    print(f" {un}_{u.bit_length()}bits = {bin_64(u)}")
    print(f" {un} = {u}")
def print_u_512_info_u(l, h, un):
    u = l.low + (l.high << 128) + (h.low<<256) + (h.high<<384) 
    print(f" {un}_{u.bit_length()}bits = {bin_64(u)}")
    print(f" {un} = {u}")

def print_u_256_neg(u, un):
    u = 2**256 - (u.low + (u.high << 128))
    print(f"-{un}_{u.bit_length()}bits = {bin_c(u)}")
    print(f"-{un} = {u}")

def print_sub(a, an, b, bn, res, resn):
    print (f"----------------Subbing {resn} = {an} - {bn}------------------")
    print_u_256_info(a, an)
    print('\n')

    print_u_256_info(b, bn)
    print_u_256_neg(b, bn)
    print('\n')

    print_u_256_info(res, resn)
    print ('---------------------------------------------------------')


def split(num: int, num_bits_shift: int = 128, length: int = 2):
    a = []
    for _ in range(length):
        a.append(num & ((1 << num_bits_shift) - 1))
        num = num >> num_bits_shift
    return tuple(a)


def splitFQP(fqp: FQ2, num_bits_shift: int = 128, length: int = 2):
    
    outer = []
    a = []

    for q in range(0,len(fqp.coeffs)):
        for _ in range(length):
            a.append(fqp.coeffs[q].n & ((1 << num_bits_shift) - 1))
            fqp.coeffs[q].n = fqp.coeffs[q].n >> num_bits_shift
        outer.append(a)
        a = []
    return outer


