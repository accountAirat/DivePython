import argparse
from Matrix import Matrix

parser = argparse.ArgumentParser(description='Class Matrix')
parser.add_argument('-one', metavar='one', type=str, help='enter Matrix')
parser.add_argument('-two', metavar='two', type=str, help='enter Matrix')
parser.add_argument('-w', metavar='width', type=int, help='enter width', default=5)
parser.add_argument('-l', metavar='height', type=int, help='enter height', default=5)
parser.add_argument('-r', action='append_const', const=2, dest='filling', default=[2])
parser.add_argument('-c', action='append_const', const=1, dest='filling')
parser.add_argument('-z', action='append_const', const=3, dest='filling')
parser.add_argument('-s', action='store_true')
parser.add_argument('-m', action='store_true')

args = parser.parse_args()
fill = args.filling[-1]

if args.one:
    print(m := eval(args.one))
else:
    print(m := Matrix(width=args.w, height=args.l, filling=fill))

if args.two:
    print(n := eval(args.two))
else:
    print(n := Matrix(width=args.w, height=args.l, filling=fill))

if args.s:
    print(m + n)
elif args.m:
    print(m * n)

'''
python3 main.py -m -one "Matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 5, 5)"
'''
