import json
import re

def clean_json_string(json_string):
    # Menghapus karakter kontrol yang tidak valid
    json_string = re.sub(r'[\x00-\x1F\x7F]', '', json_string)
    return json_string

def convert_jsonl_to_conversation_format(input_file, output_file):
    conversations = []
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            # Bersihkan karakter kontrol yang tidak valid
            clean_line = clean_json_string(line)
            
            try:
                entry = json.loads(clean_line)
                prompt = entry['prompt']
                completion = entry['completion']
                
                conversation = {
                    "messages": [
                        {"role": "system", "content": "Selamat Datang"},
                        {"role": "user", "content": prompt},
                        {"role": "assistant", "content": completion}
                    ]
                }
                conversations.append(conversation)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                continue
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for conversation in conversations:
            json.dump(conversation, outfile)
            outfile.write('\n')

# File input dan output
input_file = 'D:\\Akademik\\Deploy Model\\modules\\generative_chatbot\\gpt_train2.jsonl'  # ganti dengan nama file input kamu
output_file = 'D:\\Akademik\\Deploy Model\\modules\\generative_chatbot\\formatted_gpt_train2.jsonl'  # ganti dengan nama file output yang diinginkan

convert_jsonl_to_conversation_format(input_file, output_file)