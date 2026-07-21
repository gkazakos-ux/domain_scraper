import requests
from bs4 import BeautifulSoup

seed_urls = [
    "https://lawjobs.gr",
    "https://www.randstad.gr"
]

found_domains = set()

print("Ξεκινάμε την αναζήτηση για .gr συνδέσμους...")

for url in seed_urls:
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a', href=True):
                href = link['href']
                if '.gr' in href:
                    found_domains.add(href)
    except Exception as e:
        pass

with open("expired_candidates.txt", "w", encoding="utf-8") as f:
    for domain in sorted(found_domains):
        f.write(domain + "\n")

print(f"Ολοκληρώθηκε! Αποθηκεύτηκαν {len(found_domains)} μοναδικά domains στο expired_candidates.txt")
