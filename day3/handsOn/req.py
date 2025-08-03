import requests

def fetch_data(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos/2"
    data = fetch_data(url)
    print("Fetched data:", data)
