from PIL import Image
import numpy as np
from collections import deque

# Load user's uploaded image
src_path = r'C:\Users\jkjus\.gemini\antigravity-ide\brain\5396b157-b920-4e6d-bbb3-858e7dffcd8a\.user_uploaded\media_1792776454447.png'
img = Image.open(src_path).convert('RGBA')
arr = np.array(img)
h, w, _ = arr.shape
print(f"Image shape: {w}x{h}")

# We want to flood-fill transparent from the outer boundary pixels where color is near-white (> 245 in R, G, B)
# Note: Jack's shirt is white, but it is bounded by the black jacket, skin neck, and tie!
# Flood-fill from outer border ensures only the external background is made transparent!

is_white = (arr[:, :, 0] > 240) & (arr[:, :, 1] > 240) & (arr[:, :, 2] > 240)
visited = np.zeros((h, w), dtype=bool)
bg_mask = np.zeros((h, w), dtype=bool)

queue = deque()

# Add all border pixels that are near-white
for x in range(w):
    if is_white[0, x]:
        queue.append((0, x))
        visited[0, x] = True
    if is_white[h-1, x]:
        queue.append((h-1, x))
        visited[h-1, x] = True

for y in range(h):
    if is_white[y, 0]:
        queue.append((y, 0))
        visited[y, 0] = True
    if is_white[y, w-1]:
        queue.append((y, w-1))
        visited[y, w-1] = True

# BFS flood fill
neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while queue:
    y, x = queue.popleft()
    bg_mask[y, x] = True
    for dy, dx in neighbors:
        ny, nx = y + dy, x + dx
        if 0 <= ny < h and 0 <= nx < w:
            if not visited[ny, nx] and is_white[ny, nx]:
                visited[ny, nx] = True
                queue.append((ny, nx))

# Set alpha to 0 for all external background pixels
arr[bg_mask, 3] = 0

# Smooth alpha slightly along edge for antialiasing
# For pixels adjacent to bg_mask, if brightness is high, ramp alpha
result_img = Image.fromarray(arr, 'RGBA')
result_img.save('jack_profile.png')
print("Successfully created jack_profile.png with transparent background!")
