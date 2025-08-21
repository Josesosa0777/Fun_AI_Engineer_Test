import json

kpis = [
    {"label": "CPU Usage", "lift": 12.5},
    {"label": "Memory Usage", "lift": 8.3},
    {"label": "Network Latency", "lift": 15.2},
    {"label": "Disk I/O", "lift": 5.7}
]

# Sort KPIs by lift descending
top_kpis = sorted(kpis, key=lambda x: x['lift'], reverse=True)[:2]

# Imprimir los dos KPIs con mayor lift
for kpi in top_kpis:
    print(f"{kpi['label']}: {kpi['lift']}% lift")


# Expected output:
# Network Latency: 15.2% lift
# CPU Usage: 12.5% lift
