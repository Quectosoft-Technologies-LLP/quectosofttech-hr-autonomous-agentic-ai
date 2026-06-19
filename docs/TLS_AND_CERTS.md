# TLS and Certificates

Ingress terminates TLS and certificates are rotated by cert-manager using a cluster issuer.
Production endpoints must enforce HTTPS and HSTS at the ingress layer.
