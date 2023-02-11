def full_adder(a, b, c):
  s = (a + b + c) % 2
  co = (a + b + c) // 2
  return s, co

def four_bit_adder(a, b, c = 0):
  s = [0, 0, 0, 0]
  for i in range(3, -1, -1):
    s[i], c = full_adder(int(a[i]), int(b[i]), c)
  s = "".join(str(j) for j in s)
  return s, c

def BCD_adder(a, b):
  a_4bits = a.split(" ")
  b_4bits = b.split(" ")
  
  s = []
  c = 0
  for i in range(len(a_4bits)-1,-1,-1):
    temp, c = four_bit_adder(a_4bits[i], b_4bits[i], c)
    if(temp>"1001"):
      temp, c1 = four_bit_adder(temp, "0110")
      c = c|c1
    s.append(temp)
  
  if(c == 1):
    s.append("0001")
  
  s.reverse()
  return " ".join(d for d in s)

print("Enter BCD inputs(eg: 1000 0110)\n")
num1 = input("num1: ")
num2 = input("num2: ")
print("the sum is ",BCD_adder(num1, num2))