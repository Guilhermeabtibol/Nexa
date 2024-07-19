const express = require('express');
const app = express();
const port = 3000;

//middleware para servir arquivos estaticos 
app.use(express.static('frontend'));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/frontend/index.html');
});

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`);
});