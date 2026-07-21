import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

seed_urls = [
    "https://lawjobs.gr",
    "https://www.randstad.gr",
    "https://www.kariera.gr",
    "https://www.xe.gr/ergasia"
]

found_domains = set()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for url in seed_urls:
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a', href=True):
                full_url = urljoin(url, link['href'])
                netloc = urlparse(full_url).netloc.lower()
                
                # Φιλτράρισμα: Μόνο καθαρά .gr (χωρίς .com.gr, .net.gr, κλπ.)
                if netloc.endswith('.gr') and not any(netloc.endswith(ext) for ext in ['.com.gr', '.net.gr', '.org.gr', '.edu.gr', '.gov.gr', '.co.gr']):
                    parts = netloc.split('.')
                    if len(parts) >= 2 and parts[-1] == 'gr':
                        root_domain = f"{parts[-2]}.{parts[-1]}"
                        found_domains.add(root_domain)
    except Exception:
        pass

with open("expired_candidates.txt", "w", encoding="utf-8") as f:
    for domain in sorted(found_domains):
        f.write(domain + "\n")

print(f"Ολοκληρώθηκε! Αποθηκεύτηκαν {len(found_domains)} καθαρά .gr root domains.")
