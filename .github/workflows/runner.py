name: 🐘 mastodon likes
on:

  schedule:
    - cron: 0 */5 * * *
  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

jobs:
  blog_post:
    runs-on: ubuntu-latest

    steps:
      - name: ➡️ Checkout the repo
        uses: actions/checkout@v2

      - name: 🐍 Set up Python 3.11
        uses: actions/setup-python@v2
        with:
          python-version: "3.11"

      - name: 👨‍💻 Install dependencies
        run: |
          pip install --upgrade pip
          pip install -r requirements.txt

      - name: 🐘🤖 Write toots
        run: python src/main.py
