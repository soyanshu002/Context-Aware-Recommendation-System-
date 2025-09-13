class BaseRecommender:
    def __init__(self):
        pass

    def train(self, data):
        """Train the model."""
        raise NotImplementedError

    def predict(self, user_id, context):
        """Generate recommendations."""
        raise NotImplementedError
