import torch
import torchvision
from torchvision.transforms import functional as F
import cv2
import numpy as np
from PIL import Image

# Load the pre-trained Faster R-CNN model
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()  # Set the model to evaluation mode

# Function to perform detection
def detect_balls(image_path):
    # Load and prepare the image
    image = Image.open(image_path).convert("RGB")
    image_tensor = F.to_tensor(image).unsqueeze(0)

    # Perform inference
    with torch.no_grad():
        predictions = model(image_tensor)

    # Get the boxes and scores
    boxes = predictions[0]['boxes']
    scores = predictions[0]['scores']
    
    # Filter boxes with a score threshold (e.g., 0.5)
    threshold = 0.5
    boxes = boxes[scores > threshold].numpy()

    # Draw bounding boxes on the image
    img_cv2 = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    for box in boxes:
        x1, y1, x2, y2 = box.astype(int)
        cv2.rectangle(img_cv2, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Display the image with detections
    cv2.imshow("Ball Detection", img_cv2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Test the function with an image
detect_balls('apps.7792.14170140096808576.ff4c4255-7707-4ec3-b558-11c949f89a03.jpg')  # Replace with your image path
