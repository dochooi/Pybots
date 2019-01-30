import sys
def cube():
    import sys, math, pygame
    from operator import itemgetter

    class Point3D:
        def __init__(self, x=0, y=0, z=0):
            self.x, self.y, self.z = float(x), float(y), float(z)

        def rotateX(self, angle):
            """ Rotates the point around the X axis by the given angle in degrees. """
            rad = angle * math.pi / 180
            cosa = math.cos(rad)
            sina = math.sin(rad)
            y = self.y * cosa - self.z * sina
            z = self.y * sina + self.z * cosa
            return Point3D(self.x, y, z)

        def rotateY(self, angle):
            """ Rotates the point around the Y axis by the given angle in degrees. """
            rad = angle * math.pi / 180
            cosa = math.cos(rad)
            sina = math.sin(rad)
            z = self.z * cosa - self.x * sina
            x = self.z * sina + self.x * cosa
            return Point3D(x, self.y, z)

        def rotateZ(self, angle):
            """ Rotates the point around the Z axis by the given angle in degrees. """
            rad = angle * math.pi / 180
            cosa = math.cos(rad)
            sina = math.sin(rad)
            x = self.x * cosa - self.y * sina
            y = self.x * sina + self.y * cosa
            return Point3D(x, y, self.z)

        def project(self, win_width, win_height, fov, viewer_distance):
            """ Transforms this 3D point to 2D using a perspective projection. """
            factor = fov / (viewer_distance + self.z)
            x = self.x * factor + win_width / 2
            y = -self.y * factor + win_height / 2
            return Point3D(x, y, self.z)

    class Simulation:
        def __init__(self, win_width=640, win_height=480):
            pygame.init()

            self.screen = pygame.display.set_mode((win_width, win_height))
            pygame.display.set_caption("Simulation of a rotating 3D Cube (http://codeNtronix.com)")

            self.clock = pygame.time.Clock()

            self.vertices = [
                Point3D(-1, 1, -1),
                Point3D(1, 1, -1),
                Point3D(1, -1, -1),
                Point3D(-1, -1, -1),
                Point3D(-1, 1, 1),
                Point3D(1, 1, 1),
                Point3D(1, -1, 1),
                Point3D(-1, -1, 1)
            ]

            # Define the vertices that compose each of the 6 faces. These numbers are
            # indices to the vertices list defined above.
            self.faces = [(0, 1, 2, 3), (1, 5, 6, 2), (5, 4, 7, 6), (4, 0, 3, 7), (0, 4, 5, 1), (3, 2, 6, 7)]

            # Define colors for each face
            self.colors = [(255, 0, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255), (255, 255, 0)]

            self.angle = 0

        def run(self):
            """ Main Loop """
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                self.clock.tick(50)
                self.screen.fill((0, 32, 0))

                # It will hold transformed vertices.
                t = []

                for v in self.vertices:
                    # Rotate the point around X axis, then around Y axis, and finally around Z axis.
                    r = v.rotateX(self.angle).rotateY(self.angle).rotateZ(self.angle)
                    # Transform the point from 3D to 2D
                    p = r.project(self.screen.get_width(), self.screen.get_height(), 256, 4)
                    # Put the point in the list of transformed vertices
                    t.append(p)

                # Calculate the average Z values of each face.
                avg_z = []
                i = 0
                for f in self.faces:
                    z = (t[f[0]].z + t[f[1]].z + t[f[2]].z + t[f[3]].z) / 4.0
                    avg_z.append([i, z])
                    i = i + 1

                # Draw the faces using the Painter's algorithm:
                # Distant faces are drawn before the closer ones.
                for tmp in sorted(avg_z, key=itemgetter(1), reverse=True):
                    face_index = tmp[0]
                    f = self.faces[face_index]
                    pointlist = [(t[f[0]].x, t[f[0]].y), (t[f[1]].x, t[f[1]].y),
                                 (t[f[1]].x, t[f[1]].y), (t[f[2]].x, t[f[2]].y),
                                 (t[f[2]].x, t[f[2]].y), (t[f[3]].x, t[f[3]].y),
                                 (t[f[3]].x, t[f[3]].y), (t[f[0]].x, t[f[0]].y)]
                    pygame.draw.polygon(self.screen, self.colors[face_index], pointlist)

                self.angle += 1

                pygame.display.flip()

    if __name__ == "__main__":
        Simulation().run()



def sorry():
    print("sorry i dont understand")

def badword():
        sys.exit()
def exit():
    sys.exit()

def meme():
    print("21")

def creator():
 print("Doc hooi did and i was made on python")
 print("check doc out at this link!: https://www.youtube.com/channel/UC2oKxyVyqEta9a3f3Wb8zHQ")


def game():

 print("Doc hooi:Hey have you got it?")
 input("Press enter to continue...")
 print("Guardian: yeah!")
 input("Press enter to continue...")
 print("Doc hooi: Ok so can you send it?")
 input("Press enter to continue...")
 print("Guardian: Um... yeah tommorow, because it is still not executable")
 input("Press enter to continue...")
 print("Doc hooi: Ok... By t-o-m-m-o-r-o-w 6 o'clock Sharp!\
 Because the game is releasing 7 o'clock to itch.io and Steam.")


while True:

    userInput = input(">>> ")
    if userInput in['hi','HI','Hi','Hello','hello','HELLO','']:
        print("Hello")

    elif userInput in ['will you marry me','can we get married','can i be your wife/husband']:
      print("No")
    elif userInput in ['fuck','fuck you','shit','bitch','dumbass','asshole']:
        badword()
    elif userInput in ['exit','EXIT','Exit','Bye','bye','BYE']:
        print("Bye!")
        exit()
    elif userInput in ['9+10','9 + 10','Whats 9+10','Whats 9 + 10','whats 9 + 10','whats 9+10']:
        meme()
    elif userInput in ['what can you do','What can you do','what can you do?','What can you do?']:
        print("This")
        cube()
    
    elif userInput in ['Chunga','big chungus']:


        import webbrowser

        webbrowser.open('https://www.youtube.com/watch?v=lp2jveJxu6w')  # Big chungus
    elif userInput in ['Who made you','who made you']:
        creator()
    elif userInput in ['can i help you','Can i help you']:
        import webbrowser

        print("\033[1;32;40m   ")
        print("Here you can")
        webbrowser.open('https://github.com/dochooi/Pybots/blob/master/jimmy/main.py')  # Go to github.com



    else:
      sorry()
