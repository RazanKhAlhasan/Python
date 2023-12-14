{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b8b1d8fc-a4b0-477f-a36e-9a394c4e6266",
   "metadata": {
    "tags": []
   },
   "source": [
    "# Project: Rank Tweets by Kindness\n",
    "\n",
    "**Sentiment Analysis**: Social media can be a great place to connect with others and share positive thoughts and experiences. However, it can also be a breeding ground for negativity and hate speech. This project aims to develop a system to rank tweets by kindness in order to promote more positive and supportive online interactions.\n",
    "\n",
    "**Benefits:**\n",
    "\n",
    "The proposed system has the potential to provide a number of benefits, including:\n",
    "\n",
    "- Promoting more positive and supportive online interactions\n",
    "- Reducing the spread of negativity and hate speech\n",
    "- Helping people to find and connect with others who share their values\n",
    "- Making social media a more enjoyable and welcoming place for everyone\n",
    "\n",
    "**Tasks:**\n",
    "\n",
    "The proposed system will use sentiment analysis to identify and rank tweets based on their level of kindness. This will be done by the following steps:\n",
    "\n",
    "1. Read the `nice_words.txt` file into a list. This file will contain a list of words that are typically associated with kindness, such as \"love,\" \"compassion,\" and \"gratitude.\"\n",
    "1. Read the `tweets.txt` file into a tweets list. This file will contain a collection of tweets to be ranked.\n",
    "1. Look at each of the tweets and count the number of nice words.\n",
    "1. Sort the tweets in descending order based on the number of nice words, with the most kind tweet first.\n",
    "1. Display the tweets, along with the count of nice words in each tweet.\n",
    "\n",
    "```\n",
    "sample tweets:\n",
    "[\n",
    "    \"great and awesome\",\n",
    "    \"what a good day\"\n",
    "]\n",
    "sample output:\n",
    "[\n",
    "    (\"great and awesome\", 2),\n",
    "    (\"what a good day\", 1),\n",
    "]\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "12126c81",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "( The kind and generous old man was always willing to help others , 2 )\n",
      "( The intelligent and talented young woman had a bright future ahead of her , 2 )\n",
      "( Sending out good vibes to everyone today! Have a beautiful day! , 2 )\n",
      "( Grateful for the amazing people in my life who make it so wonderful , 1 )\n",
      "( The beautiful flowers were in full bloom and the sweet scent filled the air , 1 )\n",
      "( It was a perfect day , 1 )\n",
      "( The birds were singing merrily and the sun was shining brightly , 0 )\n",
      "( He was a role model for the entire community and he was loved by everyone , 0 )\n",
      "( She was passionate about her work and she was determined to make a difference in the world , 0 )\n",
      "( Hate , 0 )\n",
      "( how are you? , 0 )\n"
     ]
    }
   ],
   "source": [
    "def checkWords(tweet, words):\n",
    "    dictionary = {}\n",
    "    with open(tweet, 'r') as f:\n",
    "        with open(words,'r') as w:\n",
    "            w = w.read()\n",
    "            for line in f:\n",
    "                dictionary.update({line: 0})\n",
    "                for word in line.split():\n",
    "                    if word in w.split():\n",
    "                            dictionary[line] += 1\n",
    "    \n",
    "            sortedElements = sorted(dictionary.items(), key = lambda x: x[1], reverse = True)\n",
    "            for key, value in sortedElements:\n",
    "                print(\"(\", key.strip(), ',' ,value ,\")\", end = \"\\n\")\n",
    "\n",
    "                \n",
    "  \n",
    "    \n",
    "    \n",
    "    \n",
    "checkWords(r'C:\\Users\\Razan\\Downloads\\tweets.txt', r'C:\\Users\\Razan\\Downloads\\nice_words.txt')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b40de9ad-9cfa-488d-9f8e-ade52b12eb2b",
   "metadata": {},
   "source": [
    "***Adding textblob library to the code to determine if the tweet is positive, negative, or neutral:***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "29884dca",
   "metadata": {},
   "outputs": [],
   "source": [
    "pip install textblob"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "311bca09",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "( The kind and generous old man was always willing to help others , 2 , Positive )\n",
      "( The intelligent and talented young woman had a bright future ahead of her , 2 , Positive )\n",
      "( Sending out good vibes to everyone today! Have a beautiful day! , 2 , Positive )\n",
      "( Grateful for the amazing people in my life who make it so wonderful , 1 , Positive )\n",
      "( The beautiful flowers were in full bloom and the sweet scent filled the air , 1 , Positive )\n",
      "( It was a perfect day , 1 , Positive )\n",
      "( The birds were singing merrily and the sun was shining brightly , 0 , Positive )\n",
      "( He was a role model for the entire community and he was loved by everyone , 0 , Positive )\n",
      "( She was passionate about her work and she was determined to make a difference in the world , 0 , Negative )\n",
      "( Hate , 0 , Negative )\n",
      "( how are you? , 0 , Neutral )\n"
     ]
    }
   ],
   "source": [
    "from textblob import TextBlob\n",
    "def checkWords(tweet, words):\n",
    "    dictionary = {}\n",
    "    with open(tweet, 'r') as f:\n",
    "        with open(words,'r') as w:\n",
    "            w = w.read()\n",
    "            for line in f:\n",
    "                dictionary.update({line: 0})\n",
    "                for word in line.split():\n",
    "                    if word in w.split():\n",
    "                            dictionary[line] += 1\n",
    "                sentiment = TextBlob(line).sentiment.polarity\n",
    "\n",
    "            sortedElements = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)\n",
    "            for key, value in sortedElements:\n",
    "                sentiment = TextBlob(key).sentiment.polarity\n",
    "                if sentiment > 0:\n",
    "                    sentiment_label = \"Positive\"\n",
    "                elif sentiment < 0:\n",
    "                    sentiment_label = \"Negative\"\n",
    "                else:\n",
    "                    sentiment_label = \"Neutral\"\n",
    "                    \n",
    "                #print(\"Sentiment:\", sentiment_label, \"| Tweet:\", key.strip(), \"| Count:\", value)\n",
    "                print(\"(\", key.strip(), ',' ,value , ',' , sentiment_label, \")\", end = \"\\n\")\n",
    "\n",
    "\n",
    "checkWords(r'C:\\Users\\Razan\\Downloads\\tweets.txt', r'C:\\Users\\Razan\\Downloads\\nice_words.txt')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5f23c0d1-e3b0-4040-ad91-1f4831ab7577",
   "metadata": {},
   "source": [
    "***Using API to extract the tweet***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "7ae3e3f3-3848-4dd5-9f25-3f09f346fdf0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'__typename': 'Tweet', 'lang': 'en', 'favorite_count': 392545, 'created_at': '2022-01-25T12:30:40.000Z', 'display_text_range': [0, 60], 'entities': {'hashtags': [], 'urls': [], 'user_mentions': [{'id_str': '71026122', 'indices': [33, 43], 'name': \"McDonald's\", 'screen_name': 'McDonalds'}], 'symbols': []}, 'id_str': '1485953263040188416', 'text': 'I will eat a happy meal on tv if @McDonalds accepts Dogecoin', 'user': {'id_str': '44196397', 'name': 'Elon Musk', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1683325380441128960/yRsRRjGO_normal.jpg', 'screen_name': 'elonmusk', 'verified': False, 'highlighted_label': {'description': 'X', 'badge': {'url': 'https://pbs.twimg.com/profile_images/1683899100922511378/5lY42eHs_bigger.jpg'}, 'url': {'url': 'https://twitter.com/X', 'url_type': 'DeepLink'}, 'user_label_type': 'BusinessLabel', 'user_label_display_type': 'Badge'}, 'is_blue_verified': True}, 'edit_control': {'edit_tweet_ids': ['1485953263040188416'], 'editable_until_msecs': '1643115640242', 'is_edit_eligible': True, 'edits_remaining': '5'}, 'conversation_count': 28848, 'news_action_type': 'conversation', 'isEdited': False, 'isStaleEdit': False}\n",
      "\n",
      " Tweet: I will eat a happy meal on tv if @McDonalds accepts Dogecoin\n",
      "\n",
      " Result: Positive ( score 0.8 )\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "url = \"https://twitter135.p.rapidapi.com/v2/Tweet/\"\n",
    "\n",
    "querystring = {\"id\":\"1485953263040188416\"}\n",
    "\n",
    "headers = {\n",
    "\t\"X-RapidAPI-Key\": \"631bfc0f22msh6af0ac5ec164ac9p141c20jsne2053689f265\",\n",
    "\t\"X-RapidAPI-Host\": \"twitter135.p.rapidapi.com\"\n",
    "}\n",
    "\n",
    "response = requests.get(url, headers=headers, params=querystring)\n",
    "\n",
    "response_json = response.json()\n",
    "print(response_json)\n",
    "\n",
    "tweet_text = response_json['text']\n",
    "blob = TextBlob(str(tweet_text))\n",
    "score = blob.polarity\n",
    "\n",
    "if score > 0:\n",
    "    result = \"Positive\"\n",
    "elif score<0:\n",
    "    result = \"Negative\"\n",
    "else: \n",
    "    result=\"Neutral\"\n",
    "\n",
    "print('\\n Tweet:', tweet_text)\n",
    "print(\"\\n Result:\", result,'(','score',score,')')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
