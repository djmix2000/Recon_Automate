import asyncio
import aiohttp
import subprocess


class Subfinder:
    def __init__(self, domain: str):
        self.subdomain_list: list[str] = []
        self.domain = domain
    def __repr__(self):
        return f"Subfinder(domain = {self.domain},subdomain_list={self.subdomain_list}"


class SubfinderCheck:
    def __init__(self,subfinder):
        self.subfinder = subfinder
    @staticmethod
    async def check_single_domain(subdomain: str) -> str:
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f'https://{subdomain}', ssl=False) as response:
                    if response.status == 200:
                        return subdomain
            except Exception as e:
                print(f"[!] Error for {subdomain}: {e}")

    async def check_subdomain(self):
        tasks  = []
        for subdomain in self.subfinder.subdomain_list:
            tasks.append(self.check_single_domain(subdomain))
        results = await asyncio.gather(*tasks)
        self.subfinder.subdomain_list = [result for result in results if result is not None]
        return self.subfinder.subdomain_list


class SubfinderParser:
    def __init__(self, subfinder):
        self.subfinder = subfinder

    def subdomain_parse(self):
        subfinder = subprocess.run(["subfinder", "-d", f"{self.subfinder.domain}"], capture_output=True, text=True)
        self.subfinder.subdomain_list = subfinder.stdout.split('\n')