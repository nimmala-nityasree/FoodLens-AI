from transformers import pipeline
from PIL import Image

classifier = pipeline(
    "image-classification",
    model="Shresthadev403/food-image-classification"
)

def predict_food(image_path):

    image = Image.open(image_path).convert("RGB")

    results = classifier(image)

    top = results[0]

    return {
        "food": top["label"].replace("_", " ").lower(),
        "confidence": round(top["score"] * 100, 2)
    }