import rembg
from PIL import Image

input_path = r'C:\Users\jkjus\.gemini\antigravity-ide\brain\5396b157-b920-4e6d-bbb3-858e7dffcd8a\.user_uploaded\media_1792779655436.png'
output_path = r'C:\Users\jkjus\.gemini\antigravity-ide\scratch\joy-justin-portfolio\jack_profile.png'

print("Using lightweight u2netp (4MB model)...", flush=True)
session = rembg.new_session('u2netp')
print("Model initialized. Loading image...", flush=True)
input_img = Image.open(input_path)

print("Removing background...", flush=True)
output_img = rembg.remove(input_img, session=session)

output_img.save(output_path, "PNG")
print(f"DONE! Saved to {output_path}", flush=True)

import numpy as np
arr = np.array(output_img)
print("Alpha min:", arr[:,:,3].min(), "max:", arr[:,:,3].max(), flush=True)
print("Top-left pixel alpha:", arr[0, 0, 3], "Center head alpha:", arr[500, 340, 3], flush=True)
