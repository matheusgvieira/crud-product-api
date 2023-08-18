import os


def run_seed_scripts():
    seed_folder = f"{os.getcwd()}/seeds"  # Change this to the path of your seeds folder
    print([file for file in os.listdir(seed_folder) if file.startswith("seed")])

    for filename in [
        file for file in os.listdir(seed_folder) if file.startswith("seed")
    ]:
        if filename.endswith(".py"):
            script_path = os.path.join(seed_folder, filename)
            print(f"Running {filename}...")
            try:
                exec(open(script_path).read())
                print(f"{filename} executed successfully.\n")
            except Exception as e:
                print(f"Error executing {filename}: {e}\n")


if __name__ == "__main__":
    run_seed_scripts()
