from math import sin, atan, sqrt
from plot import plot


def linear(x1, y1, x2, y2):
    #	xstart,ystart=send(x,y)
    n = 100
    slope = (y2 - y1) / (x2 - x1)
    xarray = [x1 + ( x2 - x1 )* i / n for i in range(n)]
    yarray = [y1 + ( y2 - y1 )* i / n for i in range(n)]
    # print(xarray)
    return (xarray, yarray)


def concave(x1, y1, x2, y2):
    n = 10000
    slope = (y2 - y1) / (x2 - x1)

    longer = max(abs(y2 - y1), abs(x2 - x1))
    shorter = min(abs(y2 - y1), abs(x2 - x1))
    r = longer / (sin(2 * atan(longer / shorter)))
    rx = 0.0
    ry = 0.0
    if(slope < 0):
        if(longer == abs(y2 - y1)):
            rx = x1 + r
            ry = y1
        else:
            rx = x2
            ry = y2 + r
    else:
        if(longer == abs(y2 - y1)):
            rx = x2 - r
            ry = y2
        else:
            rx = x1
            ry = y1 + r

    xarray = [x1 + i * (x2 - x1) / n for i in range(n)]
    yarray = [ry - sqrt(r * r - (xarray[i] - rx)**2) for i in range(n)]
    return (xarray, yarray)
    # plot(xarray, yarray)


def convex(x1, y1, x2, y2):
    n = 10000
    slope = (y2 - y1) / (x2 - x1)
    longer = max(abs(y2 - y1), abs(x2 - x1))
    shorter = min(abs(y2 - y1), abs(x2 - x1))
    r = longer / (sin(2 * atan(longer / shorter)))
    rx = 0.0
    ry = 0.0
    # print(longer, abs(y2 - y1))
    if(slope < 0):
        if(longer == abs(y2 - y1)):
            rx = x2 - r
            ry = y2
        else:
            rx = x1
            ry = y1 - r
    else:
        if(longer == abs(y2 - y1)):
            rx = x1 + r
            ry = y1
        else:
            rx = x2
            ry = y2 - r

    xarray = [x1 + i * (x2 - x1) / n for i in range(n)]
    # print(x1, y1, x2, y2, longer, shorter, r, rx, ry)
    yarray = [ry + sqrt(r * r - (xarray[i] - rx)**2) for i in range(n)]
    # plot(xarray, yarray)
    return (xarray, yarray)


def main():
	"""
	More like a test_function rather than main :p
	"""
	(x,y) = concave(1.0, 4.0, 4.0, 1.0)
	plot(x,y)
	convex(1.0, 4.0, 4.0, 1.0)

	concave(1.0, 1.0, 4.0, 4.0)
	convex(1.0, 1.0, 4.0, 4.0)

if __name__ == "__main__":
    main()
