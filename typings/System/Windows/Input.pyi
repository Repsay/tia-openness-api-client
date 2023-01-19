# encoding: utf-8
# module System.Windows.Input calls itself Input
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ICommand:
    """ Defines a command. """
    def CanExecute(self, parameter):
        """
        CanExecute(self: ICommand, parameter: object) -> bool

            Defines the method that determines whether the command can execute in its current state.

            parameter: Data used by the command.  If the command does not require data to be passed, this object can be set to ll.

            Returns: ue if this command can be executed; otherwise, lse.
        """
        ...

    def Execute(self, parameter):
        """
        Execute(self: ICommand, parameter: object)

            Defines the method to be called when the command is invoked.

            parameter: Data used by the command.  If the command does not require data to be passed, this object can be set to ll.
        """
        ...

    CanExecuteChanged = None


