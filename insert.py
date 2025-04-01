import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')  # Replace 'your_project_name' with your actual project name
django.setup()


from django.conf import settings
from game.models import Game, Category  



data = [
    {"tag_name": "Taarak Mehta Ka Ooltah Chashmah", "num_searches": "450,000", "category": "Television"},
    {"tag_name": "Bigg Boss", "num_searches": "450,000", "category": "Television"},
    {"tag_name": "The Kapil Sharma Show", "num_searches": "74,000", "category": "Television"},
    {"tag_name": "Kaun Banega Crorepati", "num_searches": "110,000", "category": "Television"},
    {"tag_name": "Indian Idol", "num_searches": "110,000", "category": "Television"},
    {"tag_name": "Comedy Nights with Kapil", "num_searches": "12,100", "category": "Television"},
    {"tag_name": "Dance India Dance", "num_searches": "33,100", "category": "Television"},
    {"tag_name": "Roadies", "num_searches": "90,500", "category": "Television"},
    {"tag_name": "Khatron Ke Khiladi", "num_searches": "90,500", "category": "Television"},
    {"tag_name": "Saath Nibhaana Saathiya", "num_searches": "60,500", "category": "Television"},
    {"tag_name": "Naagin", "num_searches": "40,500", "category": "Television"},
    {"tag_name": "Yeh Rishta Kya Kehlata Hai", "num_searches": "1,000,000", "category": "Television"},
    {"tag_name": "CID", "num_searches": "673,000", "category": "Television"},
    {"tag_name": "Bhabiji Ghar Par Hai", "num_searches": "22,200", "category": "Television"},
    {"tag_name": "Kumkum Bhagya", "num_searches": "301,000", "category": "Television"},
    {"tag_name": "Jasprit Bumrah", "num_searches": "1,000,000", "category": "Cricket"},
    {"tag_name": "Shikhar Dhawan", "num_searches": "550,000", "category": "Cricket"},
    {"tag_name": "KL Rahul", "num_searches": "1,500,000", "category": "Cricket"},
    {"tag_name": "Sourav Ganguly", "num_searches": "301,000", "category": "Cricket"},
    {"tag_name": "Sunil Gavaskar", "num_searches": "301,000", "category": "Cricket"},
    {"tag_name": "Yuvraj Singh", "num_searches": "450,000", "category": "Cricket"},
    {"tag_name": "Ravindra Jadeja", "num_searches": "1,220,000", "category": "Cricket"},
    {"tag_name": "Anil Kumble", "num_searches": "135,000", "category": "Cricket"},
    {"tag_name": "Rahul Dravid", "num_searches": "450,000", "category": "Cricket"},
    {"tag_name": "Shubman Gill", "num_searches": "3,350,000", "category": "Cricket"},
    {"tag_name": "Prithvi Shaw", "num_searches": "301,000", "category": "Cricket"},
    {"tag_name": "Mohammed Shami", "num_searches": "1,220,000", "category": "Cricket"},
    {"tag_name": "Navdeep Saini", "num_searches": "60,500", "category": "Cricket"},
    {"tag_name": "IIT Bombay", "num_searches": "301,000", "category": "Education"},
    {"tag_name": "IIM Ahmedabad", "num_searches": "135,000", "category": "Education"},
    {"tag_name": "Amartya Sen", "num_searches": "74,000", "category": "Education"},
    {"tag_name": "APJ Abdul Kalam", "num_searches": "450,000", "category": "Education"},
    {"tag_name": "Dr. B.R. Ambedkar", "num_searches": "0", "category": "Education"},
    {"tag_name": "Raghuram Rajan", "num_searches": "60,500", "category": "Education"},
    {"tag_name": "Satyendra Nath Bose", "num_searches": "33,100", "category": "Education"},
    {"tag_name": "Venkatraman Ramakrishnan", "num_searches": "12,100", "category": "Education"},
    {"tag_name": "Har Gobind Khorana", "num_searches": "12,100", "category": "Education"},
    {"tag_name": "Vikram Sarabhai", "num_searches": "201,000", "category": "Education"},
    {"tag_name": "Meghnad Saha", "num_searches": "14,800", "category": "Education"},
    {"tag_name": "Srinivasa Ramanujan", "num_searches": "135,000", "category": "Education"},
    {"tag_name": "Nirmala Sitharaman", "num_searches": "368,000", "category": "Education"},
    {"tag_name": "Mahatma Gandhi", "num_searches": "673,000", "category": "Indian History"},
    {"tag_name": "Jawaharlal Nehru", "num_searches": "368,000", "category": "Indian History"},
    {"tag_name": "Bhagat Singh", "num_searches": "550,000", "category": "Indian History"},
    {"tag_name": "Sardar Vallabhbhai Patel", "num_searches": "246,000", "category": "Indian History"},
    {"tag_name": "Subhas Chandra Bose", "num_searches": "550,000", "category": "Indian History"},
    {"tag_name": "Indira Gandhi", "num_searches": "550,000", "category": "Indian History"},
    {"tag_name": "Rajiv Gandhi", "num_searches": "301,000", "category": "Indian History"},
    {"tag_name": "Lal Bahadur Shastri", "num_searches": "246,000", "category": "Indian History"},
    {"tag_name": "Sarojini Naidu", "num_searches": "201,000", "category": "Indian History"},
    {"tag_name": "Chandrasekhar Azad", "num_searches": "201,000", "category": "Indian History"},
    {"tag_name": "Rani Lakshmi Bai", "num_searches": "201,000", "category": "Indian History"},
    {"tag_name": "Tipu Sultan", "num_searches": "135,000", "category": "Indian History"},
    {"tag_name": "Mangal Pandey", "num_searches": "110,000", "category": "Indian History"},
    {"tag_name": "Koo", "num_searches": "22,200", "category": "Social Media"},
    {"tag_name": "ShareChat", "num_searches": "1,500,000", "category": "Social Media"},
    {"tag_name": "Moj", "num_searches": "165,000", "category": "Social Media"},
    {"tag_name": "Chingari", "num_searches": "18,100", "category": "Social Media"},
    {"tag_name": "Josh", "num_searches": "110,000", "category": "Social Media"},
    {"tag_name": "Gaana", "num_searches": "110,000", "category": "Social Media"},
    {"tag_name": "MX TakaTak", "num_searches": "22,200", "category": "Social Media"},
]


image_dir = os.path.join(settings.MEDIA_ROOT, 'game_images')

for item in data:
    category, created = Category.objects.get_or_create(name=item["category"])

    image_filename = item["tag_name"].replace(" ", "_")  
    image_path = None
    for ext in ['.jpg', '.jpeg', '.png']:  
        potential_image_path = os.path.join(image_dir, image_filename + ext)
        if os.path.exists(potential_image_path):
            image_path = 'game_images/' + image_filename + ext 
            break

    Game.objects.create(
        tag_name=item["tag_name"],
        num_searches=int(item["num_searches"].replace(",", "")),
        category=category,
        image=image_path
    )
