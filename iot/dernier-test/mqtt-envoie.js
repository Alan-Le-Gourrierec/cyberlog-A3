const { error } = require('console');
const mqtt = require('mqtt');

const broker = 'https://test.mosquitto.org';
const topic = 'MASTER';

const client = mqtt.connect(broker);

function publishMessage() {
    const message = 'Salut mon pote ^^';
    client.publish(topic, message);
    console.log('le message ' + message + 'à été envoyé')
}

client.on('connect', () => {
    console.log('on se connect');
    setInterval(publishMessage,10000)
});

client.on('error', (err) => {
    console.error('NOOOOONNNNNNN une erreur');
});

client.on('close', () =>{
    console.log("Et c'est fermé ... dommage, une prochaine fois peu être ^^");
});