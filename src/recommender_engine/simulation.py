def simulate_ctr(model, test_data):
    """Simulate CTR on test dataset."""
    ctrs = []
    for _, row in test_data.iterrows():
        user_id = row['user_id']
        context = {'hour': row['hour'], 'location': row['location']}
        recommended = model.predict(user_id, context)
        ctr = 1 if row['clicked_item'] in recommended else 0
        ctrs.append(ctr)
    return sum(ctrs) / len(ctrs)
