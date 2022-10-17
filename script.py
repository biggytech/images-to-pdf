from PIL import Image
import sys

# validate args count
if not len(sys.argv) == 6:
  print("Invalid number of arguments")
  sys.exit()

images_path = sys.argv[1]
extension = sys.argv[2]
from_range = int(sys.argv[3])
to_range = int(sys.argv[4])
output_file_path = sys.argv[5]

print("Generating...")

imagelist = range(from_range, to_range+1)

images = [
    Image.open(images_path + str(i) + '.' + extension)
    for i in imagelist
]

pdf_path = output_file_path
    
images[0].save(
    pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)

print("Done!")