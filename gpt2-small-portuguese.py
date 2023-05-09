# Importa as classes AutoTokenizer e AutoModelForCausalLM da biblioteca Transformers
from transformers import AutoTokenizer, AutoModelForCausalLM

# Carrega o tokenizer pré-treinado para o modelo "pierreguillou/gpt2-small-portuguese"
tokenizer = AutoTokenizer.from_pretrained("pierreguillou/gpt2-small-portuguese")

# Carrega o modelo pré-treinado "pierreguillou/gpt2-small-portuguese" utilizando a classe AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained("pierreguillou/gpt2-small-portuguese")

# Define o prompt de entrada
prompt = 'Qual o sentido da vida?'

# Codifica o prompt em tokens de entrada para o modelo
input_ids = tokenizer.encode(prompt, return_tensors='pt')

# Gera 50 tokens de saída a partir do prompt de entrada usando o modelo
output = model.generate(input_ids=input_ids, max_length=50, num_beams=5, no_repeat_ngram_size=2, early_stopping=True)

# Decodifica os tokens de saída em texto legível utilizando o tokenizer
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

# Imprime o texto gerado pelo modelo
print(generated_text)
