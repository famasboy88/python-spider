import re
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

DIR = os.path.dirname(__file__)
cred = credentials.Certificate(os.path.join(DIR, 'service.json'))
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://zywie-2b7c2.firebaseio.com'
})

food_exchange_tag = db.reference().child("usda_food_exchange").get()
food_list = db.reference().child("food_title").get()

for key, category in food_exchange_tag.items():
    for category_key, category_item in category.items():
        usda_kcal = category_item.get("kcal")
        usda_value_grams = category_item.get("value_grams")
        cnt = 0
        for food_key, food_details in food_list.items():
            list_recipe = food_details.get("list_recipe")
            photo_url = food_details.get("photo_url")
            if(photo_url is None):
                photo_url = "http://images.media-allrecipes.com/global/recipes/nophoto/nopicture-910x511.png"
            if(list_recipe is not None):
                r = re.compile("\\b" + category_key + "\\b")
                result = filter(r.search, list_recipe)
                if (list(result)):
                    # print("FoodEx: "+key, "cat: "+category_key, "id: "+food_key,list_recipe, "KCal: "+str(usda_kcal), "perG: "+ str(usda_value_grams))
                    cnt+=1
                    db.reference().child("foodex_usda").child(key).child(category_key).update({
                        "kcal": usda_kcal,
                        "value_grams": usda_value_grams,
                        "no_food_items": cnt
                    })
                    db.reference().child("food_each_category").child(key).child(category_key).child(food_key).update({
                        "list_recipe": list_recipe,
                        "photo_url": photo_url
                    })
