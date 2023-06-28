import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the 8-bit RGB image
image = cv2.imread("template_high.png")
print(image)
# Split the image into individual channels
channels = cv2.split(image)
print(channels)
# Scale up each channel's pixel values to 16-bit range
channels_16bit = [np.uint16(channel) * 256 for channel in channels]

image_16bit = cv2.merge(channels_16bit)
cv2.imwrite("img16.tiff", image_16bit)
img16 = cv2.imread("img16.tiff", cv2.IMREAD_UNCHANGED)
channels = cv2.split(img16)
channels_16bit = [np.uint16(channel) * 256 for channel in channels]

# Calculate histograms for the 16-bit channels
hist_16bit = [cv2.calcHist([image_16bit], [i], None, [65536], [0, 65536]) for i in range(3)]

# Plot histograms for the 16-bit channels
colors = ('b', 'g', 'r')
titles = ('Blue Channel', 'Green Channel', 'Red Channel')

plt.figure(figsize=(12, 4))

for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.plot(hist_16bit[i], color=colors[i])
    plt.title(titles[i] + ' (16-bit)')
    plt.xlim([0, 65536])
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
