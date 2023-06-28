import cv2
import numpy as np

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

# Create a random 16-bit image
#image_16bit = np.random.randint(0, 65536, size=(1000, 1000), dtype=np.uint16)
# Search for values within the 8-bit range (0-255)
#indices = np.where((image_16bit >= 0) & (image_16bit <= 255))
# Get the coordinates of the matching values
#coordinates = list(zip(indices[0], indices[1]))

# Print the coordinates of the matching values
#for coord in coordinates:
#    print(f"Found value within 8-bit range at coordinates: {coord}")

print(channels_16bit)
# Display the 16-bit image
cv2.imshow('16-bit Image', image_16bit)
cv2.waitKey(0)
cv2.destroyAllWindows()



#16 BIT IMAGE AT -142 FARENHEIT TEMPEARTURE IS image set with pixels to 0

flow_image_16bit = np.zeros((height, width), dtype=np.uint16)

#16 BIT IMAGE AT 1832 FARENHEIT DEGREES IS image st with pixels to 65535

fhigh_image_16bit = np.full((height, width), 65535, dtype=np.uint16)

pixel_scale = 65535
farenheit_scale = 1974

#16bit a pixelheit_degree = pixel_scale / farenheit_scale ; this is at 33.199
pixelheit_degree = pixel_scale / farenheit_scale

#room farenheit temperature is 68, wich is 2257.5379
TFroom = pixelheit_degree * 68