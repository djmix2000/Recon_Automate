import asyncio
from Gau import Gau, GauBatchParser
from Subfinder import Subfinder, SubfinderParser, SubfinderCheck


async def main():
    subfinder = Subfinder("kuper.ru")
    subfinder_parser = SubfinderParser(subfinder)
    subfinder_parser.subdomain_parse()
    subfinder_check = SubfinderCheck(subfinder)
    subdomain_list = await subfinder_check.check_subdomain()
    print(subdomain_list)
    gau = Gau(subdomain_list,"kuper.ru")
    batch_parser = GauBatchParser(gau)
    batch_parser.parse_all()
    print(repr(gau))



if __name__ == "__main__":
    asyncio.run(main())
