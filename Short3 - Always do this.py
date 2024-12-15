#  Copyright © 2024 AppMillers. 
#  Created by Elshad Karimov 
#  youtube.com/@app_millers
#  www.appmillers.com 

import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
print(f"Secret key: {SECRET_KEY}")