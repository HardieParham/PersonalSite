from src.app import create_app

my_app = create_app()
  
if __name__ == "__main__":
    print("Running app.")
    my_app.run(debug=False, host='0.0.0.0', port=5000)
