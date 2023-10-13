def is_monotonically_increasing(arr):
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            return False
    return True
szamlista = [1, 2, 3, 1, 5]
if is_monotonically_increasing(szamlista):
    print("A számlista szigorúan monoton növekvő.")
else:
    print("A számlista nem szigorúan monoton növekvő.")