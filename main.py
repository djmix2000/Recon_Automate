import asyncio
import subprocess
import aiohttp


async def check_single_domain(subdomain:str)->str:
    async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f'https://{subdomain}', ssl=False) as response:
                    if response.status == 200:
                        return subdomain
            except Exception as e:
                print(f"[!] Error for {subdomain}: {e}")



class Recon:
    def __init__(self,domain:str):
        self.subdomain_list: list[str] = []
        self.domain = domain
        self.gau_list: list[list[str]]=[]

    async def check_subdomain(self):
        tasks = [check_single_domain(subdomain) for subdomain in self.subdomain_list]
        results = await asyncio.gather(*tasks)
        self.subdomain_list = [result for result in results if result is not None]


    async def subdomain_parse(self):
        subfinder = subprocess.run(["subfinder", "-d", f"{self.domain}"], capture_output=True, text=True)
        self.subdomain_list = subfinder.stdout.split('\n')
        await self.check_subdomain()

    def gau_parse_single(self,domain:str):
        gau = subprocess.run(['gau', f"{domain}"], capture_output=True, text=True)
        gau_list_temp = gau.stdout.split('\n')
        self.gau_list.append(gau_list_temp)

    def gau_parse_all(self):
        for domain in self.subdomain_list:
            self.gau_parse_single(domain)
        self.gau_parse_single(self.domain)


    def get_gau_list(self) -> list[list[str]]:
        return self.gau_list

    def get_subdomain(self) -> list[str]:
        return self.subdomain_list







async def main():
    kuper = Recon("kuper.ru")
    await kuper.subdomain_parse()
    kuper.gau_parse_all()
    print(kuper.gau_list)




if __name__ == "__main__":
    asyncio.run(main())
