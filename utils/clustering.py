from shapely.geometry import box

def cluster_boxes(boxes, distance_threshold=0.5):
    '''
        Clusters bounding boxes based on the distance between them.

        Args:
            boxes: A list of bounding boxes, where each box is a list or tuple
                        of (x1, y1, x2, y2).
            distance_threshold: The maximum distance between two boxes to be considered
                                part of the same cluster.
    '''

    # Convert bounding boxes to Shapely polygons
    polygons = [box(x1, y1, x2, y2) for x1, y1, x2, y2 in boxes]

    # Merge based on distance
    merged_polygons = []
    while polygons:
        base = polygons.pop(0)
        
        # Find all polygons within the distance threshold
        close = [p for p in polygons if base.distance(p) <= distance_threshold]
        
        # Remove the close polygons from the list
        polygons = [p for p in polygons if p not in close]

        # Merge the close polygons
        for p in close:
            base = base.union(p)
        merged_polygons.append(base)

    # Extract the bounding boxes of the merged polygons
    merged_boxes = [
        (int(p.bounds[0]), int(p.bounds[1]), int(p.bounds[2]), int(p.bounds[3])) for p in merged_polygons
    ]

    return merged_boxes