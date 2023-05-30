# Development 🔧


## Getting Started
1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
```sh
$ git clone https://github.com/your-username/clubs-event-platform-backend.git
$ cd clubs-event-platform-backend
```

### For setting virtual environment

```sh
$ virtualenv venv
```

### For activating virtual environment in Windows

```sh
$ venv/Scripts/activate
```

### For activating virtual environment in Linux and macOS

```sh
$ source venv/bin/activate
```

### For deactivating virtual environment
```sh
$ deactivate
```
After creating virtual environment

### Start

```sh
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```


## Contributing a New feature
Create a new branch for your contribution.
```sh
$ git checkout -b your_name/unique_feature_name
```

### Making Changes and Pushing
1. Make your desired changes to the codebase.
2. Test your changes thoroughly to ensure they work as expected.
3. Document any new features, modifications, or important considerations.
4. Commit your changes with a descriptive commit message.
5. Push your changes to your forked repository.
```sh
$ git commit -m "Add new feature: ..."
$ git push origin my-contribution
```

### Creating a Pull Request
1. Go to the original repository on GitHub.
2. Switch to the branch you just pushed.
3. Click on the "New Pull Request" button.
4. Fill out the necessary details and provide a descriptive summary of your changes.
5. Submit the pull request for review.

## Code Review and Feedback
Once you have submitted a pull request, the project maintainers will review your changes. They may provide feedback or request further modifications. Please respond to any comments in a timely manner and make the necessary adjustments.


