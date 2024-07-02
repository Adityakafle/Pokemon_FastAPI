# Pokemon API Project

It is the project which provides REST API to fetch and filter Pokemon list , their name and type.

## Setup Instructions

1. **Clone the Repository:**
   ```git bash
   git clone https://github.com/Adityakafle/Pokemon_FastAPI.git
2. **Install dependencies**
    ```git bash
    pip install -r requirements.txt

4. **Set Up POSTGRESQL**

   Install PostgreSQL and Create a new database and Update the database connection URL in pokemon_api/.env,  change username and password there to connect with postgresql server.

5. **Run the FASTAPI server**
    ```git bash
   uvicorn app.main:app --reload

 
 

5. **Accessing the API:**

   You can open any browser and enter the link :  http://127.0.0.1:8000/docs to interact with API , you can also send the parameters type and name with the endpoint.

   To see list of pokemons with their name, image and type hit the endpoint /api/v#/pokemons or enter the link: http://127.0.0.1:8000/api/v1/pokemons
