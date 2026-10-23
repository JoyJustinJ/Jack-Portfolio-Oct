from PIL import Image
import rembg
import numpy as np

src_path = r'C:\Users\jkjus\.gemini\antigravity-ide\brain\5396b157-b920-4e6d-bbb3-858e7dffcd8a\.user_uploaded\media_1792779655436.png'
out_path = r'C:\Users\jkjus\.gemini\antigravity-ide\scratch\JACK-portfolio\jack_profile.png'

# 1. Load full resolution user photo
img = Image.open(src_path).convert('RGBA')
print(f"Original image size: {img.size}")

# 2. Run rembg with u2netp on the full-resolution image
session = rembg.new_session('u2netp')
transparent_full = rembg.remove(img, session=session)

# 3. Find bounding box of Jack's actual body
arr = np.array(transparent_full)
alpha = arr[:, :, 3]
rows = np.where(alpha > 15)[0]
cols = np.where(alpha > 15)[1]

top_y = rows.min()
bottom_y = rows.max()
left_x = cols.min()
right_x = cols.max()

body_h = bottom_y - top_y
body_w = right_x - left_x
print(f"Body bounds: Y={top_y}..{bottom_y} (height={body_h}), X={left_x}..{right_x} (width={body_w})")

# Keep slight 10px headroom at top so hair tips aren't clipped
crop_top = max(0, top_y - 12)
crop_bottom = min(arr.shape[0], bottom_y + 1)
crop_left = max(0, left_x - 16)
crop_right = min(arr.shape[1], right_x + 16)

zoomed_cutout = transparent_full.crop((crop_left, crop_top, crop_right, crop_bottom))
print(f"Zoomed cutout resolution: {zoomed_cutout.size} (pure subject, no empty dead space!)")

# Save at maximum PNG compression quality without any resampling/loss
zoomed_cutout.save(out_path, format="PNG", optimize=True)
print(f"Saved high-clarity zoomed cutout to {out_path}!")
