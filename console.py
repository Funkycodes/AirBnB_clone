"""
File: console.py
Author: theMaskedOtaku
Email: otakuS3nnin@gmail.com
Github: https://github.com/Funkycodes
Description:
"""

import cmd
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.user import User
from models.place import Place
from models.state import State


class HBNBCommand(cmd.Cmd):

    """Main component of the console.
    Extends cmd.Cmd class.
    """
    
    class_dict = {
        "Amenity": Amenity,
        "BaseModel": BaseModel,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User
    }
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

    def do_create(self, line):
        """Create an instance of class given as argument if it exists, else re\
turn error
        """

        name = self.class_dict[line]()
        name.__str__()

    def do_save(self, line):
        """Save all instances of given class
        """
        self.class_dict[line].save()

    def do_show(self, line):
        """Show all initialized instances
        """

        print(models.storage.all())

if __name__ == "__main__":
    HBNBCommand().cmdloop()
