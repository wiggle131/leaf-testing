import numpy as np

p1 = np.array([9,  77 , 80])
p2 = np.array([29,  67 , 69])
p3 = np.array([46,  66 , 61])
p4 = np.array([63,  70 , 53])
p5 = np.array([79,  83 , 46])
p6 = np.array([85,  78 , 53])
p7 = np.array([77,  72 , 58])
p8 = np.array([70,  66 , 63])
p9 = np.array([66,  63 , 66])
p10 = np.array([64,  62 , 68])
p11 = np.array([62,  61 , 70])
p12 = np.array([58,  60 , 72])
p13 = np.array([53,  60 , 73])
p14 = np.array([50,  57 , 74])
p15 = np.array([48,  59 , 78])
p16 = np.array([45,  60 , 79])
p17 = np.array([42,  59 , 81])
p18 = np.array([39,  60 , 83])
p19 = np.array([36,  60 , 84])
p20 = np.array([34,  61 , 86])
p21 = np.array([32,  62 , 89])
p22 = np.array([28,  64 , 93])
p23 = np.array([26,  65 , 95])
p24 = np.array([24,  66 , 98])
p25 = np.array([20,  69 , 101])
p26 = np.array([16,  72 , 103])
p27 = np.array([16,  74 , 99])
p28 = np.array([15,  75 , 96])
p29 = np.array([15,  76 , 92])
p30 = np.array([14,  76 , 89])
p31 = np.array([13,  77 , 87])
p32 = np.array([11,  78 , 84])
p33 = np.array([9,  77 , 82])
p34 = np.array([8,  76 , 80])



# These two vectors are in the plane
v1 = p1 - p32
v2 = p2 - p22

# the cross product is a vector normal to the plane
cp = np.cross(v1, v2)
a, b, c = cp

# This evaluates a * x3 + b * y3 + c * z3 which equals d
d = np.dot(cp, p3)

print('The equation is {0}x + {1}y + {2}z = {3}'.format(a, b, c, d))

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(10, 104, 50)
y = np.linspace(10, 104, 50)
X, Y = np.meshgrid(x, y)

Z = (d - a * X - b * Y) / c

# plot the mesh. Each array is 2D, so we flatten them to 1D arrays
ax.plot(X.flatten(),
        Y.flatten(),
        Z.flatten(), 'bo ')

# plot the original points. We use zip to get 1D lists of x, y and z
# coordinates.
ax.plot(*zip(p1,
p2,
p3,
p4,
p5,
p6,
p7,
p8,
p9,
p10,
p11,
p12,
p13,
p14,
p15,
p16,
p17,
p18,
p19,
p20,
p21,
p22,
p23,
p24,
p25,
p26,
p27,
p28,
p29,
p30,
p31,
p32,
p33,
p34), color='r', linestyle=' ', marker='o')

# adjust the view so we can see the point/plane alignment
ax.view_init(0, 5)
plt.tight_layout()
plt.savefig('plane.png')
plt.show()