import clipboard
import keyboard
import sys
import time

WAIT_TIME = 5

to_type = clipboard.paste()

args = sys.argv[:]
assert len(args) > 0, "This should never happen"
filename = args[0]

confirm = True

if len(args) == 1:  # only filename
    confirm = True
else:
    unknown_args = []

    i = 1
    while i < len(args):
        if args[i].lower().strip() == "no_confirm":
            if confirm:
                print(f"Found \"no_confirm\" as argument {i}, bypassing confirmation.")
                confirm = False
        else:
            unknown_args.append(args[i])
        i += 1

    if len(unknown_args) == 0:
        pass
    elif len(unknown_args) == 1:
        print(f"Ignoring unknown argument \"{unknown_args[0]}\".")
    elif len(unknown_args) == 2:
        print(f"Ignoring unknown arguments \"{unknown_args[0]}\" and \"{unknown_args[1]}\".")
    else:
        unknown_args_str = "\"" + "\", \"".join(unknown_args[:-1]) + \
                           "\", and \"" + unknown_args[-1] + "\""
        print(f"Ignoring unknown arguments {unknown_args_str}")

print("Here is what is going to be typed:\n" + to_type + "\n")

if confirm:
    print(f"When you're ready, press Enter, and you'll have {WAIT_TIME} seconds to switch "
          "applications to where you would like the text to be typed.\n"
          "You can also bypass this confirmation next time by running this script "
          "with the argument \"no_confirm\", i.e.:\n"
          f"python {filename} no_confirm\n"
          "Press Enter when you're ready.")
    input()

print(f"You have {WAIT_TIME} seconds to switch applications before typing begins!")
time.sleep(WAIT_TIME)

print("Beginning typing!")
start = time.time()
keyboard.write(to_type)
end = time.time()

print(f"Done! [Time elapsed: {end - start:.3f} seconds]")
