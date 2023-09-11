import cv2
import torch
import cvlib as cv

class_names = ['Rice Black Bug', 'Rice Bug', 'Rice Stem Borer']

# Define color map for each class
class_colors = {'Rice Black Bug': (0, 0, 255), 
                'Rice Bug': (0, 255, 255), 
                'Rice Stem Borer': (0, 255, 0)}

detected_classes = []

def detect_count_classes(frame, model, conf_thres=0.5, iou_thres=0.5):
    # Get detections
    results = model(frame)

    # Initialize dictionary for counting classes
    class_counts = {class_name: 0 for class_name in class_names}

    # Initialize list for storing detected class names
    

    # Process detections
    for result in results.xyxy:
        if result is not None:
        # Get class indices, confidence, and bounding boxes
            class_indices = result[:, -1].int()
            confidences = result[result[:, -2] >= 0.5, -2].tolist()
            boxes = result[:, :4]


            # Plot boxes and labels on frame
            # Plot boxes and labels on frame
            for box, class_index, confidence in zip(boxes, class_indices, confidences):
                class_name = class_names[class_index]

                # Get color for current class
                color = class_colors[class_name]
                
                # Add class name and confidence to label
                label = class_name + f" ({confidence:.2f})"

                frame = cv2.rectangle(frame, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), color, 2)
                frame = cv2.putText(frame, label, (int(box[0]), int(box[1])-10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

                # Count the detected class
                class_counts[class_name] += 1

                # Store the detected class name
                detected_classes.append(class_name)

    # Print the detected class names
    #print(detected_classes)

    return frame, class_counts
