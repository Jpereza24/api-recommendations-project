# api-recommendations-project

The goal of this project is to create an API based on a database of conversations that some users have had in different chats.

The API has functions to get all the data from the database, all the users and their messages, create a new user and a new message in the database, get the sentiment that can be extracted from the conversations in a chat and another one to recommend friends to a user based on its conversations in the different chats.

The files in this repository are the following:

- api:
    - Where is stored all the code of the different functions of the API.

- Input:
    - Folder where is the json with the original database.

- Output:
    - Folder where I have storage the jsons of the different collections that I have charged in MongoAtlas.

- src:
    - Folder with 2 functions:
        - mongo_connection.py: To connect with MongoAtlas.
        - user_text.py: To clean a query from MongoAtlas into a dictionary.

- MongoAtlas:
    - File to establish to upload the database to MongoAtlas.

- Jupyter Notebooks to try the different functions of the API and to upload new collections to MongoAtlas.