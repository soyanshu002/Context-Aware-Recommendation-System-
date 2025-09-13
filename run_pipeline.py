from src.data_preprocessing.load_data import load_user_data, load_product_data, load_context_data
from src.data_preprocessing.clean_data import clean_user_data, clean_product_data
from src.data_preprocessing.feature_engineering import add_time_features, encode_categorical
from src.models.context_aware_model import ContextAwareRecommender
from src.recommender_engine.simulation import simulate_ctr

# Load data
users = load_user_data('data/raw/users.csv')
products = load_product_data('data/raw/products.csv')
context = load_context_data('data/raw/context.csv')

# Clean data
users = clean_user_data(users)
products = clean_product_data(products)

# Feature engineering
users = add_time_features(users)
users = encode_categorical(users, ['location'])

# Train model
model = ContextAwareRecommender()
model.train(users)  # placeholder

# Simulate CTR
ctr = simulate_ctr(model, users)
print(f"Simulated CTR: {ctr:.2%}")
