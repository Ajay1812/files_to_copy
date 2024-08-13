import glob
import os
import shutil

save_directory = r"/Users/ajay/Documents/Personal/Courses/Frontend/Javascript/Basics/wall/Extracted"

wallpaper = []
wallpaper = glob.glob("/Users/ajay/Documents/Personal/Courses/Frontend/Javascript/Basics/wall/Wallpapers/*/*[.jpg,.png]")
# print(wallpaper)

for path in wallpaper:
  file_name = os.path.basename(path)
  destination = os.path.join(save_directory, file_name)
  shutil.copy2(path ,destination)

print(f"Copied {len(wallpaper)} files to {save_directory}")
