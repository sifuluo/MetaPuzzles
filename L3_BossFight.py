from typing import List
# Write any import statements here

def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
  # Write your code here
  maxdamage = 0
  keeprun = True
  wfix = 0
  while keeprun:
    keeprun = False
    for i in range(N):
      if i == wfix: continue
      damage = H[wfix] * D[wfix] + H[i] * D[i] + max(H[wfix] * D[i], H[i] * D[wfix])
      if damage > maxdamage:
        keeprun = True
        maxdamage, wi = damage, i
    if keeprun: wfix = wi
  return maxdamage / B

def main():
  N = 4
  H = [1, 1, 2, 3]
  D = [1, 2, 1, 100]
  B = 8
  dd = getMaxDamageDealt(N,H,D,B)
  print(dd)

main()