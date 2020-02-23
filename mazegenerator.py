from PIL import Image

# put imgname equal to the image to be solved

imgname = './assets/maps/original.png'


def array(imgname):

    image = Image.open(imgname)

    width, height = image.size

    maze = []

    for i in range(width):

        row = []

        for j in range(height):

            if image.getpixel((j, i))[0] == 255:

                row.append(0)

            else:

                row.append(1)

        maze.append(row)

    return maze


    # node making algorithm
    # key --
    # 0 = wall
    # 1 = connecting nodes
    # 2 = nodes
    # 3 = start node
    # 4 = end node
if __name__ == "__main__":
    print(array(imgname))
