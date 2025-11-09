
{
  "log": { "level": "info" },

  "dns": {
    "servers": ["https://1.1.1.1/dns-query"],
    "strategy": "prefer_ipv4"
  },

  "inbounds": [
    {
      "type": "tun",
      "tag": "tun-in",
      "interface_name": "singbox",
      "inet4_address": ["172.19.0.1/30"],          // <— ВАЖНО: добавляет адрес IPv4
      "inet6_address": ["fdfe:dcba:9876::1/126"],  // можно оставить как есть или удалить
      "auto_route": true,
      "mtu": 1500,
      "stack": "mixed",
      "sniff": true
    }
  ],

  "outbounds": [
    {
      "type": "vless",
      "tag": "vless-out",
      "server": "94.103.1.74",           // например: example.com или 1.2.3.4
      "server_port": 443,
      "uuid": "69bd5ce1-0025-4269-b8e2-136ef28f734e",             // твой VLESS UUID
      "flow": "xtls-rprx-vision",                        // обычно пусто
      "tls": {
        "enabled": true,
        "server_name": "google.com",     // обычно тот же домен, что и server
        "insecure": false,

        "utls": { "enabled": true, "fingerprint": "chrome" },

        "reality": {
          "enabled": false,
          "public_key": "hFg_STFZBH88z08re4TojkUK3KqqBlki9pOVK7_PNHE",
          "short_id": "05d46102b94f703c"
        }
      },

      "transport": {
        "type": "tcp"                    // поменяй при необходимости:
                                         // "ws" -> добавь "path" и "headers"."Host"
                                         // "grpc" -> добавь "service_name"
      }
    },

    { "type": "direct", "tag": "direct" },
    { "type": "block",  "tag": "block"  }
  ],

  "route": {
    "final": "vless-out",
    "rules": []
  }
}
