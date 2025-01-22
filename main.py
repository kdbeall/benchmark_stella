import time
from sentence_transformers import SentenceTransformer

import torch
print(torch.cuda.is_available())  # Should return True if a GPU is available
print(torch.cuda.get_device_name(0))  # Prints the name of the GPU

# Load the Stella model with 700-dimensional embedding
device = "cuda" if torch.cuda.is_available() else "cpu"
model = SentenceTransformer("dunzhang/stella_en_400M_v5", trust_remote_code=True).to(device)

# Business texts to benchmark
business_texts = [
    """
    At QuantumEdge Solutions, we specialize in creating cutting-edge software tailored to your business needs. 
    Our team of expert developers and designers is dedicated to delivering scalable and secure solutions 
    that drive growth and efficiency. Whether you're a startup or an enterprise, we help you leverage 
    the latest in AI and cloud technologies to stay ahead of the competition.
    """,
    """
    Welcome to Luxora, your one-stop shop for premium home goods and lifestyle essentials. 
    From luxurious bedding to eco-friendly kitchenware, we curate products that bring style 
    and sustainability to your everyday life. Enjoy free shipping on orders over $50 and 
    experience customer service that puts your satisfaction first.
    """,
    """
    Find your dream home with Skyline Realty. With over a decade of experience in the real estate market, 
    we pride ourselves on connecting buyers with properties that fit their lifestyle and budget. 
    From cozy starter homes to luxurious estates, our agents are here to guide you every step of the way. 
    Discover the difference with Skyline Realty.
    """,
    """
    At Harmony Wellness Studio, we believe in nurturing the mind, body, and spirit. 
    Our holistic approach includes yoga classes, meditation workshops, and personalized wellness plans 
    designed to help you achieve balance and vitality. Join our community and take the first step 
    toward a healthier, happier you.
    """,
    """
    Secure your future with Vanguard Wealth Advisors. Our experienced financial planners offer personalized 
    investment strategies, retirement planning, and wealth management services. Whether you're starting your 
    journey or refining your portfolio, we're here to help you achieve your financial goals with confidence.
    """,
    """
    Unlock your potential with Elevate Learning Academy. We provide online courses, workshops, and certifications 
    in fields like technology, business, and design. Learn from industry experts and gain the skills you need 
    to thrive in today's competitive job market. Start your journey with Elevate Learning Academy today.
    """,
    """
    Explore the world with Wanderlust Travel Co. Whether you're dreaming of a tropical getaway or a cultural adventure, 
    we offer curated travel packages and personalized itineraries that make planning your next trip effortless. 
    Let us help you create unforgettable memories with Wanderlust Travel Co.
    """,
    """
    Indulge in the rich flavors of the Mediterranean with Olive Grove Catering. 
    Our menu features authentic dishes made with fresh, locally sourced ingredients. 
    Perfect for weddings, corporate events, or intimate gatherings, our catering services 
    bring a touch of elegance and exceptional taste to any occasion.
    """,
    """
    Transform your body and mind at Apex Fitness. Our state-of-the-art gym offers a variety of workout classes, 
    personal training sessions, and wellness programs tailored to your goals. Whether you're just starting out 
    or are a seasoned athlete, Apex Fitness is here to support your fitness journey.
    """,
    """
    Boost your online presence with Zenith Digital Marketing. From SEO to social media management, 
    we offer data-driven strategies that help your brand stand out in the digital landscape. 
    Let us help you connect with your audience and drive meaningful results for your business.
    """
]

# Benchmark the embedding process
start_time = time.time()
embeddings = model.encode(business_texts, prompt_name="s2p_query", device=device)
end_time = time.time()

# Calculate time per embedding
total_time = end_time - start_time
time_per_embedding = total_time / len(business_texts)

# Output results
total_time, time_per_embedding
