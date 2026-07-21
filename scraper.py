import requests
from bs4 import BeautifulSoup

# Στοχευμένες αρχικές σελίδες (seed URLs) για νομικά και επαγγελματικά domains
seed_urls = [
    "https://lawjobs.gr",
    "https://www.randstad.gr"
]

print("Ξεκινάμε την αναζήτηση για .gr συνδέσμους στις στοχευμένες πηγές...")

total_found = 0

for url in seed_urls:
    print(f"\nΣύνδεση με: {url}")
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            found_count = 0
            for link in soup.find_all('a', href=True):
                href = link['href']
                if '.gr' in href:
                    print(f"  -> Βρέθηκε: {href}")
                    found_count += 1
                    total_found += 1
                    
            print(f"Βρέθηκαν {found_count} σύνδεσμοι σε αυτή τη σελίδα.")
        else:
            print(f"Δεν ήταν δυνατή η πρόσβαση. Κωδικός: {response.status_code}")
    except Exception as e:
        print(f"Σφάλμα κατά τη σύνδεση: {e}")

print(f"\nΟλοκληρώθηκε! Συνολικά βρέθηκαν {total_found} σχετικές διευθύνσεις.")
