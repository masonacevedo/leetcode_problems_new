import sys
import pyperclip

if __name__ == "__main__":
    name_strings = sys.argv[1:]
    name = "_".join(name_strings)

    ans = name.replace(".","")
    ans += ".py"
    print(ans)
    pyperclip.copy(ans)