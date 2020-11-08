const express = require('express');
const bodyParser = require('body-parser');  

const {conversation} = require('@assistant/conversation');

const app = conversation({debug: true});

app.handle('rich_response', conv => {
  conv.add('This is a card rich response.');
  conv.add(new Card({
    title: 'Card Title',
    subtitle: 'Card Subtitle',
    text: 'Card Content',
    image: new Image({
      url: 'https://developers.google.com/assistant/assistant_96.png',
      alt: 'Google Assistant logo'
    })
  }));
});
express().use(bodyParser.json(), app).listen(3000);


