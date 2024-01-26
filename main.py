from src import utils
from src.openspace import OpenSpace


def main():
    filepath = "colleagues.xlsx"
    names = utils.read_names_from_excel(filepath)
    open_space = OpenSpace()
    open_space.organize(names)
    open_space.store("output.xlsx")
    open_space.display()
    print(f"\nTotal number of occupied seats: {open_space.total_people()}")
    print(f"Number of available seats: {open_space.total_seats_left()}")

if __name__ == "__main__":
    main()
