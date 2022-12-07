
# T&C and Privacy Policy Generator

This platform allow users to generate Terms and Conditions (T&C) and Privacy Policy
# Documentation

## Run Locally

The first thing to do is to clone the repository:

```bash
  git clone git@github.com:zuri-training/Reindeer2-T_c_gen.git
```

Go to the project directory
```bash
  cd Reindeer2-T_c_gen
```

Create a virtual environment to install dependencies in and activate it:

```bash
  virtualenv -p python3 env
  /env/scripts/activate
```

Then install the dependencies:
```bash
  (env) pip install -r requirements.txt  
```

Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:

```bash
  (env) cd t_c_gen
```

Start the server
```bash
  (env)$ python manage.py runserver  
```

And navigate to http://127.0.0.1:8000/t_c_policy_gen/ on your browser


# Features

You can now interact with the application as a Guest.

## Guest User: Unauthenticated

1. Can only view basic information about the application
2. Can only view and interact with the applications documentations
3. Needs to register to view more details
4. Have limited access to application functionalities


- To have full access to the application functionalities, you will need to be a REGISTERED USER.

## Registered User: Authenticated
1. Full access to the application
2. Can enter basic information
3. Can generate selected files with the right data and information
4. Allowed to export, download, share and use website embed
5. Allow user save data and come back to download

- To have access as a regsitered user, kindly use the following credentials:
- username: testuser
- password: testpass


## Tech Stack

**Client:** • HTML • CSS • JavaScript

**Server:** • Python • Django

**Design:** • Figma


## Useful Resources

- Database Schema
- Designs from the Product Design Team
## Contributors

- [@Team Reindeer2](https://www.github.com/)


## Acknowledgements

 I4G x Zuri Training 
## License

[MIT](https://choosealicense.com/licenses/mit/)

