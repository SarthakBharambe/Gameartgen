def load_category_prompts(file_path="prompts/categories.txt"):
    category_map = {}
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                key, value = line.strip().split(":", 1)
                category_map[key.strip()] = value.strip()
    return category_map
