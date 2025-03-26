import hashlib

def password_cracker(hash, use_salts=False):
    # Read the top 10,000 passwords
    with open("top-10000-passwords.txt", "r") as file:
        passwords = [line.strip() for line in file.readlines()]

    salts = []
    
    # Read salts if use_salts is True
    if use_salts:
        with open("known-salts.txt", "r") as file:
            salts = [line.strip() for line in file.readlines()]
    
    # Check passwords without salts
    if not use_salts:
        for password in passwords:
            hashed_password = hashlib.sha1(password.encode()).hexdigest()
            if hashed_password == hash:
                return password
    else:
        # Check passwords with salts (both prepend and append)
        for password in passwords:
            for salt in salts:
                if hashlib.sha1((salt + password).encode()).hexdigest() == hash:
                    return password
                if hashlib.sha1((password + salt).encode()).hexdigest() == hash:
                    return password

    return "PASSWORD NOT IN DATABASE"
