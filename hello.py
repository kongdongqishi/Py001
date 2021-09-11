def main():
    if __name__ == "__main__":
        print("hello.py is being run directly")
    else:
        print("hello.py is being imported into annother module")
# 此时是进行独立调用，因此__name__显示为__main__，显示的结果为hello.py is being run directly
main()
# 此时进行模块的调用，调用模块的时候，也调用了里面的函数，因此__name__的值为__hello__，显示的结果为hello.py is being imported into annother module
from hello import main


