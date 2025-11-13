{
  "log": {
    "level": "info"
  },

  "dns": {
    "servers": [
      {
        "tag": "remote",
        "address": "https://1.1.1.1/dns-query"
      },
      {
        "tag": "local",
        "address": "local"
      }
    ]
  },

  "inbounds": [
    {
      "type": "tun",
      "tag": "tun-in",
      "address": [
        "172.19.0.1/30",
        "fdfe:dcba:9876::1/126"
      ],
      "route_address": [
        "172.19.0.0/30",
        "fdfe:dcba:9876::/126"
      ],
      "route_exclude_address": [
        "192.168.0.0/16",
        "10.0.0.0/8",
        "172.16.0.0/12",
        "fd00::/8"
      ],
      "auto_route": true,
      "strict_route": false,
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
      "network": "tcp",
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
    {
      "type": "direct",
      "tag": "direct"
    },
    {
      "type": "block",
      "tag": "block"
    }
  ],

  "route": {
    "auto_detect_interface": true,
    "rules": [
      {
        "inbound": [
          "tun-in"
        ],
        "ip_cidr": [
          "10.0.0.0/8",
          "172.16.0.0/12",
          "192.168.0.0/16",
          "127.0.0.0/8",
          "::1/128",
          "fc00::/7"
        ],
        "outbound": "direct"
      },
      {
        "inbound": [
          "tun-in"
        ],
        "port": 53,
        "network": "udp",
        "outbound": "direct"
      }
    ]
  }
}
