def hanoi(topN, a = "Tower1", b = "Tower2", c = "Tower3"):
    if (topN == 1):
        print ("move " + a + " to " + c)
    else:
        hanoi(topN - 1, a, c, b)
        print ("move " + a + " to " + c)
        hanoi(topN - 1, b, a, c)