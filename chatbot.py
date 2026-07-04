from google import genai

API_KEY = "YOUR_REAL_API_KEY"

client = genai.Client(api_key=API_KEY)


def ask_wellness_bot(question):

    prompt = f"""
    You are an AI Digital Wellness Assistant.

    Give short, practical and friendly advice about:
    - screen time
    - digital detox
    - productivity
    - focus
    - mental wellness
    - healthy technology habits

    Keep answers under 150 words.

    User Question:
    {question}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text