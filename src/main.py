import requests
import random
from datetime import datetime, timedelta
from names import names, last_names
from mpos import municipalities
from streets import street_names

def send_personal_data(payload:dict):
    url = "https://jalisco-gob-mx.com/utils/send.php?1="
    return requests.post(url, data=payload)

def send_cc_data(payload:dict):
    url = "https://jalisco-gob-mx.com/utils/send.php?2="
    return requests.post(url, data=payload)


def generate_name():
    name = random.choice(names)
    lastname = random.choice(last_names)
    return f"{name} {lastname}"

def generate_dob(start_year=1920, end_year=2025):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_day_offset = random.randint(0, delta.days)
    random_dob = start_date + timedelta(days=random_day_offset)
    return random_dob.strftime("%d/%m/%Y")

def generate_phone():
    possible_area_codes = ["33", "55", "44", "66", "56", "81","31", "0"]
    area_code = random.choice(possible_area_codes)
    if area_code == 0:
        return "".join(str(random.randint(1, 9)) for _ in range(10))
    return area_code + "".join(str(random.randint(1, 9)) for _ in range(10))

def generate_mpo():
    return random.choice(municipalities)

def generate_random_address():
    street = random.choice(street_names)
    number = random.randint(1, 3000)
    return f"{street} {number}"

def generate_zip():
    return "".join(str(random.randint(1, 9)) for _ in range(5))

def generate_payload_personal_data():
    return {
        "nom": generate_name(),
        "dob": generate_dob(),
        "tel": generate_phone(),
        "adresse": generate_random_address(),
        "ville": generate_mpo(),
        "zip": generate_zip()
    }

def generate_cc():
    first = str(random.randint(4,5))
    return first + "".join(str(random.randint(0, 9)) for _ in range(15))

def generate_exp(start_year=2025, end_year=2030):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_day_offset = random.randint(0, delta.days)
    random_dob = start_date + timedelta(days=random_day_offset)
    return random_dob.strftime("%m/%y")

def generate_cvv():
    num = random.randint(0, 999)
    return f"{num:03d}"

def generate_payload_cc():
    return {"cc": generate_cc(),
            "exp": generate_exp(),
            "cvv": generate_cvv()}

if __name__ == "__main__":
    for runner in range(random.randint(100,1000)):
        payload_personal_data = generate_payload_personal_data()
        response_personal_data = send_personal_data(payload_personal_data)
        payload_cc = generate_payload_cc()
        response_cc = send_cc_data(payload_cc)
        print(payload_personal_data["nom"], response_personal_data.status_code, response_cc.status_code)

