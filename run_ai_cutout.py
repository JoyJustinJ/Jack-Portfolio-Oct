import rembg
from PIL import Image
import os

input_path = r'C:\Users\jkjus\.gemini\antigravity-ide\brain\5396b157-b920-4e6d-bbb3-858e7dffcd8a\.user_uploaded\media_1792779655436.png'
output_path = r'C:\Users\jkjus\.gemini\antigravity-ide\scratch\joy-justin-portfolio\jack_profile.png'

print("Opening user photo...")
input_img = Image.open(input_path)
print(f"Original size: {input_img.size}")

print("Running AI background removal (U2-Net)...")
# alpha_matting=True gives smooth edge blending
output_img = rembg.remove(input_img, alpha_matting=True, alpha_matting_foreground_threshold=240, alpha_matting_background_threshold=10)

output_img.save(output_path, "PNG")
print(f"Saved AI transparent cutout to: {output_path}")

# Verify output
import numpy as np
arr = np.array(output_img)
print(f"Alpha min: {arr[:,:,3].min()}, max: {arr[:,:,3].max()}")
print(f"Top-left corner alpha: {arr[0,0,3]}, top-center alpha: {arr[0, arr.shape[1]//2, 3]}")
