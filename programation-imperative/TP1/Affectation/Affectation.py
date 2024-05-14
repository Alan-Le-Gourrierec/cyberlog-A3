#
# A program to manipulate variables and affectations.
#
#-------------------------------------------------
# step 1
a = 3
#-------------------------------------------------
b = a * a
a = a + b
c = a + b
b = a / b
d = "co"
e = a == b
print("Step 1.\n  a:", a, "\t", type(a),
      "\n  b:", b, "\t", type(b),
      "\n  c:", c, "\t", type(c),
      "\n  d:", d, "\t", type(d),
      "\n  e:", e, "\t", type(e), "\n")

#-------------------------------------------------
# step 2
#-------------------------------------------------
c = a % 5
a = a * b
b = a % 5
d = d + "u"
e = c < a < b
print("Step 2.\n  a:", a, "\t", type(a),
      "\n  b:", b, "\t", type(b),
      "\n  c:", c, "\t", type(c),
      "\n  d:", d, "\t", type(d),
      "\n  e:", e, "\t", type(e), "\n")

#-------------------------------------------------
# step 3
#-------------------------------------------------
a = d * 2
b = a * c
c = a / c
d = d * b
e = a == b or c >= d or e
print("Step 3.\n  a:", a, "\t", type(a), 
      "\n  b:", b, "\t", type(b),
      "\n  c:", c, "\t", type(c),
      "\n  d:", d, "\t", type(d),
      "\n  e:", e, "\t", type(e), "\n")
