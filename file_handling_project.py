from pathlib import Path
import shutil

def creating_folder():
    try:
        name =input("Enter name of the folder : ")
        p = Path(name)
        p.mkdir()
        print("Your folder is created successfully!")
    except Exception as err :
        print(f"An error occoured as {err}")


def  reading_folder():
    try:
        print("You have following folders to read....")
        p = Path("")
        folders = list(p.rglob("*"))
        for index,element in enumerate(folders):
            print(f"{index+1} : {element}")
        print(f"You have total {index} files and folder to read...")
    except Exception as err:
        print(f"An error occured as {err}")

def updating_folder():
    try:
        reading_folder()
        old_name = input("Enter which file you want to update :")
        p = Path(old_name)
        if p.exists() and p.is_dir():
            new_name = input("Enter new name :  ")
            new_p = Path(new_name)
            p.rename(new_p)
            print("Your folder name is updated successfully")
        else:
            print(f"No such folder exixts ")
    except Exception as err:
        print("An error occured as {err}")


def deleting_folder():
    try:
        reading_folder()
        delete = input("which folder you wanna delete: ")
        p = Path(delete)
        if p.exists and p.is_dir:
            shutil.rmtree(p)
            print("Folder is deleted successfully")
        else:
            print("No such file exist")
    except Exception as err:
        print(f"An occured as {err}")


def create_file():
    try:
        name = input("which name do you wanna give your file ? : ")
        p = Path(name)
        if not p.exists():
            with open(name,"w") as fs:
                writing = input("Write what do you want :")
                fs.write(writing)

            print("Your file created successfully..")
        else:
            print("Sorry this name is already exist")
    except Exception as err:
        print(f"An error occured as {err}")

def read_file():
    try:
        reading_folder()
        name = input("Which file you wanna read : ")
        p = Path(name)
        if p.exists and p.is_dir:
            with open(name,"r") as fs:
                content = fs.read()
                print("You content in the file....")
                print(content)
        else:
            print("No such file exist!")
    except Exception as err:
        print(f"An error occured as {err}")

def update_file():
    try:
        reading_folder()
        name = input("which file you wanna update:")
        p = Path(name)
        if p.exists() and p.is_file():
            print("1. For renaming the file")
            print("2. For appending something in the file ")
            print("3. For overwriting the file content ")
            choice = int(input("tell your choice : "))

            if choice == 1:
                new_name = input("Tell new name for file:")
                new_p = Path(new_name)
                if not new_p.exists():
                    p.rename(new_name) 
                    print("Your file name changed successfully")
                else:
                    print("Sorry file already exist!")
            if choice == 2:
                    with open(name,'a') as fs:
                        data = input("what you want to append : ")
                        fs.write(" "+ data)
                    print("Data appended successfully ")

            if choice == 3:
                with open(name,"w") as fs :
                    data = input("What you want to overwrite : ")
                    fs.write(data)
                print("Data changed successfully ")
    except  Exception as err:
        print(f"An error occured as {err}")

def delete_file():
    try:
        reading_folder
        name = input("tell your file name with extension : ")
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("file Deleted successfully")
        else:
            print("sorry no such file exist")
    
    except Exception as err:
        print(f"An error occured as {err}")

    
while True:
    print("Hey! choose one option to test me...... ")
    print("1. for creating a folder.")
    print("2. for reading a folder.")
    print("3. for updating a folder.")
    print("4. for deleting a folder.")
    print("5. for creating a file.")
    print("6. for reading a file.")
    print("7. for updating a file.")
    print("8. for deleting a file.")
    print("0. for Exit the programe")

    choice = int(input("Please,enter you choice : "))

    if choice == 1:
        creating_folder()

    if choice == 2:
        reading_folder()

    if choice == 3 :
        updating_folder()

    if choice == 4:
        deleting_folder()

    if choice == 5:
        create_file()

    if choice == 6:
        read_file()

    if choice == 7 :
        update_file()

    if choice == 8:
        delete_file()
