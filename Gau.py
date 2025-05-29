import subprocess


class Gau:
    def __init__(self, subdomain: list[str],domain:str):
        self.domain = domain
        self.subdomain_list: list[str] = subdomain
        self.gau_list: list[list[str]] = []

    def gau_parse_single(self,domain:str):
        gau = subprocess.run(['gau', f"{domain}"], capture_output=True, text=True)
        gau_list_temp = gau.stdout.split('\n')
        self.gau_list.append(gau_list_temp)

    def gau_parse_all(self):
        for domain in self.subdomain_list:
            self.gau_parse_single(domain)
        self.gau_parse_single(self.domain)
