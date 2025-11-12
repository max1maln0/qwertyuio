{
  "log": {
    "level": "info",
    "timestamp": true
  },

  "dns": {
    "strategy": "ipv4_only",
    "servers": [
      {
        "tag": "cf-doh",
        "type": "https",
        "server": "cloudflare-dns.com/dns-query",
        "detour": "vless-out"
      },
      {
        "tag": "gg-doh",
        "type": "https",
        "server": "dns.google/dns-query",
        "detour": "vless-out"
      }
    ]
  },

  "inbounds": [
    {
      "type": "tun",
      "tag": "tun-in",
      "stack": "gvisor",
      "auto_route": true,
      "strict_route": false,
      "mtu": 1380,
      "address": [
        "172.19.0.1/30",
        "fdfe:dcba:9876::1/126"
      ],
      "route_address": [
        "172.19.0.0/30",
        "fdfe:dcba:9876::/126"
      ],
      "route_exclude_address": [
        "10.0.0.0/8",
        "172.16.0.0/12",
        "192.168.0.0/16",
        "fd00::/8"
      ]
    }
  ],

  "outbounds": [
    {
      "type": "vless",
      "tag": "vless-out",
      "server": "94.103.1.74",
      "server_port": 443,
      "uuid": "69bd5ce1-0025-4269-b8e2-136ef28f734e",
      "flow": "xtls-rprx-vision",
      "domain_resolver": "cf-doh",
      "tls": {
        "enabled": true,
        "server_name": "google.com",
        "utls": { "enabled": true, "fingerprint": "firefox" },
        "reality": {
          "enabled": true,
          "public_key": "hFg_STFZBH88z08re4TojkUK3KqqBlki9pOVK7_PNHE",
          "short_id": "05d46102b94f703c"
        }
      }
    },
    { "type": "dns", "tag": "dns-out" },
    { "type": "direct", "tag": "direct" },
    { "type": "block", "tag": "block" }
  ],

  "route": {
    "auto_detect_interface": true,
    "final": "vless-out",
    "default_domain_resolver": { "server": "cf-doh" },
    "rules": [
      { "protocol": "dns", "outbound": "dns-out" },
      { "port": 53, "network": "udp", "outbound": "dns-out" },
      { "geoip": "private", "outbound": "direct" },
      { "ip_cidr": ["224.0.0.0/3"], "outbound": "direct" }
    ]
  }
}
