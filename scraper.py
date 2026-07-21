import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# Στοχευμένες αρχικές σελίδες (seed URLs) για νομικά και επαγγελματικά domains
seed_urls = [
    "https://lawjobs.gr",
    "https://www.randstad.gr"
]

found_domains = set()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

print("Ξεκινάμε την αναζήτηση και φιλτράρισμα για μοναδικά .gr domains...")

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

print(f"Ολοκληρώθηκε! Αποθηκεύτηκαν {len(found_domains)} καθαρά .gr domains στο expired_candidates.txt")
