import pandas as pd

# Load nutrition database
nutrition_df = pd.read_csv("data/nutrition.csv")


def get_nutrition(food_name):
    """
    Returns nutrition details for a food.
    """

    food_name = food_name.lower().strip()

    for _, row in nutrition_df.iterrows():
        if row["Food"].lower() == food_name:
            return {
                "Calories": row["Calories"],
                "Protein": row["Protein"],
                "Carbs": row["Carbs"],
                "Fat": row["Fat"],
            }

    # If food not found
    return {
        "Calories": "N/A",
        "Protein": "N/A",
        "Carbs": "N/A",
        "Fat": "N/A",
    }


def get_recommendation(food_name):
    """
    Simple healthy recommendation based on food.
    """

    recommendations = {
        "pizza": "Pair it with a fresh salad and limit sugary drinks.",
        "burger": "Choose a whole-wheat bun and add more vegetables.",
        "french fries": "Enjoy in moderation and pair with grilled protein.",
        "ice cream": "Keep portions small and add fresh fruit.",
        "apple": "Great choice! Rich in fiber and vitamins.",
        "banana": "Excellent pre-workout snack with natural energy.",
        "salad": "Excellent choice! Consider adding lean protein for a balanced meal.",
        "fried rice": "Pair it with vegetables and reduce extra oil.",
    }

    return recommendations.get(
        food_name.lower(),
        "Enjoy a balanced meal with plenty of vegetables and water."
    )