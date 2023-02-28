#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import CloudFlare
from typing import List, Dict


def main():
    email: str = ""  # your Cloudflare email account
    key: str = ""  # your Cloudflare api key
    domain: str = ""  # domain, waiting to clear, like yourdomain.com.
    cf = CloudFlare.CloudFlare(email=email, key=key)
    zones: List[Dict] = []
    try:
        zones = cf.zones.get(params={"name": domain})
        if len(zones) == 0:
            exit('/zones.get %s - %s' % (domain, "not found"))
    except Exception as e:
        exit('/zones.get %s - %s' % (domain, e))
    zone_id: str = zones[0]["id"]  # 因为只会有1个结果
    print(f"[{domain}][{zone_id}]")
    while True:
        records: List[Dict] = cf.zones.dns_records.get(zone_id)
        if len(records) == 0:
            print("Not！")
            break
        for _record in records:
            record_id: str = _record["id"]
            cf.zones.dns_records.delete(zone_id, record_id)
            print("删除[{}][{}][{}]成功".format(_record["type"], _record["name"], record_id))
    print("打完收工")


if __name__ == '__main__':
    main()
