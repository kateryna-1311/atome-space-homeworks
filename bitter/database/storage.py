from typing import TypedDict


class User(TypedDict):
    name: str
    posts: list[int]
    followers: list[str]
    following: list[str]


class Post(TypedDict):
    id: int
    author: str
    content: str
    likes: list[str]
    comments: list[str]
    views: int


users: dict[str, User] = {
    "elonmusk": {
        "name": "Elon Musk",
        "posts": [1],
        "followers": ["zuck", "sama", "karpathy"],
        "following": ["naval", "geohot"],
    },
    "mrbeast": {
        "name": "MrBeast",
        "posts": [2],
        "followers": ["elonmusk", "billgates"],
        "following": ["zuck"],
    },
    "billgates": {
        "name": "Bill Gates",
        "posts": [3],
        "followers": ["guido"],
        "following": ["sama", "lexfridman"],
    },
    "zuck": {
        "name": "Mark Zuckerberg",
        "posts": [4],
        "followers": ["mrbeast"],
        "following": ["elonmusk", "sama"],
    },
    "naval": {
        "name": "Naval Ravikant",
        "posts": [5],
        "followers": ["elonmusk", "geohot"],
        "following": ["karpathy"],
    },
    "lexfridman": {
        "name": "Lex Fridman",
        "posts": [6],
        "followers": ["sama"],
        "following": ["elonmusk", "naval"],
    },
    "geohot": {
        "name": "George Hotz",
        "posts": [7],
        "followers": ["karpathy"],
        "following": ["naval"],
    },
    "sama": {
        "name": "Sam Altman",
        "posts": [8],
        "followers": ["billgates", "zuck"],
        "following": ["elonmusk", "lexfridman"],
    },
    "karpathy": {
        "name": "Andrej Karpathy",
        "posts": [9],
        "followers": ["naval"],
        "following": ["geohot", "sama"],
    },
    "guido": {
        "name": "Guido van Rossum",
        "posts": [10],
        "followers": ["billgates"],
        "following": ["karpathy"],
    },
}

posts: list[Post] = [
    {
        "id": 1,
        "author": "elonmusk",
        "content": "Mars is looking more achievable every year.",
        "likes": ["zuck", "sama", "karpathy", "naval", "mrbeast"],
        "comments": [],
        "views": 0,
    },
    {
        "id": 2,
        "author": "mrbeast",
        "content": "Just gave away 100 pizzas 🍕",
        "likes": ["elonmusk", "billgates", "zuck", "guido", "lexfridman", "sama"],
        "comments": [],
        "views": 0,
    },
    {
        "id": 3,
        "author": "billgates",
        "content": "AI will change education dramatically.",
        "likes": ["sama", "karpathy", "guido", "lexfridman"],
        "comments": [],
        "views": 0,
    },
    {
        "id": 4,
        "author": "zuck",
        "content": "The future is virtual reality.",
        "likes": ["elonmusk", "mrbeast", "sama"],
        "comments": [],
        "views": 0,
    },
    {
        "id": 5,
        "author": "naval",
        "content": "Learn to build. Learn to sell.",
        "likes": ["geohot", "karpathy", "lexfridman", "sama", "billgates", "guido"],
        "comments": [],
        "views": 0,
    },
    {
        "id": 6,
        "author": "lexfridman",
        "content": "Long conversations are underrated.",
        "likes": ["sama", "elonmusk", "naval", "karpathy"],
        "comments": [],
        "views": 0,
    },
    {
        "id": 7,
        "author": "geohot",
        "content": "Code should be simple.",
        "likes": ["karpathy", "naval", "guido", "sama", "elonmusk"],
        "comments": [],
        "views": 0,
    },
    {
        "id": 8,
        "author": "sama",
        "content": "The intelligence age has begun.",
        "likes": [
            "elonmusk",
            "billgates",
            "karpathy",
            "lexfridman",
            "naval",
            "mrbeast",
            "zuck",
            "guido",
        ],
        "comments": [],
        "views": 0,
    },
    {
        "id": 9,
        "author": "karpathy",
        "content": "Neural networks are just math and GPUs.",
        "likes": ["sama", "geohot", "naval", "lexfridman", "billgates"],
        "comments": [],
        "views": 0,
    },
    {
        "id": 10,
        "author": "guido",
        "content": "Readability counts.",
        "likes": [
            "elonmusk",
            "sama",
            "karpathy",
            "billgates",
            "lexfridman",
            "zuck",
            "mrbeast",
            "naval",
            "geohot",
        ],
        "comments": [],
        "views": 0,
    },
]
