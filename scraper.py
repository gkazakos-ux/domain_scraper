import socket
import sys

def load_targets():
    """Διαβάζει τα υποψήφια domains προς έλεγχο από το αρχείο targets.txt"""
    try:
        with open("targets.txt", "r", encoding="utf-8") as f:
            return [line.strip().lower() for line in f if line.strip() and line.strip().endswith(".gr")]
    except FileNotFoundError:
        print("Το αρχείο targets.txt δεν βρέθηκε.")
        return []

def check_gr_domain(domain):
    """
    Ελέγχει τη διαθεσιμότητα ενός .gr domain μέσω DNS/Socket.
    Αν δεν υπάρχει ενεργό DNS, θεωρείται υποψήφιο ληγμένο/ελεύθερο.
    """
    try:
        socket.gethostbyname(domain)
        return False  # Υπάρχει ενεργό DNS, άρα είναι κατειλημμένο
    except socket.gaierror:
        return True   # Δεν βρέθηκε DNS, άρα είναι πιθανώς ελεύθερο

def main():
    targets = load_targets()
    if not targets:
        print("Δεν υπάρχουν domains προς έλεγχο.")
        return

    expired_candidates = []
    print(f"Ξεκινάει ο έλεγχος για {len(targets)} .gr domains...")

    for domain in targets:
        if check_gr_domain(domain):
            expired_candidates.append(domain)

    # Αποθήκευση των διαθέσιμων στοexpired_candidates.txt
    with open("expired_candidates.txt", "w", encoding="utf-8") as f:
        for domain in expired_candidates:
            f.write(domain + "\n")

    print(f"Ολοκληρώθηκε. Εντοπίστηκαν {len(expired_candidates)} διαθέσιμα .gr domains.")

if __name__ == "__main__":
    main()
