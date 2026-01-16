def copy_file(command) -> None:
    cp, src, dst = command.split()

    if src == dst:
        return

    if command != 3:
        return

    with open(src, "r") as file_in, open(dst, "w") as file_out:
        file_out.write(file_in.read())