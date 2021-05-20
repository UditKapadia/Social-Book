def delete():
    with open("users.txt", "r") as f:
        lines = f.readlines()
    with open("users.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != "uk12345"+","+"mnmnmn":
                f.write(line)
                f.close()
