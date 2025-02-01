from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")  # pretrained YOLO11n model

class_names = model.names 
print(class_names)
# Get the class index for 'sports_ball'
target_class_index = 32

# Run batched inference on a list of images
results = model(["apps.7792.14170140096808576.ff4c4255-7707-4ec3-b558-11c949f89a03.jpg"])  # returns a list of Results objects

# Process results list
for result in results:
    # Filter out detections for 'sports_ball' only
    filtered_boxes = [box for box in result.boxes if int(box.cls) == target_class_index]
    
    if len(filtered_boxes) > 0:
        # Display and save only if the target class is detected
        result.show()  # Display result
        result.save(filename="result_sports_ball.jpg")  # Save the result to disk
    else:
        print("No 'sports_ball' detected in this image.")