from BStore_Database import DvdDb
from BStore_GUI import BStore

def main():
    db = DvdDb(init=False, db="dvdstore.csv")
    app = BStore(database=db)
    app.mainloop()

if __name__ == "__main__":
    main()