import dns.resolver

def query_dns(domain):
    try:
        # A record (IPv4)
        print("\nA record (IPv4):")
        answers = dns.resolver.resolve(domain, 'A')
        for rdata in answers:
            print(rdata)

        # MX record (Mail servers)
        print("\nMX record (Mail Servers):")
        answers = dns.resolver.resolve(domain, 'MX')
        for rdata in answers:
            print(f"{rdata.exchange} (priority {rdata.preference})")

        # NS record (Name servers)
        print("\nNS record (Name Servers):")
        answers = dns.resolver.resolve(domain, 'NS')
        for rdata in answers:
            print(rdata)

    except Exception as e:
        print("Error:", e)

# Take domain input from user
domain = input("Enter domain: ")
query_dns(domain)