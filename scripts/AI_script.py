def AI(AI_PATH):
    from transformers import AutoModelForCausalLM, AutoTokenizer

    device = "cuda" # the device to load the model onto

    tokenizer = AutoTokenizer.from_pretrained(AI_PATH)
    model = AutoModelForCausalLM.from_pretrained(AI_PATH)

    messages = [
        {"role": "user", "content": "Quel est votre condiment préféré ?"},
        {"role": "assistant", "content": "En fait, j'aime bien presser du jus de citron frais. Il ajoute juste ce qu'il faut de saveur piquante à tout ce que je prépare dans la cuisine !"},
        {"role": "user", "content": "Avez-vous des recettes de mayonnaise ?"}
    ]

    encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt")

    model_inputs = encodeds.to(device)
    model.to(device)

    generated_ids = model.generate(model_inputs, max_new_tokens=1000, do_sample=True)
    decoded = tokenizer.batch_decode(generated_ids)
    print(decoded[0])
