# decorator
def main(func):
    def subMain():
        print('1')
        func()
        print('3')
    
    return subMain()


def sub():
    print('2')

main(sub) # use directly

# use as decorator
@main
def sub2():
    print('5')