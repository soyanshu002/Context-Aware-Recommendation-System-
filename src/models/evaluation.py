def compute_ctr(predictions, actual_clicks):
    """Compute click-through rate."""
    total_clicks = sum(actual_clicks)
    total_recommended = len(predictions)
    return total_clicks / total_recommended if total_recommended > 0 else 0
