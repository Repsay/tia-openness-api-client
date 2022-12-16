import os

cur_dir = os.path.dirname(os.path.abspath(__file__))

for root, dirs, files in os.walk(os.path.join(cur_dir, "stubs")):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                new_file = file_path.replace(".py", ".pyi")
                with open(new_file, "w") as f2:
                    f2.write(f.read())
            os.remove(file_path)
