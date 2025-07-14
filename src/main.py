import sys
from guest import Guest
from user import User
from solution import greet


def main():
    guest = Guest()
    print(greet(guest))

    user = User('Tota')
    print(greet(user))
    return 0


if __name__ == "__main__":
    sys.exit(main())
