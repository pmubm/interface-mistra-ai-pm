from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return "Hello World !"



@app.get('/square')
def square(n:int=5):
    return n*n



@app.get('/mistralai')
def mistralai(prompt):
    return prompt