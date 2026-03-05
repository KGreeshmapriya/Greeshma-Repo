import requests

API_KEY = "61c80879a1944704916d0e113a5dee73"

def get_news():

    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"
    try:
        r = requests.get(url).json()

        articles = r.get("articles", [])

        if len(articles) == 0:
            return sample_news()

        return articles[:6]

    except:
        return sample_news()


def sample_news():
    return [
        {
            "title": "AI is Transforming the Tech Industry",
            "description": "Artificial Intelligence continues to reshape industries worldwide.",
            "urlToImage": "https://picsum.photos/400/200?1"
        },
        {
            "title": "Python Remains the Most Popular Programming Language",
            "description": "Developers across the globe continue to prefer Python for data science and AI.",
            "urlToImage": "https://picsum.photos/400/200?2"
        },
        {
            "title": "Startups Focus on Automation Tools",
            "description": "Automation platforms are gaining popularity among new startups.",
            "urlToImage": "https://picsum.photos/400/200?3"
        },
        {
            "title": "Space Exploration Advances in 2026",
            "description": "Private space companies are accelerating missions to the Moon and Mars.",
            "urlToImage": "https://picsum.photos/400/200?4"
        },
        {
            "title": "Cybersecurity Becomes a Global Priority",
            "description": "Governments and companies increase investments in cybersecurity.",
            "urlToImage": "https://picsum.photos/400/200?5"
        }
    ]