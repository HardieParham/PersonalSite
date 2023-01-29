from app.app import Factory


app = Factory.create_app()

if __name__ == "__main__":
    app.run()