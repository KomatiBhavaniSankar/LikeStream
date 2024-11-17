

https://github.com/user-attachments/assets/d0ef5c43-a8c4-4d96-a014-b953b872fd42

# LikeStream
LikeStream is a minimal blogging site built using the Django web framework. It allows users to post blogs, interact with others through comments, and engage with content via likes.
OVERVIEW VIDEO OF LIKESTREAM : https://drive.google.com/file/d/1M-ieMNC2RZLoLYdwmS1PEHmilP7Bcsag/view?usp=sharing
# Features

- User registration and login.
- Create, edit, and delete blog posts.
- Like posts.
- Comment on posts.
- Search functionality.
- Responsive design.
- User profiles.
- Admin dashboard.

# Installation and Setup

###### **Prequisites** as per the `requirements.txt`

``` txt
asgiref==3.8.1
boto3==1.34.117
botocore==1.34.117
crispy-bootstrap4==2024.1
dj-database-url==2.2.0
Django==4.2
django-crispy-forms==2.1
django-storages==1.14.3
djangorestframework==3.15.1
drf-yasg==1.21.7
gunicorn==22.0.0
inflection==0.5.1
jmespath==1.0.1
packaging==24.0
pillow==10.3.0
psycopg2==2.9.9
psycopg2-binary==2.9.9
python-dateutil==2.9.0.post0
pytz==2024.1
PyYAML==6.0.1
s3transfer==0.10.1
six==1.16.0
sqlparse==0.5.0
typing_extensions==4.12.1
tzdata==2024.1
uritemplate==4.1.1
urllib3==1.26.19
```

1. **Install Git**
First, you need to install Git on your local machine if you haven't already. You can download it from the Git website and follow the installation instructions for your operating system.

**For Linux users**
```bash
sudo apt install git 
```

**For Windows users**
- Refer to the Microsoft store or visit the https://git-scm.com/download/win

2. **Install Python and Django**
Make sure you have Python and Django installed on your system. You can download Python from the Python website, and you can install Django using pip:

``` bash
pip install django
```

3. **Clone the Repository**
Open your terminal or command prompt and navigate to the directory where you want to clone the project. Use the git clone command followed by the URL of the GitHub repository.

``` bash
git clone https://github.com/BhavaniShankar2004/LikeStream.git
```

4. **Navigate to the Project Directory**
Change into the newly created directory that contains the cloned project:

```bash
cd LikeStream
```

5. **Set Up a Virtual Environment**
It is a good practice to use a virtual environment for your Django project to manage dependencies. You can create a virtual environment using the following command:

```bash
python -m venv venv
```


6. **Activate the virtual environment**
On Windows:
``` powershell
venv\Scripts\activate
```

On macOS and Linux:
``` bash
source venv/bin/activate
```


7. **Install Dependencies**
Install the required dependencies listed in the requirements.txt file. Run the following command:

``` bash
pip install -r requirements.txt
```

8. Configure the Database
Depending on the database used by the project, you might need to set up and configure your database. This usually involves:
- Creating a new database.
- Updating the DATABASES setting in the settings.py file with your database credentials.

9. **Run Migrations**
Apply the database migrations to set up the database schema. Run the following command:

``` bash
python manage.py migrate
```

10. **Create a Superuser**
Create a superuser account to access the Django admin interface:

``` bash
python manage.py createsuperuser
```

11. **Run the Development Server**
Start the Django development server to verify that everything is working correctly:

``` bash
python manage.py runserver
```

Open your web browser and navigate to http://127.0.0.1:8000/ to see your Django project in action.


Additional Steps (if applicable)
Set Up Environment Variables: If the project uses environment variables (e.g., for secret keys, API keys, etc.), create a .env file in the project root and add the necessary variables.
Static and Media Files: Ensure that static and media files are correctly set up. This might involve running python manage.py collectstatic and configuring AWS S3 or another service for media file storage.
That's it! You should now have a cloned and running Django project from GitHub. If you encounter any issues, refer to the project's README file for additional instructions specific to the project.



# Features and Functionality

**User Authentication:**
- **Register:** Users can create an account with a username, email, and password.
- **Login/Logout**: Users can log in and log out of their accounts.
- **Profile**: Users can view and update their profiles.

**Blog Management:**
- **Create Post:** Users can create new blog posts.
- **Edit Post:** Users can edit their existing posts.
- **Delete Post:** Users can delete their posts.

**Comments:**
- **Add Comment:** Users can comment on blog posts.
- **Edit/Delete Comment:** Users can edit or delete their comments.

**Likes:**
- **Like Post:** Users can like posts.


**Search (posts/users):**
- **Search:** Users can search posts by keywords.
- **Admin Dashboard**
- **Manage Users:** Admins can manage user accounts.
- **Manage Posts and Comments:** Admins can oversee posts and comments.


# Contributing

If you’re open to contributions:

- **Fork the Repository:** Create a personal copy of the repository.
- **Create a Feature Branch:** Work on a new feature or fix on a separate branch.
- **Submit a Pull Request:** Submit a pull request with your changes.


# Licensing

Specify the license under which the project is distributed. For example:
This project is licensed under the MIT License - see the [LICENSE]() file for details.

