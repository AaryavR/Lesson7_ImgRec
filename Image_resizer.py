import cv2

image = cv2.imread("image.png")

sizex = int(input("What do you want the x size to be (px): "))
sizey = int(input("what do you want the y size to be (px): "))

cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded Image', sizex, sizey)

cv2.imshow('Loaded Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Image Dimensions: {image.shape}")