import cv2

def crop_image(image_path, box):
    '''
        Crop an image using the given bounding box.

        Args:
            image_path (str): Path to the image file.
            box (tuple): Bounding box coordinates (x1, y1, x2, y2).

        Returns:
            cropped_image: Cropped image.
    '''

    # Load the image
    image = cv2.imread(image_path)

    # Extract box coordinates
    x1, y1, x2, y2 = tuple(box)

    # Crop the image
    cropped_image = image[y1:y2, x1:x2]
    
    return cropped_image

def show_images(images):
    '''
        Display a list of images.

        Args:
            images: A list of images to display.
    '''

    for i, img in enumerate(images):
        cv2.imshow(f"Image {i}", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def save_image(image, output_path):
    '''
        Save an image to a file.

        Args:
            image: Image to save.
            output_path (str): Path to save the image.
    '''

    cv2.imwrite(output_path, image)

def draw_boxes(image_path, boxes):
    '''
        Draw bounding boxes on an image.

        Args:
            image_path (str): Path to the image file.
            boxes: List of bounding boxes.

        Returns:
            image: Image with bounding boxes drawn.
    '''

    # Load the image
    image = cv2.imread(image_path)

    # Draw bounding boxes
    for box in boxes:
        x1, y1, x2, y2 = box
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return image