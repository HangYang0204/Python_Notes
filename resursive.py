def _countdown_(n):
    if n < 0:
        print('blast off!')
    else:
        print(n)
        countdown(n-1)
k = int(input('enter number you want to countdown: '))
_countdown_(k)

t = input('enter string you want to repeat: ')
num = int(input('enter number of times it will show: '))
def _print_(s,n):
    if n < 0:
        return
    print(s)
    _print_(s,n-1)

_print_(t,num)
