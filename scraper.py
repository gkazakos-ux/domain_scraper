import requests
from bs4 import BeautifulSoup

# Η πρώτη μας δοκιμαστική σελίδα (seed URL) για να ψάξουμε για .gr συνδέσμους
seed_url = "https://www.google.com" 

print(f"Ξεκινάμε την αναζήτηση από τη διεύθυνση: {seed_url}")

try:
    response = requests.get(seed_url, timeout=10)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Ψάχνουμε για συνδέσμους (.gr) μέσα στη σελίδα
        found_count = 0
        for link in soup.find_all('a', href=True):
            href = link['href']
            if '.gr' in href:
                print(f"Βρέθηκε σύνδεση: {href}")
                found_count += 1
                
        print(f"Ολοκληρώθηκε! Βρέθηκαν συνολικά {found_count} σχετικές διευθύνσεις.")
    else:
        print(f"Δεν μπόρεσε να ανοίξει η σελίδα. Κωδικός: {response.status_code}")
except Exception as e:
    print(f"Παρουσιάστηκε κάποιο σφάλμα: {e}")
