import hashlib


def read_passwords(filename):
  passwords = []
  with open(filename, 'r') as file:
    for password in file:
      passwords.append(password.strip())
  return passwords


def read_salts(filename):
  salts = []
  with open(filename, 'r') as file:
    for salt in file:
      salts.append(salt.strip())
  return salts


def crack_sha1_hash(hash, use_salts=False):
  file_passwords = 'top-10000-passwords.txt'
  file_salts = 'known-salts.txt'

  passwords = read_passwords(file_passwords)

  if use_salts:
    salts = read_salts(file_salts)

    for salt in salts:
      for password in passwords:
        salted_password_prepend = password + salt
        hashed_password_prepend = hashlib.sha1(salted_password_prepend.encode()).hexdigest()
        
        salted_password_append = salt + password
        hashed_password_append = hashlib.sha1(salted_password_append.encode()).hexdigest()

        if hashed_password_prepend == hash or hashed_password_append == hash:
          return password

  else:
    for password in passwords:
      hashed_password = hashlib.sha1(password.encode()).hexdigest()

      if hashed_password == hash:
        return password

  return 'PASSWORD NOT IN DATABASE'
