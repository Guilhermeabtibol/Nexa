document.getElementById('predictButton').addEventListener('click', async () => {
    const image = document.getElementById('imageInput').files[0];
    if (!image) {
      alert('Por favor, selecione uma imagem.');
      return;
    }
  
    const imgElement = document.createElement('img');
    imgElement.src = URL.createObjectURL(image);
    document.body.appendChild(imgElement);
  
    // Carregar o modelo
    const model = await tf.loadLayersModel('model.json');
  
    // Pré-processar a imagem
    const imgTensor = tf.browser.fromPixels(imgElement).resizeNearestNeighbor([224, 224]).toFloat().expandDims(0);
  
    // Fazer a previsão
    const predictions = await model.predict(imgTensor).data();
    const result = predictions[0]; // Dependendo do modelo, isso pode variar
    document.getElementById('result').innerText = `Predição: ${result}`;
  });
  