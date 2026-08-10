import requests
import json
import openai
import datetime

OBSIDIAN_API = "http://localhost:27123"
VAULT_NAME = "knowledge-forest"
LOG_PATH = "System/operation-log.md"

def log(message):
    with open(LOG_PATH, "a") as f:
        f.write(f"{datetime.datetime.now().isoformat()} - {message}\n")

def search_notes(query):
    resp = requests.post(f"{OBSIDIAN_API}/search/", json={"query": query})
    return resp.json()

def read_note(path):
    resp = requests.get(f"{OBSIDIAN_API}/vault/{VAULT_NAME}/{path}")
    return resp.text

def create_note(path, content):
    resp = requests.post(f"{OBSIDIAN_API}/vault/{VAULT_NAME}/{path}", data=content.encode('utf-8'))
    return resp.status_code == 200

def bloom(question_path):
    log(f"开始开花：{question_path}")
    question_content = read_note(question_path)
    relevant = search_notes(" ".join(question_content.split()[:30]))
    with open("提示词（prompts）/生成花朵（generate-flowers）.md", "r") as f:
        prompt_template = f.read()
    prompt = prompt_template.replace("{{question}}", question_content).replace("{{knowledge_chunks}}", json.dumps(relevant))
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user", "content": prompt}]
    )
    flowers_text = response.choices[0].message.content
    flower_list = flowers_text.split("## 方案")
    for i, flower in enumerate(flower_list):
        if i == 0:
            continue
        flower_content = f"## 方案{flower.strip()}"
        create_note(f"Flowers/花-{question_path}-{i}.md", flower_content)
    log(f"完成开花：创建了{len(flower_list)-1}朵花")

if __name__ == "__main__":
    bloom("Questions/如何提升用户留存.md")