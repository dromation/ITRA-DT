import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the 8-bit RGB image
image = cv2.imread('template_high.png')
print(image)
# Split the image into individual channels
channels = cv2.split(image)
print(channels)
# Scale up each channel's pixel values to 16-bit range
channels_16bit = [np.uint16(channel) * 256 for channel in channels]

# Merge the scaled channels back into a 16-bit RGB image
image_16bit = cv2.merge(channels_16bit)
cv2.imwrite("img16.tiff", image_16bit)
img16 = cv2.imread("img16.tiff", cv2.IMREAD_UNCHANGED)
channels = cv2.split(img16)
channels_16bit = [np.uint16(channel) * 256 for channel in channels]


# Calculate the histogram for each channel
histograms = []
for channel in channels_16bit:
    histogram = cv2.calcHist([img16], [0], None, [65536], [0, 65536])
    histograms.append(histogram)

# Plot the histograms
colors = ('b', 'g', 'r')
titles = ('Blue Channel', 'Green Channel', 'Red Channel')


for histogram, color in zip(histograms, colors):
    plt.plot(histogram, color=color)
    plt.title(titles)
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Histograms')
plt.legend(['Blue', 'Green', 'Red'])
plt.show()
