import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# Διευρυμένες πηγές για Job Board και Νομική Εταιρεία
seed_urls = [
    "https://lawjobs.gr",
    "https://www.randstad.gr",
    "https://www.kariera.gr",
    "https://www.xe.gr/ergasia"
]

found_domains = set()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

print("Ξεκινάμε τη συλλογή από τις διευρυμένες πηγές...")

for url in seed_urls:
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a', href=True):
                full_url = urljoin(url, link['href'])
                netloc = urlparse(full_url).netloc
                if netloc.endswith('.gr') and netloc:
                    found_domains.add(netloc)
    except Exception:
        pass

# Αποθήκευση στο αρχείο
with open("expired_candidates.txt", "w", encoding="utf-8") as f:
    for domain in sorted(found_domains):
        f.write(domain + "\n")

print(f"Ολοκληρώθηκε! Αποθηκεύτηκαν συνολικά {len(found_domains)} .gr domains.")
