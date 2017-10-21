from shutil import copyfile
from random import randint

def make_testdata():
    for i in range(500):
        copyfile(f'test_template_{randint(1, 2)}.png', f'testdata/test_{i:03}.png')

if __name__ == '__main__':
    make_testdata()

