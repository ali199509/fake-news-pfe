from kafka import KafkaProducer
import json
import time
import random

# Connexion au serveur Kafka local
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

# Liste de faux tweets simulés
fake_tweets = [
    {"text": "🚨BREAKING: COVID vaccine causes 1 in 3 deaths!!!", "user": "bot_01"},
    {"text": "NASA confirms Earth is flat!", "user": "bot_02"},
    {"text": "Bill Gates is controlling minds with 5G", "user": "bot_03"},
    {"text": "Aliens spotted in Paris - government hides the truth", "user": "bot_04"}
]

# Envoi boucle continue
while True:
    tweet = random.choice(fake_tweets)
    tweet["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")
    producer.send("twitter-topic", tweet)
    print("Envoyé :", tweet)
    time.sleep(2)  # Pause entre les messages
