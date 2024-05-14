const { error} = require('console');
const mqtt = require('mqtt');

const broker = 'https://test.mosquitto.org';
const topic = 'MASTER';

const client = mqtt.connect(broker);

client.on('connect', () =>{
    console.log('log au broker');

    client.subscribe(topic, (err) => {
        if (!err){
            console.log('on est abonnée !!!!');
        }
    });
});

client.on('message', (message) => {
    console.log('nous avons reçu : ' + message);
});

client.on('error', (err) =>{
    console.error("les problèmes de connection ... c'est trop triste")
});

client.on('close', () =>{
    console.log("et c'est la fin");
});