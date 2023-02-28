# clear Dynadot to Cloudflare
[简体中文](README-zh.md) | [English](README.md)

When you purchase a new domain from Dynadot and point nameservers to Cloudflare, it may scanned for a lot of invalid domains.

However, Cloudflare does not support batch deletion, just only be using the API. :(

## Warning

Please do use it for the existing domain, this domain will be cleared.

## How to use
Install dependencies
```shell
pip install cloudflare
```

Edit`main.py`

Modify `email`，`key` and `domain` to your Cloudflare account.

Run it!
```shell
python main.py
```

## Bugs
If too many invalid domains, script maybe crashed. 

**Don't worry, just run it again**