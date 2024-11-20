import openai
from abc import ABC, abstractmethod


class AiHandler(ABC):
    """
    Abstract base class for handling interactions with AI systems.
    """

    @abstractmethod
    def generate_card_with_image(self, prompt: str) -> dict:
        """
        Generates a card description with parameters and an associated image.

        Parameters:
        -----------
        prompt : str
            The textual prompt for generating card details and image.

        Returns:
        --------
        dict
            The AI-generated card data including an image URL.
        """
        pass


class OpenAIHandler(AiHandler):
    """
    A concrete implementation of AiHandler
    using OpenAI's API for text and image generation.
    """

    def __init__(self, api_key: str, model: str = "gpt-4"):
        """
        Initializes the OpenAIHandler with the given API key and model.

        Parameters:
        -----------
        api_key : str
            The API key required to access the OpenAI API.
        model : str
            The GPT model to use for text generation.
        """
        self.api_key = api_key
        self.model = model
        openai.api_key = api_key

    def generate_card_text(self, prompt: str) -> str:
        """
        Generates card text using the OpenAI API.

        Parameters:
        -----------
        prompt : str
            The textual prompt for generating card details.

        Returns:
        --------
        str
            The AI-generated card text in JSON format.
        """
        system_message = (
            "You are a card generator AI. Generate a "
            + "card in the following JSON format:\n"
            + """
{
  "title": "some title",
  "description": "describe the card",
  "ability": "describe the ability of this card",
  "type": "building|monster|effect",
  "valid_for": "number of turns that the card
  will be valid for (-1 if it is infinite)",
  "rarity": "common|rare|epic|legendary",
  "yeilds": {
    "each_turn": {
      "food": "0-5",
      "wood": "0-5",
      "iron": "0-5",
      "coins": "0-5"
    },
    "instant": {
      "food": "0-20",
      "wood": "0-20",
      "iron": "0-20",
      "coins": "0-20"
    }
  },
  "consumes": {
    "each_turn": {
      "food": "0-2",
      "wood": "0-2",
      "iron": "0-2",
      "coins": "0-2"
    },
    "instant": {
      "food": "0-10",
      "wood": "0-10",
      "iron": "0-10",
      "coins": "0-10"
    }
  },
  "stats": {
    "health": "10-90(for monsters or buildings only)",
    "damage": "3-25(for monsters only)"
  },
  "effects_on_me": {
    "each_turn": {
      "on_player": {
        "health": "0-3"
      },
      "on_monsters": {
        "health": "0-2",
        "damage": "0-2",
        "number_of_monsters": "-1 for all monsters"
      }
    },
    "instant": {
      "on_player": {
        "health": "0-10"
      },
      "on_monsters": {
        "health": "0-15",
        "damage": "0-15",
        "number_of_monsters": "-1 for all monsters"
      }
    }
  },
  "effects_on_enemy": {
    "each_turn": {
      "on_player": {
        "health": "negative number at most -3"
      },
      "on_monsters": {
        "health": "negative number at most -2",
        "damage": "negative number at most -2",
        "number_of_monsters": "-1 for all monsters"
      }
    },
    "instant": {
      "on_player": {
        "health": "negative number at most -10"
      },
      "on_monsters": {
        "health": "negative number at most -15",
        "damage": "negative number at most -15",
        "number_of_monsters": "-1 for all monsters"
      }
    }
  }
}
Ensure the card is either passive (has yields) or aggressive
(boosts or affects others). Respond with only JSON.
"""
        )

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt},
        ]

        try:
            response = openai.ChatCompletion.create(
                model=self.model, messages=messages, temperature=0.7
            )
            response_content = response.choices[0].message.content

            if isinstance(response_content, str):
                return response_content
            else:
                raise ValueError("Unexpected response format from OpenAI API.")
        except Exception as e:
            raise Exception(f"Error generating card text: {e}")

    def generate_card_image(self, description: str) -> str:
        """
        Generates a card image using the OpenAI API.

        Parameters:
        -----------
        description : str
            A description of the card for generating its image.

        Returns:
        --------
        str
            The URL of the generated image.
        """
        try:
            response = openai.Image.create(
                prompt=description, n=1, size="512x512"
            )
            return response["data"][0]["url"]
        except Exception as e:
            raise Exception(f"Error generating card image: {e}")

    def generate_card_with_image(self, prompt: str) -> dict:
        """
        Generates a card with text and an associated image.

        Parameters:
        -----------
        prompt : str
            The textual prompt for generating card details and image.

        Returns:
        --------
        dict
            The AI-generated card data including an image URL.
        """
        card_json = self.generate_card_text(prompt)

        try:
            card_data = eval(card_json)
            card_image_url = self.generate_card_image(card_data["description"])
            card_data["image_url"] = card_image_url
            return card_data
        except Exception as e:
            raise Exception(f"Error generating card with image: {e}")

    def send_card_request(self) -> dict:
        """
        Generates a card request with a predefined prompt.

        Returns:
        --------
        dict
            The generated card as a Python dictionary including an image.
        """
        prompt = (
            "Generate a creative card according to the provided JSON template."
        )
        return self.generate_card_with_image(prompt)
