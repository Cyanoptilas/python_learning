# 1
x = 100 - 5**2 + 5 /5
print("🚀 ~ x:", x)

# 2
text2  = (
    "Usage: "
    "-h help"
    "-v version"

    "1"
    "2"
    "3"

)
print(text2)

#3
text3 = """1
2
3
"""
print(text3)
# text3b = '''1
# 2
# 3
# '''
# print(text3b)

#4
print(len("abc"))

#5
word5 = "1234567890"
slicedWord5= word5[2:5]
print(slicedWord5)

#6
word6 = "1234567890"
slicedWord6= word6[-5:]
print(slicedWord6)

#7
price7 = 15000
print(f"価格:{price7:7d}")

#8
import math

print(f"πはおよそ...{math.pi:5f}")
print(f"πはおよそ...{math.pi:.5f}")
print(f"πはおよそ...{math.pi:10.5f}")

#9
x9 = 300
y9= 150
z9 = 200
print("spam: {0}, ham: {1}, eggs: {2}".format(x9, y9, z9))
print("spam: {x9}, ham: {y9}, eggs: {z9}".format(x9, y9, z9))
print("spam: {}, ham: {}, eggs: {}".format(x9, y9, z9))
print("spam: {a}, ham{b}, eggs: {c}".format(a=x9, b=y9, c=z9))