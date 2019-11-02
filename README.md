# Messenger Platform Sample

This is a sample project showcasing the Messenger Platform. You can go through the [walk-through](https://developers.facebook.com/docs/messenger-platform/guides/quick-start) to understand this code in more detail. The [Complete Guide](https://developers.facebook.com/docs/messenger-platform/implementation) goes deeper into the features available.

Visit the [dev site](https://developers.facebook.com/docs/messenger-platform/) to find out more details about the Messenger Platform.

To test thsi application :

Download or clone the code to your local directory:
https://github.com/SanjayIngole/ShopperChatter.git

Note : Install the Python libraries. Required for recognizing the colors.:

> npm install nltk
> npm install web-colors
> npm install colours

Update the validation token in your node/app.js file (Look for VALIDATION_TOKEN). You can either set the env varaible or hard code the value for testing purpose. 

Run the application 
> npm install
> node app.js


Once the application is up and running open a tunnel which will generate the URL that needs to be configured in the Messager App.

> lt --port 5000
your url is: https://neat-elephant-12.localtunnel.me

Set up the Webhook in you App on Devloper Dashboard. Set Callback URL and Validation token and save.

Open the Messanger on your phone and starting chatting with your App.

A sample interaction:

App : Welcome to Facebook Hackathon Chicago 2019. This is the a Smart Shopper with AI Project. At any time, use the menu below to navigate through the features. 
      
App: How can I help you today?

You : I am looking for a chair

App : Here's what I found. You can also filter by color.

<<List of Products>>

You : I want to buy a white chair

App : Here's what I found.

<<List of Products>>
Note: All the Products come with a link to see that product with Augmented Reality. User will have to enable the camera and see how the product looks.

You : Do you also have any tables?            

App: Sorry, we don't have any products like that 😞
