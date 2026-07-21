import socket
import itertools

# Λέξεις-κλειδιά που ταιριάζουν στους τομείς σου (job boards & νομικά)
keywords_part1 = ["law", "legal", "job", "jobs", "career", "kariera", "hr", "work", "Lex", "attorney"]
keywords_part2 = ["greece", "hellas", "GR", "Athens", "Thessaloniki", "portal", "board", "Direct"]

# Δημιουργία συνδυασμών για .gr domains
candidates = set()
for p1, p2 in itertools.product(keywords_part1, keywords_part2):
    candidates.add(f"{p1.lower()}{p2.lower()}.gr")
    candidates.add(f"{p1.lower()}-{p2.lower()}.gr")

expired_domains = []

print(f"Ξεκινάει ο έλεγχος για {len(candidates)} υποψήφια domains...")

def is_domain_available(domain):
    """
    Ελέγχει αν το domain είναι διαθέσιμο (δηλαδή δεν έχει ενεργό DNS / A record).
    """
    try:
        socket.gethostbyname(domain)
        return False  # Υπάρχει ενεργό site/DNS, άρα ΔΕΝ είναι ελεύθερο
    except socket.gaierror:
        return True   # Δεν βρέθηκε DNS, άρα πιθανότατα είναι ελεύθερο/ληγμένο

# Έλεγχος διαθεσιμότητας για κάθε υποψήφιο domain
for domain in sorted(candidates):
    if is_domain_available(domain):
        expired_domains.append(domain)

# Αποθήκευση των διαθέσιμων/ληγμένων στο αρχείο
with open("expired_candidates.txt", "w", encoding="utf-8") as f:
    for domain in expired_domains:
        f.write(domain + "\n")

print(f"Ολοκληρώθηκε! Βρέθηκαν {len(expired_domains)} ελεύθερα/ληγμένα domains.")
