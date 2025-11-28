#References:
# https://www.geeksforgeeks.org/python/making-a-flask-app-using-a-postgresql-database/
# https://www.geeksforgeeks.org/python/python-introduction-to-web-development-using-flask/
# https://stefanopassador.medium.com/docker-compose-with-python-and-posgresql-45c4c5174299
# https://www.docker.com/blog/how-to-use-the-postgres-docker-official-image/
# https://www.psycopg.org/docs/install.html
# https://csveda.com/postgresql-flask-database-display-data-in-a-web-page/
# # OpenAI. (2025). ChatGPT (GPT-5 ) [Large language model]. Code partially generated for psycopg2 connection
# & data distribution assistance and debugging. https://chat.openai.com/chat


#import dependencies
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
import os
load_dotenv()
from flask import Flask, render_template


app = Flask(__name__)

#establish db connection
conn = psycopg2.connect(dbname="ElFroggodb", user="ElFroggo", password=os.getenv('POSTGRES_PASSWORD'), host="db", port="5432")

#enable us to access values using dictionary key/values
curr = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#create table if not existing already 
curr.execute(''' CREATE TABLE IF NOT EXISTS Frogs (
    ID SERIAL,
    Name VARCHAR(26),
    ScientificName VARCHAR(50),
    Color VARCHAR(26),
    PRIMARY KEY(ID)
) ''')

#if the values don't exist in the db already, insert them
curr.execute("SELECT COUNT(*) FROM Frogs")
count = curr.fetchone()[0]

if count == 0:
    curr.execute(''' INSERT INTO Frogs (Name, ScientificName, Color)
                    VALUES ('Billy', 'Leiopelma', 'Blue'), ('Stephen Island Frog', 'Leiopelma hamiltoni', 'Turquoise'), 
                            ('Western Spadefoots', 'Spea', 'Light Green'), ('Plains Spadefoot', 'Spea bombifrons', 'Green & yellow-spotted'),
                            ('Great Basin Spadefoot', 'Spea intermontana', 'Blue & yellow-spotted')
                ''')
conn.commit()
curr.close()
conn.close()

#create a route to post the data in on the webpage (template page)
@app.route("/frogs")
def frogs():
    conn = psycopg2.connect(dbname="ElFroggodb", user="ElFroggo", password=os.getenv('POSTGRES_PASSWORD'), host="db", port="5432")
    curr = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    frogs=curr.execute("SELECT * FROM Frogs")
    frogs = curr.fetchall()
    curr.close()
    conn.close()
    return render_template("index.html", frogs=frogs)


#run on port 5000 and localhost
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
