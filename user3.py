from user_class import User

def main():
    user = User()
    a=user.PUT("key1", "value1")
    print(a)
    b=user.PUT("key1", "value2")
    print(b)
    c=user.READ("key1")
    print(c)
    d=user.GET("key1")
    print(d)
    e=user.READ("key1")
    print(e)
    print("read a value from our client_1 file's key")
    f=user.READ("lobularia")
    print(f)


if __name__ == "__main__":
    main()    
