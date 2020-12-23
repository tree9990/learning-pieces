
def debug(func):
    def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
        print ("[DEBUG]: enter {}()".format(func.__name__))
        print ('Prepare and say...',)
        a=args
        b=kwargs
        print(a,b)
        return func(*args, **kwargs)
    return wrapper  # 返回

@debug
def say(*some, **something):
    print ("hello {}!".format(something))

def main():
    ddd={"aaa":333, "bbb":555}
    say(*ddd, fff=7890)

if __name__=="__main__":
    main()
