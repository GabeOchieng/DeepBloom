from BloomFilter import BloomFilter
import mmh3
import string
import random

def get_digest(item, index):
    return mmh3.hash(bytes(item), index)

def string_digest(item, index):
    return mmh3.hash(bytes(item, 'utf-8'), index)

def generate_random_string(N):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

#### Tests
def simple_test():
    bf = BloomFilter(10000, .001, get_digest)
    for i in range(10000):
        bf.add(i)
        if not bf.check(i):
            print("False Negative!")

    count = 0.0
    fp = 0.0
    for i in range(10001, 100000):
        if bf.check(i):
            fp+=1
        count += 1

    print("False Positive Rate: " + str(fp / count))

def string_test():
    bf = BloomFilter(10000, .001, string_digest)
    for i in range(10000):
        if i % 1000 == 0:
            print("hello") 
        random_string = generate_random_string(i)
        bf.add(random_string)
        assert(bf.check(random_string))

    count = 0.0
    fp = 0.0
    for i in range(10001, 100000):
        random_string = generate_random_string(i)
        if bf.check(random_string):
            fp+=1
        count += 1

    print("False Positive Rate: " + str(fp / count))


string_test()
