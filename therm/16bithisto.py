import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the 8-bit RGB image
image = cv2.imread("temperature_high.png")

# Split the image into individual channels
channels = cv2.split(image)
b = channels
g = channels
r = channels
# Convert the individual channels to 16-bit by expanding the range
b_16bit = np.uint16(b) * 257
g_16bit = np.uint16(g) * 257
r_16bit = np.uint16(r) * 257

# Merge the 16-bit channels back into an image
image_16bit = cv2.merge([b_16bit, g_16bit, r_16bit])

# Calculate histograms for the 8-bit channels
#hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
#hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
#hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

# Calculate histograms for the 16-bit channels
hist_b_16bit = cv2.calcHist([b_16bit], [0], None, [65536], [0, 65536])
hist_g_16bit = cv2.calcHist([g_16bit], [0], None, [65536], [0, 65536])
hist_r_16bit = cv2.calcHist([r_16bit], [0], None, [65536], [0, 65536])

# Plot histograms for comparison
colors = ('b', 'g', 'r')
titles = ('Blue Channel', 'Green Channel', 'Red Channel')

plt.figure(figsize=(12, 6))
"""
plt.subplot(2, 3, 1)
plt.plot(hist_b, color=colors[0])
plt.title(titles[0] + ' (8-bit)')
plt.xlim([0, 256])
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.subplot(2, 3, 2)

plt.plot(hist_g, color=colors[1])
plt.title(titles[1] + ' (8-bit)')
plt.xlim([0, 256])
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.subplot(2, 3, 3)
plt.plot(hist_r, color=colors[2])
plt.title(titles[2] + ' (8-bit)')
plt.xlim([0, 256])
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
"""
plt.subplot(2, 3, 4)
plt.plot(hist_b_16bit, color=colors[0])
plt.title(titles[0] + ' (16-bit)')
plt.xlim([0, 65536])
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.subplot(2, 3, 5)
plt.plot(hist_g_16bit, color=colors[1])
plt.title(titles[1] + ' (16-bit)')
plt.xlim([0, 65536])
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.subplot(2, 3, 6)
plt.plot(hist_r_16bit, color=colors[2])
plt.title(titles[2] + ' (16-bit)')
plt.xlim([0, 65536])
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
