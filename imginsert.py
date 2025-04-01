import os
import django
from django.core.files import File
from django.core.files.storage import default_storage

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')  

from django.conf import settings
from game.models import Game

image_dir = os.path.join(settings.MEDIA_ROOT, 'game_images')

print("Files in image directory:")
for root, dirs, files in os.walk(image_dir):
    for file in files:
        print(os.path.join(root, file))

for game in Game.objects.all():
    image_filename = game.tag_name.replace(' ', '_')
    image_path = None
    
    for ext in ['.jpg', '.jpeg', '.png']:
        potential_image_path = os.path.join(image_dir, image_filename + ext)
        print(f"Checking path: {potential_image_path}")  
        
        if os.path.exists(potential_image_path):
            image_path = 'game_images/' + image_filename + ext
            break

    if image_path:
        with default_storage.open(image_path, 'rb') as f:
            game.image.save(image_path, File(f))
        game.save()
        print(f"Updated image for {game.tag_name}")
    else:
        print(f"No image found for {game.tag_name}")
