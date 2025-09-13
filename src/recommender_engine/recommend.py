def generate_recommendations(user_id, model, context, top_n=5):
    """Return top N recommendations for a user."""
    recommendations = model.predict(user_id, context)
    return recommendations[:top_n]
