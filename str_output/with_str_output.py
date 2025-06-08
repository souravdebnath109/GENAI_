from langchain_google_genai import GoogleGenerativeAI
from typing import TypedDict
import json

# Define structured output schema
class Review(TypedDict):
    summary: str
    sentiment: str

# Initialize the model
model = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key="gemini_api_key"
)

# Your review text
review_text = """

Have you ever really lived until you’ve seen Tom Cruise dangling off an exploded bridge, or using a vertiginous mountainside as an Evel Kneivel-style motorbike ramp?

Audiences have long been awaiting Mission Impossible: Dead Reckoning – Part One, which for four years has suffered production delays, interrupted repeatedly by the initial outbreak of the Covid-19 pandemic and its various resurgences. With such a long and convoluted road to audiences, expectations have grown high: what would Tom Cruise’s death-defying stunt work and the nous of Christopher McQuarrie, director of two prior well-loved iterations of the franchise, have in store for us?

For the most part: all the excitement we would expect. Sure, a confusing plot hole sometimes appears, but Cruise, one of our greatest living movie stars, just jumps through it, usually from a great height. We’re too busy being absorbed into the exotic locations, or the iconically life-like face masks, or a knife-fight on top of a speeding train.

Read Next
Must-see summer blockbusters for 2023, from The Little Mermaid to Mission Impossible and Barbie
square
FILM
Must-see summer blockbusters for 2023, from The Little Mermaid to Mission Impossible and Barbie
Read More
This time around, Ethan Hunt is faced with the mysterious and all-consuming power known as The Entity, a sentient AI that has the ability to infiltrate and manipulate information in every major world government, banking system, internet or satellite-based tech: whoever controls it effectively controls the entire planet.

Hunt and his team (the reliably great Ving Rhames and Simon Pegg on comms throughout) are faced with chasing down two interlocking parts of a key to The Entity’s source code – and racing against some villainous types who have aligned themselves with The Entity’s power, including Gabriel (Esti Morales, convincingly slick and amoral), a vicious foe with little regard for human life.

Meanwhile, in some of the film’s most crackling non-action moments, the film introduces Grace (Hayley Atwell, a charismatic presence who brightens every scene she’s in), a slippery international thief whose slick operations in art and jewellery heists have given her some poise under pressure – which she will need.

The film does make some amusing jabs at the algorithmic and the automated in the form of its evil AI enemy (also, as it goes, the real-life enemy of Cruise’s beloved old-school filmmaking and practical effects). But Mission Impossible is best when it is dispensing with narrative excuses to get to the action, which it does with an almost nod-and-wink level of self-awareness.

In that respect, the movie is a marvel of physical jeopardy and Hollywood setpieces par excellence: every car crashing crunch of metal, every walloping thud of a body falling. You get the sense these people really are being banged around; that they are made of flesh and blood rather than superhero rubber and magic.

Whether screeching through Roman traffic in a yellow Fiat 500 or trying to stop a runaway train from veering disastrously off its tracks, McQuarrie’s Mission Impossible is at its most thrilling when it’s all full-throttle, or in simple and powerful close-up of Tom Cruise, himself a kind of feat of Hollywood engineering at its finest. Much like 007, these are the kinds of movies where the sparkle covers over any silliness.

"""

# Prompt that strictly asks for JSON
prompt = f"""
Analyze the following review text and return a JSON object with two fields:

- "summary": A short summary of the review
- "sentiment": One of the values - "positive", "negative", or "neutral"

ONLY return a valid JSON object. Do not include any extra explanation or text.

Review text:
\"\"\"
{review_text}
\"\"\"
"""

# Invoke model
response = model.invoke(prompt)

# Try parsing the output as JSON
try:
    result: Review = json.loads(response)
    print("Summary:", result["summary"])
    print("Sentiment:", result["sentiment"])
except json.JSONDecodeError:
    print("Failed to parse response as JSON.")
    print("Raw response:", response)
