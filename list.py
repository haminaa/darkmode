import os

def list_folders(path):
    try:
        folders = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
        for folder in folders:
            print(folder)
    except Exception as e:
        print(f"error: {e}")

path = r""

list_folders(path)