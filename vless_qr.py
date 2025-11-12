{
  "log": {
    "level": "info",
    "timestamp": true
  },

  "dns": {
    "servers": [
      {
        "type": "https",
        "server": "cloudflare-dns.com",
        "tag": "doh"
      },
      {
        "type": "local",
        "tag": "localdns"
      }
    ],
    "strategy": "prefer_ipv4"
  },

  "inbounds": [
    {
      "type": "tun",
      "tag": "tun-in",
      "address": ["172.19.0.1/30", "fdfe:dcba:9876::1/126"],
      "route_address": ["172.19.0.0/30", "fdfe:dcba:9876::/126"],
      "route_exclude_address": ["192.168.0.0/16", "10.0.0.0/8", "172.16.0.0/12", "fd00::/8"],
      "auto_route": true,
      "stack": "system",
      "mtu": 1280
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
      "tls": {
        "enabled": true,
        "server_name": "google.com",
        "alpn": ["h2", "http/1.1"],
        "utls": {
          "enabled": true,
          "fingerprint": "firefox"
        },
        "reality": {
          "enabled": true,
          "public_key": "hFg_STFZBH88z08re4TojkUK3KqqBlki9pOVK7_PNHE",
          "short_id": "05d46102b94f703c"
        }
      },
      "domain_resolver": "doh"
    },
    { "type": "direct", "tag": "direct" },
    { "type": "block",  "tag": "block" }
  ],

  "route": {
    "final": "vless-out",
    "default_domain_resolver": { "server": "doh" },
    "rules": [
      { "ip": ["SERVER_IP_CIDR"], "outbound": "direct" },
      { "geoip": ["private"], "outbound": "direct" }
    ]
  }
}
