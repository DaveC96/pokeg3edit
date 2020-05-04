#   --  Standard libraries
import argparse

#   --  Local
import pokestring
import savedata

#   --      --      --      --      --      --      --      --

def main():
    parser = argparse.ArgumentParser(description="Savegame editor for Pokemon Gen 3")
    parser.add_argument("--file", dest="savefile", action="store", help="Save data to modify")
    parser.add_argument("--trainer-name", dest="mod_trainername", action="store", help="Set the trainer's name (1-7 characters)")

    args = parser.parse_args()
    print(args.savefile)
    print(args.mod_trainername)


if __name__ == "__main__":
    main()