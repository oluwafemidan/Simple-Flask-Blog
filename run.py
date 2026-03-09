from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

# from app({'flaskblog'}folder/module) import app(object/variable) and when you're working with packages that is going to import
# from the __init__.py file within that package so that app variable has to exist
# within __init__.py 

# >>> tree /f

# >>> from app import app,db
# >>> app.app_context().push()
# >>> db.create_all()

# Run the development web server