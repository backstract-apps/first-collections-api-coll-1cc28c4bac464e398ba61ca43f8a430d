from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - first-collections-api-coll-1cc28c4bac464e398ba61ca43f8a430d',debug=False,docs_url='/elated-blackwell-482e3aa8bea611ef95970242ac12000546/docs',openapi_url='/elated-blackwell-482e3aa8bea611ef95970242ac12000546/openapi.json')

app.include_router(router, prefix='/elated-blackwell-482e3aa8bea611ef95970242ac12000546/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()