# Natalia Suska's Portfolio 

View Natalia's portfolio, including her paintings, drawings, and photographs. Also be able to submit payments for commissions.
Note: *Under any circumstances, you are not allows to repost any images throughout the website without Natalia's permission.* 
If cloning this file, before deploying your website to a server, replace **all** images. 


## Installation

Fork [this repo](https://github.com/nataliasuska/natalia), then clone or download the forked repo onto your local computer (for example to the Desktop), then navigate there from the command-line:

```sh
cd ~/Desktop/natalia/
```

Create a new file called ".env" and place the following contents inside, replcing the placeholder with your own keys. Please note that the current website is not yet fully configured, so these are not required yet. In future features, the contact form will be able to send an email via the SendGrid API, and, the Stripe payment processing will likewise be fully integrated. However, for good measure:

```sh
# this is the .env file...
APP_ENV="production"

SENDGRID_API_KEY = _________
SENDER_ADDRESS = _________


STRIPE_PUBLIC_KEY="pk_live_______________"
STRIPE_SECRET_KEY="sk_test_______________"
```
[More information on the SendGrid Package](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/sendgrid.md)
[More information on Stripe](https://stripe.com/docs)

Use Anaconda to create and activate a new virtual environment, perhaps called "website-env":

```sh
conda create -n website-env python=3.8
conda activate website-env
```

Then, within an active virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

## Usage

### Web App and Testing
You may choose to run this website locally. I have configured mine with Heroku so that anyone could reach it. However it's a good test to do so locally. Just run this command in your terminal(after installing requirements):

```
# mac:
FLASK_APP=website flask run
# windows:
export FLASK_APP=website
flask run
```

## Deploying to Heroku

### Prerequisites

If you haven't yet done so, [sign up for a Heroku account](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/heroku.md#prerequisites) and [install the Heroku CLI](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/heroku.md#installation), and make sure you can login and list your applications.

```sh
heroku login # just a one-time thing when you use heroku for the first time

heroku apps
```

> NOTE: When running `heroku login` in Git Bash, it hangs after successfully logging them in. If this is the case for you, close that Git Bash window and when you open a new one, making sure to go to the right directory.

### Server Setup

> IMPORTANT: run the following commands from the root directory of your repository!

Use the online [Heroku Dashboard](https://dashboard.heroku.com/) or the command-line (instructions below) to [create a new application server](https://dashboard.heroku.com/new-app), specifying a unique name (e.g. "notification-app-123", but yours will need to be different):

```sh
heroku create nataliasuska # this was mine - you must choose your own unique heroku name!
```

Verify the app has been created:

```sh
heroku apps
```

Also verify this step has associated the local repo with a remote address called "heroku":

```sh
git remote -v
```

## Deploying to Heroku

After this configuration process is complete, you are finally ready to "deploy" the application's source code to the Heroku server:

```sh
git push heroku main
```

> NOTE: any time you update your source code, you can repeat this deployment command to upload your new code onto the server

## Running the Script in Production

Once you've deployed the source code to the Heroku server, login to the server to see the files there, and take an opportunity to test your ability to run the script that now lives on the server:

```sh
heroku run bash 

# or alternatively, run it from your computer, in "detached" mode:
heroku run "python -m app.daily_briefing"
```
That's it!


## [License](https://github.com/nataliasuska/natalia/blob/main/LICENSE)

#### Note
This [repo is configured](https://codeclimate.com/github/nataliasuska/natalia) with Code Climate service. 
However, though I didn't integrate with Travis CI and don't have a 'test' folder, I did complete local website hosting tests before and even during deployment onto Heroku. It's what worked with my website, given that it is mostly HTML for my user's needs. 