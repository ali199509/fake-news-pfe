from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Chargement du modèle préentraîné
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=2)
model.eval()

# Texte à prédire
text = "COVID vaccine causes autism and cancer!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

# Inférence
with torch.no_grad():
    outputs = model(**inputs)
    predicted = torch.argmax(outputs.logits, dim=1).item()

label = "Fake News" if predicted == 1 else "Real News"
print(f"Texte : {text}")
print(f"Résultat : {label}")
