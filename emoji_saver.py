import requests

links = []

with open("emoji_links.txt", "r") as file:
    links = file.read().splitlines()

for link in links:
    response = requests.get(link)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the filename from the URL
        filename = link.split("/")[-1]

        # Save the image
        with open(f"emojis/{filename}", "wb") as file:
            file.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {link}")
