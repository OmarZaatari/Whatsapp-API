# Whatsapp Water Reminder Bot

This is a personal project that I started to learn about APIs and how to work with them.
## Resources
I used Meta's guide for using Whatsapp Business to get this up and running.
The glitch app is a remix of Whatsapp's template glitch application for deploying **Webhooks**.

Check out these resources:

- [**Webhook set up guide**](https://developers.facebook.com/docs/whatsapp/getting-started/signing-up/#configure-webhooks): The walkthrough for the code in this project.

- [**Quick start tutorial**](https://developers.facebook.com/docs/whatsapp/getting-started/signing-up/): Build your first app by remixing this project and following our quick start tutorial.

- [**WhatsApp Business Platform Documentation**](https://developers.facebook.com/docs/whatsapp/)

## Environment Setup

1. Create an account on Glitch to have access to all features mentioned here.
2. Remix this project on Glitch.
3. Click on the file `.env` on the left sidebar, and set these environment variables

- `WEBHOOK_VERIFY_TOKEN`: You can use any string and use the same when setting up the webhook in your app in the following steps.
- `GRAPH_API_TOKEN`: You can get a **Temporary access token** from the dashboard of your app on **Meta for Developers** when you click **API Setup** under the **WhatsApp** section on the left navigation pane.

4. Get the new Glitch URL to use as your webhook, eg: `https://project-name.glitch.me/webhook`. You can find the base URL by clicking on **Share** on top right in Glitch, copy the **Live Site** URL, then add `/webhook` to it.
5. Subscribe the webhook URL in the dashboard of your app on **Meta for Developers**. Click the **Configuration** menu under **WhatsApp** in the left navigation pane.
   In the **Webhook** section, click **Edit** and paste your webhook URL from the previous step. For the **Verify token** field, use the `VERIFY_TOKEN` value in your .env file, then click **Verify and save**.
   Under the **Webhook fields** section click **Manage** and make sure **messages** field is selected.
6. Edit `server.js` to change the webhook logic as needed.
7. Click on the **Logs** tab at the bottom to view server logs. The logs section also has a button to attach a debugger via Chrome devtools.
