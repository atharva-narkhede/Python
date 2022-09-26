import cmath


def area_circle(r):
    area = cmath.pi*r*r
    print('Area of circle: ', round(area, 2), 'sq. units')


n = int(input("Enter radius: "))
area_circle(n)
