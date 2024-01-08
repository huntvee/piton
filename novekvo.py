def novekvo(n):
    for i in range(1, len(n)):
        if n[i] <= n[i - 1]:
            return False
    return True
szamlista = [1, 2, 3, 4, 5]
if novekvo(szamlista):
    print("A számlista szigorúan monoton növekvő.")
else:
    print("A számlista nem szigorúan monoton növekvő.")