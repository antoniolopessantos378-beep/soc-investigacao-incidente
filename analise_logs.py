with open("logs.txt", "r") as file:
    logs = file.readlines()

failed = 0
ips = []

for log in logs:
    if "FAILED" in log:
        failed += 1
    if "ip:" in log:
        ip = log.split("ip: ")[1].strip()
        ips.append(ip)

print(f"Tentativas falhas: {failed}")
print(f"IPs encontrados: {set(ips)}")

if failed >= 2:
    print("ALERTA: Possível ataque de força bruta!")
