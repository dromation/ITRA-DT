import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the 8-bit image
image = cv2.imread("template_high.png", 0)

# Calculate the histogram
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# Plot the histogram
plt.plot(histogram)
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
