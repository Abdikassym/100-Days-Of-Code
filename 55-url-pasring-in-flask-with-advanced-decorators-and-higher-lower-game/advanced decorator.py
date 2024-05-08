class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = True


def is_logged_in_decorator(function):  # 3. Create a decorator
    def wrapper(*args, **kwargs):  # 6. There can be any arguments, so we use *args. args* = [user]
        if args[0].is_logged_in:  # 5. this line equals "if user.is_logged_in:". But since there is no user, we must
                                  # define it, by defining it in 8th line.
            function(args[0])
    return wrapper


@is_logged_in_decorator  # 4. apply decorator to function
def create_blogpost(user):
    print(f"This is {user.name}'s new blogpost!")


new_user = User("pixu")  # 1. Create an object with name = pixu
create_blogpost(new_user)  # 2. Call the func, get this is pixu's new blogpost.


