import sys

from PIL import Image
from PIL import ImageDraw
from google.cloud import vision_v1p3beta1 as vision

def localize_objects_uri(uri):
    client = vision.ImageAnnotatorClient()

    image = vision.types.Image()
    image.source.image_uri = uri

    objects = client.object_localization(image=image).localized_object_annotations
    return objects

if __name__ == '__main__':
    uri = sys.argv[1]
    print('Localize objects from {}'.format(uri))

    objects = localize_objects_uri(uri)
    print('Number of objects found: {}\n'.format(len(objects)))
    for obj in objects:
        print('{} (confidence: {})'.format(obj.name, obj.score))
        print('Normalized bounding polygon vertices: ')
        for vertex in obj.bounding_poly.normalized_vertices:
            print('- ({}, {})'.format(vertex.x, vertex.y))
