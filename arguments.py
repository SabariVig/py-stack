import argparse
import sys


class circle:
    def __init__(self,x):
        self.radius = x
        self.pi = 3.14

    def area_circle(self):
        area = self.pi*self . radius ** self.radius
        print("Area Of Circle is ",area)



def main():
    parser = argparse.ArgumentParser(description="Prints The Radius Of The Circle")
    parser.add_argument('-r', '--radius', type=int, required=True , default = 5)
    arg=parser.parse_args()
    c = circle(arg.radius)
    c.area_circle()



if __name__ == '__main__':
    main()




