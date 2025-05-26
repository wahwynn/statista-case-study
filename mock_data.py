import json
import random
from pathlib import Path

from faker import Faker

fake = Faker()

SUBJECTS = ["Economy", "Technology", "Health", "Retail", "Energy"]
MOCK_DATA_FILE = "./mock_data.json"


def generate_mock_data(n=100):
    data_file = Path(MOCK_DATA_FILE)
    if data_file.exists():
        return json.loads(data_file.read_text())

    data = []
    for i in range(n):
        item = {
            "id": i + 1,
            "title": fake.sentence(nb_words=6),
            "subject": random.choice(SUBJECTS),
            "description": fake.paragraph(nb_sentences=3),
            "link": fake.url(),
            "date": fake.date(),
        }
        data.append(item)

    data_file.write_text(json.dumps(data, indent=4))

    return data


if __name__ == "__main__":
    data = generate_mock_data()
    print(f"Created {len(data)} mock entries")
