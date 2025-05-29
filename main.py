import asyncio
from Gau import Gau
from Subfinder import Subfinder


async def main():
    subfinder = Subfinder("kuper.ru")
    subfinder.subdomain_parse()
    subdomain_list = await subfinder.check_subdomain()
    print(subdomain_list)
    gau = Gau(subdomain_list,"kuper.ru")
    gau_list = gau.gau_parse_all()
    print(gau_list)



if __name__ == "__main__":
    asyncio.run(main())
