thoung_url = "https://chanthoung.com"
only_domain = thoung_url.removeprefix("https://") # removeprefix() removes text from the beginning of a string.
print(f"Original URL: {thoung_url}")
print(f"Clean URL: {only_domain}")