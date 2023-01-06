from src.app import create_flask_app
import warnings

warnings.filterwarnings('ignore')

if __name__ == '__main__':

    create_flask_app().run(
        host="0.0.0.0", 
        port=5000, 
        threaded=True, 
        debug=False
    )

