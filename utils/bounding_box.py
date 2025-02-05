import cv2
from config.config import PADDING_BB_X, PADDING_BB_Y

def padding_box_function(box, image):
    '''
        Maps a bounding box to a new box with padding.

        Args: 
            box: Bounding box coordinates (x1, y1, x2, y2).
            image: Image of the bounding box.

        Returns:
            A new bounding box with a padding.
    '''

    x1, y1, x2, y2 = map(int, box) # Extract coordinates
        
    # Calculate padding
    width = x2 - x1 # Width of the box
    height = y2 - y1 # Height of the box
    x_padding = int(width * PADDING_BB_X)
    y_padding = int(height * PADDING_BB_Y)

    # Apply padding (clamping to image boundaries)
    x1 = max(0, x1 - x_padding)
    y1 = max(0, y1 - y_padding)
    x2 = min(image.shape[1], x2 + x_padding)  # Fits to image width
    y2 = min(image.shape[0], y2 + y_padding)  # Fits to image height

    return (x1, y1, x2, y2)

def padding_bounding_boxes(boxes, image_path):
    """
        Maps each box to a new box with a padding.

        Args:
            boxes: List of bounding boxes.
            image_path: path to image file.

        Returns:
            A new list of boxes with a padding.
    """

    image = cv2.imread(image_path) # Load the image

    return [padding_box_function(box, image) for box in boxes]

def extract_boxes(yolo_results):
    """
        Extract bounding boxes from the YOLO detection results.

        Args: 
            yolo_results: List of detected objects.

        Returns:
            bounding_boxes: List of bounding boxes.
    """

    boxes = []

    if hasattr(yolo_results, 'boxes'):
        if yolo_results.boxes is not None and yolo_results.boxes.xyxy is not None:
            xyxy = yolo_results.boxes.xyxy.cpu().numpy() # Extract boxes and convert to numpy
            for box in xyxy:
                x1, y1, x2, y2 = map(int, box)  # Convert to integers
                boxes.append((x1, y1, x2, y2))
    elif isinstance(yolo_results, list): # handle list of results (multiple images)
        for res in yolo_results:
            if hasattr(res, 'boxes'):
                if res.boxes is not None and res.boxes.xyxy is not None:
                    xyxy = res.boxes.xyxy.cpu().numpy()
                    for box in xyxy:
                        x1, y1, x2, y2 = map(int, box)
                        boxes.append((x1, y1, x2, y2))
    else:
        print("Unsupported results format.")
        return []

    return boxes