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