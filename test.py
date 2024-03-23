# import os

# folder_path = "Giới Động Vật (Animal)/Lớp Cá Sụn (Chondrichthyes)/tmp"  # Replace with the actual folder path

# for folder_name in os.listdir(folder_path):
#     if os.path.isdir(os.path.join(folder_path, folder_name)):
#         parts = folder_name.split(" ")
#         if len(parts) == 3:
#             name = parts[0]
#             ijk = parts[2]
#             xyz = parts[1]
#             ijk = ijk[1:-1]
#             new_folder_name = f"{name} {ijk} ({xyz})"
#             os.rename(
#                 os.path.join(folder_path, folder_name),
#                 os.path.join(folder_path, new_folder_name)
#             )


def HelloWorld(a):
  print("Hello, World!")

HelloWorld("print")
