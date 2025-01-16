import random
import requests

API_TOKEN = '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'     # Use Hugging Face API token to authenticate API requests
API_URL = "https://api-inference.huggingface.co/models/gpt2"   # API URL for Hugging Face

headers = {
    "Authorization": f"Bearer {API_TOKEN}"  # Authorize the API token for API requests.
}

def generate_app_ideas():
    
    payload = {
        "inputs": "Suggest 3 unique app ideas for a new mobile app.",
    }
    response = requests.post(API_URL, headers=headers, json=payload)           # Sending a POST request to Hugging Face API

    if response.status_code == 200:
        app_ideas = response.json()
        generated_text = app_ideas[0]['generated_text']
        return generated_text
    else:
        print(f"Error: {response.status_code} - {response.text}")                ## Print error message if API request fails.
        return None

def random_talk():
    
    responses = [
        "I'm doing great, thanks for asking!",
        "I'm just a chatbot, but I'm always here to chat!",
        "I'm doing well, how about you?",
        "I'm here to help you with anything you need!",
        "Why don't you tell me something interesting?"
    ]
    return random.choice(responses)

def starting_talk():

    reply = [
        "Hello! How can I assist you today?",
        "Hi! How's it going?",
        "Hey! What's up?"
    ]
    return random.choice(reply)

def tell_joke():
    
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why don't programmers like nature? It has too many bugs!",
        "What do you get when you cross a snowman and a vampire? Frostbite!"
    ]
    return random.choice(jokes)

def chatbot():
    print("Chatbot: Hello! I can help you with new ideas. Let's chat!")

    while True:
        user_input = input("You: ").lower()     # Accept user input and convert it to lowercase for easy matching.
        if user_input == "what new app should i build?":
            print("Chatbot: Here are some app ideas:")
            app_ideas = generate_app_ideas()      # Generate app ideas using Hugging Face
            if app_ideas:
                print("1. A meditation app with rewards.")
                print("2. Grocery delivery for special diets.")
                print("3. Subscription service for AI-generated art.")
                
                user_choice = input("Chatbot: Please select the ideas by typing their numbers (e.g., '1 and 2', '1 and 3', '2 and 3'). ")
                choices = user_choice.split(" and ")

                print("\nChatbot: Here are the selected ideas:")

                for choice in choices:
                    if choice == "1":
                        print("Idea 1: A meditation app with rewards.")
                        print("Suggestion: You can build a mobile app that guides users through meditation sessions and A Meditation App with Rewards aims to combine the benefits of mindfulness with the motivation of gamification. The core idea is to guide users through various meditation sessions, helping them reduce stress, improve focus, and enhance overall well-being. The app would offer a range of guided meditation practices, including mindfulness, deep breathing, body scan, and even sleep meditations. The key feature of this app is the reward system. Users can earn points or virtual rewards for completing meditation sessions, maintaining streaks, or achieving specific milestones, such as meditation for a certain number of minutes or days. These rewards could be in the form of badges, virtual gifts, or even discounts on premium features. To further enhance engagement, the app could incorporate social features, like sharing progress with friends or joining challenges. Additionally, personalized meditation recommendations based on user preferences or progress can keep the experience fresh and motivating, ensuring long-term user retention.")
                    elif choice == "2":
                        print("Idea 2: Grocery delivery for special diets.")
                        print("Suggestion: Create an app that focuses on delivering groceries tailored to specific diets, such as gluten-free, vegan, or keto. A grocery delivery service for special diets focuses on providing customers with personalized, diet-specific food options delivered directly to their doorsteps. This service caters to individuals with dietary restrictions or preferences, such as gluten-free, keto, vegan, paleo, diabetic-friendly, or low-sodium diets. The key to success lies in understanding the unique needs of each customer and offering curated meal plans and ingredient boxes that align with their dietary goals. The app or platform can allow users to input their dietary preferences, health goals, or restrictions, and generate a customized shopping list. Integration with local suppliers and grocery stores ensures fresh and high-quality ingredients. Additionally, the platform can offer recipe suggestions, nutritional information, and tracking tools to help users maintain their diets. By focusing on convenience, health, and personalization, this service can help people save time, eat healthier, and stick to their dietary plans, all while supporting local businesses and sustainable food sourcing.")
                    elif choice == "3":
                        print("Idea 3: Subscription service for AI-generated art.")
                        print("Suggestion: Develop a subscription-based app where users can access AI-generated art. A Subscription Service for AI-Generated Art can be a unique platform that offers users access to digital artwork created by artificial intelligence. The service can be structured with different subscription tiers, each offering exclusive features such as personalized artwork, access to a broader library, or the ability to request custom art styles. For instance, a basic tier could provide access to a set of pre-generated art pieces, while a premium tier could allow users to interact with the AI, inputting their preferences (e.g., style, color scheme, theme) to generate bespoke artwork. The service could also offer users the ability to download high-resolution versions of the generated art for personal use or commercial licensing. The AI model can be trained on various artistic styles—abstract, realism, surrealism, etc.—to create diverse and unique artworks. This service would appeal to both individuals looking for personal art and businesses needing custom illustrations, designs, or marketing materials.")
                    else:
                        print(f"Invalid choice: {choice}. Please select valid options.")

        
        elif "how are you" in user_input or "how's it going" in user_input:
            print(f"Chatbot: {random_talk()}")

        elif "hi" in user_input or "hey" in user_input or "hello" in user_input:
            print(f"Chatbot: {starting_talk()}")

        elif "tell me a joke" in user_input or "joke" in user_input:
            print(f"Chatbot: {tell_joke()}")

        
        elif "help" in user_input or "commands" in user_input:
            print("Chatbot: You can ask me to:\n- Suggest new app ideas\n- Chat with me\n- Tell me a joke\n- Ask for help or commands")

       
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break

        else:
            print("Chatbot: I didn't quite understand that. You can ask for app ideas, talk to me, or ask for a joke.")

if __name__ == "__main__":
    chatbot()
