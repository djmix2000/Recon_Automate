import subprocess


class Gau:
    def __init__(self, subdomain: list[str],domain:str):
        self.domain = domain
        self.subdomain_list: list[str] = subdomain
        self.gau_list: list[list[str]] = []
    def __repr__(self):
        return f"Gau(domain= {self.domain},subdomain_list = {self.subdomain_list},gau_list = {self.gau_list}"

class GauSingleParser:
    @staticmethod
    def parse(domain:str)->list[str]:
        gau_s = subprocess.run(['gau', f"{domain}"], capture_output=True, text=True)
        gau_list_temp = gau_s.stdout.split('\n')
        return gau_list_temp


class GauBatchParser:
    def __init__(self,gau:Gau):
        self.gau = gau

    def parse_all(self):
        for domain in self.gau.subdomain_list:
            self.gau.gau_list.append(GauSingleParser.parse(domain))
        self.gau.gau_list.append(GauSingleParser.parse(self.gau.domain))

