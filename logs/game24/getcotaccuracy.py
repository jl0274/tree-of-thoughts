import json

with open('gpt-4o-mini_0.7_naive_cot_sample_100_start900_end1000.json') as f:
    data = json.load(f)

total = 0
accurate_items = 0
for entry in data:
    rewards = entry['infos']
    for item in rewards:
        total += 1
        accurate_items += item['r']
accuracy = accurate_items / total
print(f"Accuracy: {accuracy:.2%} ({accurate_items}/{total})")
