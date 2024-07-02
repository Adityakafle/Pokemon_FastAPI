# Pokemon API Project

It is the project which provides REST API to fetch and filter Pokemon list , their name and type.

## Setup Instructions

1. **Clone the Repository:**
   ```git bash
   git clone https://github.com/Adityakafle/Pokemon_FastAPI.git
2. **Install dependencies**
    ```git bash
    pip install -r requirements.txt

3. **Run the FASTAPI server**
    ```git bash
   uvicorn app.main:app --reload

4. **Accessing the API:**

   You can open any browser and enter the link :  http://127.0.0.1:8000/docs to interact with API , you can also send the parameters type and name with the endpoint.

   To see list of pokemons with their name, image and type hit the endpoint /api/v#/pokemons or enter the link: http://127.0.0.1:8000/api/v1/pokemons
