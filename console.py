#!/usr/bin/python3
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
        """End Of File indicator for program, quits the program with void
        return value"""

        return True

    def emptyline(self):
        """Override the default behaviour of response to emptyline input"""
        pass

    def do_create(self, line):
        """Create an instance of class given as argument if it exists, else re\
turn error"""

        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        else:
            obj = self.class_dict[line]()
            obj.save()
            print(obj.id)

    def do_save(self, line):
        """Save all instances of given class"""
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
        obj_list = []
        if ln == 0:
            for obj in storage.all().values():
                obj_list.append(obj)
            print(obj_list)
        elif args[0] in HBNBCommand.class_dict:
            for key, obj in storage.all().items():
                if args[0] == key.split('.')[0]:
                    obj_list.append(obj)
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Update object with id attribute match"""

        args = line.split()
        ln = len(args)

        if ln == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        elif ln == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        elif ln == 2:
            print("** attribute name missing **")
        elif ln == 3:
            print("** value missing **")
        elif ln >= 4:
            key = "{}.{}".format(args[0], args[1])
            type_cast = type(eval(args[3]))
            attr_value = type_cast(args[3].strip('"\''))
            setattr(storage.all()[key], args[2], attr_value)
            storage.all()[key].save()

    def do_count(self, line):
        """Print count of all instantiated objects"""
        args = line.split()
        if args[0]:
            if args[0] in HBNBCommand.class_dict:
                count = 0
                for key in storage.all().keys():
                    if args[0] == key.split('.')[0]:
                        count += 1
                print(count)
            else:
                print("** class doesn't exist **")

    def default(self, line):
        """Accepts class name followed by arguement"""
        args = line.split('.')
        class_arg = args[0]
        if len(args) == 1:
            print("*** Unknown syntax: {}".format(line))
            return
        try:
            args = args[1].split('(')
            command = args[0]
            if command == 'all':
                HBNBCommand.do_all(self, class_arg)
            elif command == 'count':
                HBNBCommand.do_count(self, class_arg)
            elif command == 'show':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip("'")
                id_arg = id_arg.strip('"')
                arg = class_arg + ' ' + id_arg
                HBNBCommand.do_show(self, arg)
            elif command == 'destroy':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip('"')
                id_arg = id_arg.strip("'")
                arg = class_arg + ' ' + id_arg
                HBNBCommand.do_destroy(self, arg)
            elif command == 'update':
                args = args[1].split(',')
                id_arg = args[0].strip("'")
                id_arg = id_arg.strip('"')
                name_arg = args[1].strip(',')
                val_arg = args[2]
                name_arg = name_arg.strip(' ')
                name_arg = name_arg.strip("'")
                name_arg = name_arg.strip('"')
                val_arg = val_arg.strip(' ')
                val_arg = val_arg.strip(')')
                arg = class_arg + ' ' + id_arg + ' ' + name_arg + ' ' + val_arg
                HBNBCommand.do_update(self, arg)
            else:
                print("*** Unknown syntax: {}".format(line))
        except IndexError:
            print("*** Unknown syntax: {}".format(line))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
