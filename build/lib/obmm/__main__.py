import sys
import time
from pathlib import Path
from yaspin import yaspin
from pyfiglet import Figlet as figlet
from clint.arguments import Args
from clint.textui import prompt, puts, colored, indent


class bccolors:
    MAIN = '\033[93m'
    ALT = '\033[94m'
    TITLE = '\033[92m'




def main(args=None):

    if args is None:
        args = sys.argv[1:]

    args = Args()

    # setup
    nameOfItem = ""
    typeOfItem = ""
    commandOfItem = ""

    foundMenu = False

    #----------------------------------------------------------------------

    figText = figlet(font='slant')
    print (bccolors.TITLE + figText.renderText('obmm'))

    firstArg = str(args[0])


    if firstArg == '-t':
        #TODO expand... theres a lot of actions
        if str(args[1]) == 'Execute' or str(args[1]) == 'ShowMenu':
            typeOfItem = str(args[1])
        else:
            print('Invalid type: ' + str(args[1]))
            exit()

   # print(str(args))
   # print(str(args[0]))
   # print(typeOfItem)

    #for item in args.flags:
     #   if item is not '_':
      #      if item == '-t':
       #         typeOfItem = (str(args[1]))

    #get home path
    home = str(Path.home())
    #concant w/ rest of dir
    configDir = home + "/.config/openbox/menu.xml"


    nameOfMenu = prompt.query(bccolors.TITLE + '>>>' + bccolors.MAIN + " Name of The Menu: ", default='root-menu')
    nameOfItem = prompt.query(bccolors.TITLE + '>>>' + bccolors.MAIN + " Name of Menu Item: ", default='New Item')
    commandOfItem = prompt.query(bccolors.TITLE + '>>>' + bccolors.MAIN + " Item Command: ")

    with yaspin(text="Creating Entry...", color="cyan") as sp:

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
