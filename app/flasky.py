

from app import  create_app

app = create_app('prd')
if __name__=='__main__':
    app.run()