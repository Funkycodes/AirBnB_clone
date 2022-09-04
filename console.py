"""
File: console.py
Author: theMaskedOtaku
Email: otakuS3nnin@gmail.com
Github: https://github.com/Funkycodes
Description:
"""

import cmd
from models import storage
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
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        else:
            obj = self.class_dict[line]()
            obj.save()
            print(obj.id)

    def do_save(self, line):
        """Save all instances of given class
        """
        self.class_dict[line].save()

    def do_show(self, line):
        """Show all initialized instances
        """

        ln = len(line.split())
        args = line.split()
        if ln == 0:
            print("** class name missing **")
            return
        elif ln == 1 and args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        elif ln == 1 and args[0] in HBNBCommand.class_dict:
            print("** instance id missing **")
        else:
            name = "{}.{}".format(args[0], args[1])
            if name not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[name])

    def do_destroy(self, line):
        """Destroy instance specified by user. And commit changes to json file
        """

        ln = len(line.split())
        args = line.split()
        if ln == 0:
            print("** class name missing **")
            return
        elif ln == 1 and args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        elif ln == 1 and args[0] in HBNBCommand.class_dict:
            print("** instance id missing **")
        else:
            name = "{}.{}".format(args[0], args[1])
            if name not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[name]
                storage.save()

    def do_all(self, line):
        """Show instantiated objects depending on whether an argument is given
        or not"""

        ln = len(line.split())
        args = line.split()
        if ln == 0:
            for objs in storage.all().values():
                print(objs)
        elif args[0] in HBNBCommand.class_dict:
            for key, obj in storage.all().items():
                if args[0] == key.split('.')[0]:
                    print(obj)
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
