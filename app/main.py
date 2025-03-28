import os.path


def copy_file(command: str) -> None:
    if command.count(".txt") == 2:
        if "cp " in command:
            command = command.split("cp", 1)[1]
        command = command.split(".txt")
        main_file = command[0].strip() + ".txt"
        new_file = command[1].strip() + ".txt"
        if os.path.exists(main_file) and main_file != new_file:
            try:
                with (
                    open(main_file, "r", encoding="utf-8") as main_file_object,
                    open(new_file, "w", encoding="utf-8") as new_file_object
                ):
                    new_file_object.write(main_file_object.read())
            except OSError as e:
                print(f"Error while copying file: {e}")
        else:
            print(f"The file named: \"{main_file}\" does not exist.")
