import asyncio
import aiohttp
import sys


async def check_subdomain(session, target, subdomain):
    url = f"https://{subdomain}.{target}"

    try:
        async with session.get(
            url,
            timeout=aiohttp.ClientTimeout(total=5),
            ssl=False
        ) as response:
            print(f"[+] {url} -> {response.status}")

    except (aiohttp.ClientError, asyncio.TimeoutError):
        pass


async def enumerate_subdomains(target, wordlist):
    connector = aiohttp.TCPConnector(limit=50)

    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []

        for subdomain in wordlist:
            subdomain = subdomain.strip()

            if subdomain:
                tasks.append(
                    check_subdomain(session, target, subdomain)
                )

        await asyncio.gather(*tasks)


def main():
    if len(sys.argv) != 3:
        print("Usage: python subdomain_enum.py <domain> <wordlist>")
        sys.exit(1)

    target = sys.argv[1]

    with open(sys.argv[2], "r") as file:
        wordlist = file.readlines()

    asyncio.run(enumerate_subdomains(target, wordlist))


if __name__ == "__main__":
    main()
