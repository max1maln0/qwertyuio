{
  "log": {
    "level": "info"
  },

  "inbounds": [
    {
      "type": "tun",
      "tag": "tun-in",

      "address": ["172.19.0.1/30", "fdfe:dcba:9876::1/126"],
      "route_address": ["172.19.0.0/30", "fdfe:dcba:9876::/126"],
      "route_exclude_address": ["10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16", "fd00::/8"],

      "auto_route": true,
      "stack": "gvisor",
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
        "utls": {
          "enabled": true,
          "fingerprint": "firefox"
        },
        "reality": {
          "enabled": true,
          "public_key": "hFg_STFZBH88z08re4TojkUK3KqqBlki9pOVK7_PNHE",
          "short_id": "05d46102b94f703c"
        }
      }
    },

    { "type": "direct", "tag": "direct" },
    { "type": "block",  "tag": "block" }
  ],

  "route": {
    "final": "vless-out",
    "auto_detect_interface": true
  },

  "dns": {
    "servers": [
      { "tag": "dns-local", "type": "local" }
    ],
    "strategy": "prefer_ipv4"
  }
}
