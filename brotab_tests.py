from brotab.main import create_clients

if __name__ == "__main__":
    client = create_clients()[0]
    for tab in client.list_tabs(""):
        print(tab)
    client.open_urls(["https://ct.de"])
