d1 = [(k,v) for k in range(1,6) for v in range(1,6)]
print("All coordinates from (1,1) to (5,5):")
for coord in d1:
    print(coord)

print(f"\nTotal number of points: {len(d1)}")