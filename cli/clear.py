import os

def clear_console(system):
    """Clears the console screen based on the operating system.

    Parameters
    ----------
    system : str
        the name of the operating system

    Returns
    -------
    int
        the exit code of the clear command
    """
    if system in ('Linux','Darwin'): 
        clear = os.system('clear')
    else:
        clear = os.system('cls')