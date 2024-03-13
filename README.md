# Introducing Content Automater

Content Automater is a versatile tool designed to streamline the content creation and management process. By leveraging various technologies, it automates tasks such as scraping data from the "r/askReddit" subreddit, capturing screenshots, editing them into engaging videos, and uploading them directly to YouTube. 

# Key Features

1. **Reddit Scraping**
    - Utilizes PRAW to scrape posts and comments from the "r/askReddit" subreddit.

2. **Screenshot Capture**
    - Utilizes Selenium to identify elements by ID and take their screenshots to be included in the final product.

3. **Video Editing**
    - Uses MoviePy to edit the screenshots together without a background video into a final product.

4. **YouTube Upload**
    - Integrates with the YouTube Data API to upload the generated videos directly to your YouTube channel.



# Getting Started

To get started with contentAutomater, first, ensure you have installed the required dependencies:

```bash
pip install -r requirements.txt
```

Make sure to have the following resources in place as well: "**Folders for background gameplay, voiceovers, screenshots and final videos**


# License

contentAutomater is licensed under the MIT License. For more information, refer to the [License](LICENSE.md) file included in the repository.
