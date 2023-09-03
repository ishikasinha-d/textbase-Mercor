## Overview

Food Wizard is your virtual kitchen companion, designed to make cooking an enjoyable and hassle-free experience. Whether you're a seasoned chef or a beginner in the kitchen, Food Wizard is here to assist you in every step of your culinary journey. With its wide range of features, this AI-powered bot helps you discover, create, and savor delicious meals tailored to your preferences and skill level.

[Demonstration Video](https://www.loom.com/share/5bd2b640a5544fdcbf643f423d887f3f)

## Key Features:

1. **Personalized Recipe Recommendations:**

   - Food Wizard understands your dietary preferences, ingredient availability, cooking skill level, and the time you have on hand.
   - It suggests recipes that align with your tastes, dietary restrictions, and the ingredients you currently have, ensuring a seamless and customized cooking experience.

2. **Ingredient Substitution Expert:**

   - If you have dietary restrictions or need ingredient substitutions, Food Wizard offers creative and suitable alternatives, ensuring you can still enjoy your favorite dishes.

3. **Cooking Coach:**

   - Food Wizard acts as your cooking coach, providing clear, step-by-step instructions for each recipe.
   - It guides you through the entire cooking process, from preparation to plating, ensuring your meals turn out perfectly every time.

4. **Cocktail Creation Assistant:**

   - For those looking to mix up some refreshing beverages, Food Wizard provides cocktail recipes and instructions.
   - It suggests cocktails based on the ingredients you have, allowing you to become a home bartender with ease.

5. **Leftover Food Innovator:**

   - Food Wizard helps you reduce food waste by offering creative and delicious recipes that make use of leftover ingredients.
   - It turns last night's dinner into today's culinary masterpiece.

6. **YouTube Recommendations:**

   - If you prefer visual cooking guides, Food Wizard recommends cooking tutorial videos from YouTube.
   - You can follow along with expert chefs and expand your culinary skills.

7. **Feedback System for Continuous Improvement:**

   - Food Wizard values your input and encourages users to provide feedback on recipes and recommendations.
   - If you have a positive experience or encounter any issues, you can share your feedback directly with Food Wizard.
   - Negative feedback helps Food Wizard improve its recommendations by avoiding similar suggestions in the future.

## Benefits:

- **Effortless Meal Planning:** Food Wizard simplifies meal planning by suggesting recipes that match your preferences and available ingredients.

- **Variety and Creativity:** Explore a wide range of recipes and cocktail ideas to keep your meals exciting and unique.

- **Reduced Food Waste:** Say goodbye to wasted ingredients with Food Wizard's leftover food recipes.

- **Skill Enhancement:** Whether you're a beginner or an experienced cook, Food Wizard helps you level up your culinary skills.

- **Time Savings:** Get quick and easy recipe recommendations based on your available time, making weekday dinners a breeze.

- **Dietary Support:** Food Wizard ensures that your dietary preferences and restrictions are respected in every recipe suggestion.

With Food Wizard by your side, cooking becomes an enjoyable adventure, and every meal you prepare is a masterpiece. Say goodbye to meal planning stress and food waste, and say hello to a world of culinary possibilities. Whether you're seeking inspiration, cooking guidance, or a refreshing drink recipe, Food Wizard has it all at your fingertips.

<p align="center">
  <picture>
    <img alt="Textbase python library" src="assets/logo.svg" width="352" height="59" style="max-width: 100%;">
  </picture>
  <br/>
  <br/>
</p>

<p align="center">
    <a href="https://docs.textbase.ai">
        <img alt="Documentation" src="https://img.shields.io/website/http/huggingface.co/docs/transformers/index.svg?down_color=red&down_message=offline&up_message=online">
    </a>
</p>

<h3 align="center">
    <p>✨ Textbase is a framework for building chatbots using NLP and ML. ✨</p>
</h3>

<h3 align="center">
    <a href="https://textbase.ai"><img src="assets/banner.png"></a>
</h3>

Just implement the `on_message` function in `main.py` and Textbase will take care of the rest :)

Since it is just Python you can use whatever models, libraries, vector databases and APIs you want.

Coming soon:

- [x] [PyPI package](https://pypi.org/project/textbase-client/)
- [x] Easy web deployment via [textbase deploy](/docs/deployment/deploy-from-cli)
- [ ] SMS integration
- [ ] Native integration of other models (Claude, Llama, ...)

![Demo Deploy GIF](assets/textbase-deploy.gif)

## Installation

Make sure you have `python version >=3.9.0`, it's always good to follow the [docs](https://docs.textbase.ai/get-started/installation) 👈🏻

### 1. Through pip

```bash
pip install textbase-client
```

### 2. Local installation

Clone the repository and install the dependencies using [Poetry](https://python-poetry.org/) (you might have to [install Poetry](https://python-poetry.org/docs/#installation) first).

For proper details see [here]()

```bash
git clone https://github.com/cofactoryai/textbase
cd textbase
poetry shell
poetry install
```

## Start development server

> If you're using the default template, **remember to set the OpenAI API key** in `main.py`.

Run the following command:

- if installed locally
  ```bash
  poetry run python textbase/textbase_cli.py test
  ```
- if installed through pip
  `bash
  textbase-client test
  `
  Response:

```bash
Path to the main.py file: examples/openai-bot/main.py # You can create a main.py by yourself and add that path here. NOTE: The path should not be in quotes
```

Now go to the link in blue color which is shown on the CLI and you will be able to chat with your bot!
![Local UI](assets/test_command.png)

### `Other commands have been mentioned in the documentaion website.` [Have a look](https://docs.textbase.ai/usage) 😃!

## Contributions

Contributions are welcome! Please open an issue or create a pull request.
