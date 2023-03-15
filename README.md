# ChatGPT_API

## Intro

This Python script uses OpenAI's GPT-3 language model to prompt the user for a rating and comment on an answer provided to a question. The script extracts the rating and comment from the user's response and returns them in a dictionary. 

If the user's response is not in JSON format, the script attempts to extract the rating and comment using regular expressions. If it fails to do so, it assigns a default rating of 0 and returns the user's response as the comment.

The script requires the OpenAI API key, which should be set as an environment variable "OPENAI_API_KEY". The script also imports the following modules:

**openai**: The official Python client for the OpenAI API.
**os**: This module provides a way of interacting with the operating system.
**dotenv**: This module loads environment variables from a .env file.
The extract_int function takes a string and returns an integer extracted from the string, using regular expressions. If the string does not contain a valid integer, it returns None.

**Overview**: 

The chatGPT_output function takes a question and answer as input and prompts the user to rate the answer and provide a comment. The function then extracts the rating and comment from the user's response and returns them in a dictionary. If the user's response is not in JSON format, the function attempts to extract the rating and comment using regular expressions. If it fails to do so, it assigns a default rating of 0 and returns the user's response as the comment.

To use the script, set the OPENAI_API_KEY environment variable to your OpenAI API key, and call the chatGPT_output function, passing in the question and answer as arguments.

**Use**:    <br> <br>
`pip install -r requirements.py`    <br>
`python app.py`

- Note:
Its recommended to create a virtualenv and use that

<br>


`virtualenv myenv1`    <br>
`source myenv1/bin/activate`