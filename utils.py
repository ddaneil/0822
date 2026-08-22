def rupiah(amount):
    # from 15000 to Rp15.000
    return f"Rp {amount:,.0f}".replace(",", ".")