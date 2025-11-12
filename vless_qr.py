{
  "log": { "level": "info" },

  "dns": {
    "servers": [
      { "address": "1.1.1.1" },
      { "address": "8.8.8.8" }
    ],
    "strategy": "prefer_ipv4"
  },

  "inbounds": [
    {
      "type": "tun",
      "tag": "tun-in",
      "inet4_address": "172.19.0.1/30",
      "inet6_address": "fdfe:dcba:9876::1/126",
      "mtu": 1500,
      "auto_route": true,
      "strict_route": false,
      "stack": "system"
    }
  ],

  "outbounds": [
    {
      "type": "vless",
      "tag": "vless-out",

      "server": "94.103.1.74",          // например: example.com
      "server_port": 443,

      "uuid": "69bd5ce1-0025-4269-b8e2-136ef28f734e",              // ТВОЙ VLESS-ключ (UUID)
      "flow": "xtls-rprx-vision",                         // оставь пустым, если не используешь xtls-rprx-vision

      "packet_encoding": "xudp",          // можно удалить, если не нужно

      "tls": {
        "enabled": true,
        "server_name": "google.com", // обычно тот же домен, что и в Host заголовке
        "insecure": false,
        "utls": { "enabled": true, "fingerprint": "chrome" },

        "reality": {
          "enabled": false,
          "public_key": "hFg_STFZBH88z08re4TojkUK3KqqBlki9pOVK7_PNHE",
          "short_id": "05d46102b94f703c"
        }
      },

      "transport": {
        "type": "ws",
        "path": "/",
        "headers": { "Host": "google.com" }
      }
    },

    { "type": "direct", "tag": "direct" },
    { "type": "block",  "tag": "block" }
  ],

  "route": {
    "auto_detect_interface": true,
    "final": "vless-out"
  }
}
