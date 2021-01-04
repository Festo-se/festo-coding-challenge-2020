import datetime

def division( n, k ):
  while n % k == 0:
    n = n / k
  return n

def ugly( n ):
  n = division(n, 7)
  n = division(n, 11)
  n = division(n, 13)
  return True if n == 1 else False

def nthUgly( n ):
  i = 1
  count = 1
  while n > count:
    i += 1
    if ugly(i):
      # as we approach the 200th room, this gets really sloooooow \_(ツ)_/¯
      print('{}: found ugly number: {}'.format(datetime.datetime.utcnow(), i))
      print('count: {}'.format(count))
      count += 1
  return i

n=200
print(nthUgly(n))
