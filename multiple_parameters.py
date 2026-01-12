
""""
 volume = width *height*length


"""

def calculate_box_volume(  width, height, length ):
    volume = width * height* length
    return volume

def main():
    width = input("Enter the width > ")
    height = input("Enter the height > ")
    length = input("Enter the length > ")
    volume = calculate_box_volume(int(width), int(height),int(length))
    # print( "Volume of the box = " + str(volume) )
    print("The volume is:", volume )

main()
