def hexcolor(r, g, b):
    hex = ("0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F")
    hexstr = "#"
    for x in r, g, b:
         hexstr += f"{hex[int(x/16)%16]}{hex[x%16]}"
    return hexstr

rgb = input("Enter R,G,B Values: ")
rgb_list = rgb.split(",")

print(hexcolor(int(rgb_list[0]),int(rgb_list[1]),int(rgb_list[2])))
