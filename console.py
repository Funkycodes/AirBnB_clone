"""
File: console.py
Author: theMaskedOtaku
Email: otakuS3nnin@gmail.com
Github: https://github.com/Funkycodes
Description: 
"""
import cmd


class HBNBCommand(cmd.Cmd):

    """Main component of the console.
    Extends cmd.Cmd class.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Implement quit command for cmd
        """

        return True

    def help_quit(self):
        """Shows help for the quit function"""

        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """
        End Of File indicator for program, quits the program with void return\
 value
        """
        return True

    def emptyline(self):
        """
        Override the default behaviour of response to emptyline input
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
