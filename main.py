import asyncio
from Gau import Gau, GauBatchParser
from Subfinder import Subfinder


async def main():
    subfinder = Subfinder("kuper.ru")
    subfinder.subdomain_parse()
    subdomain_list = await subfinder.check_subdomain()
    print(subdomain_list)
    gau = Gau(subdomain_list,"kuper.ru")
    batch_parser = GauBatchParser(gau)
    batch_parser.parse_all()
    print(repr(gau))



if __name__ == "__main__":
    asyncio.run(main())
