import cv2
import matplotlib.pyplot as plt

image_path = 'example.jpg'
# Load the image
image = cv2.imread(image_path)
# Convert the image from BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# get img dimensions
height, width, _ = image_rgb.shape

# step 2: draw two rectangles around interesting regions
# Rectangle 1: top-left corner
rect1_width, rect1_height = 150, 150
top_left1 = (20, 20)
bottom_right1 = (top_left1[0] + rect1_width, top_left1[1] + rect1_height)
cv2.rectangle(image_rgb, top_left1, bottom_right1, (0, 255, 255), 3)

# Rectangle 2: bottom-right corner
rect2_width, rect2_height = 200, 150
top_left2 = (width - rect2_width - 20, height - rect2_height - 20)
bottom_right2 = (top_left2[0] + rect2_width, top_left2[1] + rect2_height)
cv2.rectangle(image_rgb, top_left2, bottom_right2, (255, 0, 255), 3)

# step 3: draw circles at the center of each rectangle
center1_x = top_left1[0] + rect1_width // 2
center1_y = top_left1[1] + rect1_height // 2
center2_x = top_left2[0] + rect2_width // 2
center2_y = top_left2[1] + rect2_height // 2
cv2.circle(image_rgb, (center1_x, center1_y), 15, (0, 255, 0), -1)
cv2.circle(image_rgb, (center2_x, center2_y), 15, (0, 255, 0), -1)

# step 4: drawing connecting lines between the centers of the rectangles
cv2.line(image_rgb, (center1_x, center1_y), (center2_x, center2_y), (0, 255, 0), 3)

# step 5: add text labels for regions and centers
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_rgb, 'Region 1', (top_left1[0], top_left1[1] - 10), font, 0.7, (255, 255, 0), 2, cv2.LINE_AA)
cv2.putText(image_rgb, 'Region 2', (top_left2[0], top_left2[1] - 10), font, 0.7, (255, 255, 0), 2, cv2.LINE_AA)
cv2.putText(image_rgb, 'Center 1', (center1_x - 40, center1_y + 30), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(image_rgb, 'Center 2', (center2_x - 40, center2_y + 30), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

# step 6: add Bi-directional arrows representing height
arrow_start = (width - 50, 20)
arrow_end = (width - 50, height - 20)
cv2.arrowedLine(image_rgb, arrow_start, arrow_end, (255, 255, 0), 3, tipLength=0.05)
cv2.arrowedLine(image_rgb, arrow_end, arrow_start, (255, 255, 0), 3, tipLength=0.05)

# annotate height value
height_label_pos = (arrow_start[0] - 150, (arrow_start[1] + arrow_end[1]) // 2)
cv2.putText(image_rgb, f'Height: {height}px', height_label_pos, font, 0.8, (255, 255, 0), 2, cv2.LINE_AA)
# step 7: display the annotated image
plt.figure(figsize=(12, 8))
plt.imshow(image_rgb)
plt.title('Annotated Image with Regions, Centers, and Bi-directional Height Arrows')
plt.axis('off')
plt.show()