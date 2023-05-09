# from flask import Flask, render_template
# from app.views import views


# my_app = Flask(__name__, static_folder='app/static', template_folder='app/templates')
# my_app.register_blueprint(views)

# @my_app.route('/')
# def base():
#     return render_template('base.html')
# if __name__ == "__main__":
#     my_app.run(debug=False)



from app.app import create_app
my_app = create_app()  
if __name__ == "__main__":
    my_app.run(debug=False)




# PLAN 
#
# FRONTEND
# Header DONE
# Navbar DONE
# Content area with AJAX requests
# Footer DONE
# Styling
# 
# BACKEND
# Routes DONE
# Content 
# Photos / icons
# 
# 
# #