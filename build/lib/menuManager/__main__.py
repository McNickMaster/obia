import os
import sys
import time
from pathlib import Path
from yaspin import yaspin

class bccolors:
    MAIN = '\033[92m'
    ALT = '\033[94m'

def main(args=None):

    if args is None:
        args = sys.argv[1:]

    #setup
    nameOfItem = ""
    typeOfItem = ""
    commandOfItem = ""

    foundMenu = False

    #TODO add spinners to this project

    #----------------------------------------------------------------------

    #get home path
    home = str(Path.home())
    #concant w/ rest of dir
    configDir = home + "/.config/openbox/menu.xml"

    nameOfMenu = input(bccolors.MAIN + "Name of The Menu (defualt root-menu): ")
    nameOfItem = input("Name of Menu Item (default New Item): ")
    typeOfItem = input("Type of Item (default Execute): ")
    commandOfItem = input("Command: ")

    with yaspin(text="Creating Entry...", color="cyan") as sp:

        time.sleep(2)

        #default checke r
        if nameOfMenu == "":
            nameOfMenu = "root-menu"

        if nameOfItem == "":
            nameOfItem = "New Item"

        if typeOfItem == "":
            typeOfItem = "Execute"

        idMenu = "id=\"" + nameOfMenu

    #------------------------------------------------------------------------------------

        #create crappy string
        #TODO find a fix?

        xmlEntry = "        <item label=\"" + nameOfItem + "\"\n            <action name=\"" + typeOfItem + "\">\n                <command>\n                   "+commandOfItem+"\n               </command>\n            </action>\n        </item>\n"

        sp.write(bccolors.ALT + "\nLooking for menu in file...")

        #open file for reading and get contents
        with open(configDir, "r") as sf:
                for line in sf:
                    if idMenu in line:
                        foundMenu = True
                        sp.write("Menu found!")

        with open(configDir, "r") as f:
                content = f.readlines()
                f.close()


        #TODO remove this if statement
        if (foundMenu == False):
            sp.write("Error: Menu " + nameOfMenu + " not found")
            exit()

        #get index
        index = [x for x in range(len(content)) if nameOfMenu in content[x].lower()]

        sp.write("Adding to menu.xml...")

        #insert text into file at index plus 1
        content.insert(index[0] + 1, xmlEntry)

        #write
        f = open(configDir, "w")
        content = "".join(content)
        f.write(content)
        f.close()

        sp.write("Done!")

if __name__ == "__main__":
    main()
