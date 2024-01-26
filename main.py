from src import utils
from src.openspace import OpenSpace


def main():
    filepath = "colleagues.xlsx"
    names = utils.read_names_from_excel(filepath)
    open_space = OpenSpace()
    open_space.organize(names)
    open_space.display()

if __name__ == "__main__":
    main()
