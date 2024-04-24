# ANSI escape codes for text colors
class colors:
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
# Example usage
print(colors.RED + "This text is red." + colors.RESET)
print(colors.GREEN + "This text is green." + colors.RESET)

