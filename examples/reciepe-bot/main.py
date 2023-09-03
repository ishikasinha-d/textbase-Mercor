from textbase import bot, Message
from textbase.models import OpenAI
from typing import List
from functions import get_feedback, give_feedback
import json

# Load your OpenAI API key
OpenAI.api_key = "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"


# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = f"""You are Chef Gabriella, a true culinary virtuoso. With her exceptional culinary skills and profound knowledge of ingredients, she transforms ordinary cooking into an extraordinary art. Gabriella's unique talent lies in her ability to craft awe-inspiring dishes from leftover ingredients, a skill that showcases her unparalleled creativity and ingenuity. Despite her culinary prowess, she remains remarkably gentle and approachable, making her a beloved mentor for beginners and seasoned enthusiasts alike. Gabriella is always ready to share her vast knowledge, offering patient guidance and answering questions with grace. Her expertise extends to effortlessly listing the ingredients for even the most complex recipes, an art form in itself. Chef Gabriella is a beacon of inspiration and mentorship, enriching the world of cuisine for all who have the privilege of learning from her.
Your goal is to help user ask relevant questions and create a dish based on the user's liking.
Previous dishes created by the user with their feedback: {get_feedback()}
"""

functions = [
    {
      "name": "give_feedback",
      "description": "template to have a user give feedback on a dish.",
      "parameters": {
        "type": "object",
        "properties": {
          "dish_name": {
            "type": "string",
            "description": "Name of the dish in consideration"
          },
          "cuisine_type": {
            "type": "string",
            "description": "Type of cuisine of the dish in consideration"
          },
           "feedback": {
            "type": "string",
            "description": "Feedback on the dish in consideration"
          }
        }
      }
    }
  ]


@bot()
def on_message(message_history: List[Message], state: dict = None):

    # Generate GPT-3.5 Turbo response
    bot_response = OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history, # Assuming history is the list of user messages
        model="gpt-3.5-turbo",
        functions = functions
    )

    if bot_response.get("function_call") is not None:
        bot_response["content"] = "Thank you for your feedback!"
        function_args = json.loads(bot_response["function_call"]["arguments"])

        # Call the function
        give_feedback(
            dish_name=function_args.get("dish_name", "Unknown"),
            cuisine_type=function_args.get("cuisine_type", "Unknown"),
            feedback=function_args.get("feedback", "Unknown")
        )

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",  
                    "value": bot_response["content"]
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }